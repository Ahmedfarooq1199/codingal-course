const express = require('express');
const Database = require('better-sqlite3');
const path = require('path');

const PORT = process.env.PORT || 3000;
const ADMIN_TOKEN = process.env.ADMIN_TOKEN || 'change-me';
const MAX_TEAMS = 32;

const db = new Database(path.join(__dirname, 'tournament.db'));
db.exec(`CREATE TABLE IF NOT EXISTS teams (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT UNIQUE NOT NULL,
  captain TEXT NOT NULL,
  email TEXT NOT NULL,
  platform TEXT NOT NULL,
  members TEXT NOT NULL,
  wins INTEGER NOT NULL DEFAULT 0,
  losses INTEGER NOT NULL DEFAULT 0,
  kills INTEGER NOT NULL DEFAULT 0,
  created_at TEXT DEFAULT CURRENT_TIMESTAMP
)`);

const app = express();
app.use(express.json({ limit: '10kb' }));
app.use(express.static(path.join(__dirname, 'public')));

// basic per-IP rate limit for registrations
const hits = new Map();
const limited = (req, res, next) => {
  const now = Date.now(), ip = req.ip;
  const recent = (hits.get(ip) || []).filter(t => now - t < 600000);
  if (recent.length >= 5) return res.status(429).json({ error: 'Too many attempts. Try again in a few minutes.' });
  recent.push(now); hits.set(ip, recent); next();
};

const clean = (v, max) => String(v || '').trim().slice(0, max);

app.get('/api/teams', (_req, res) => {
  res.json({
    max: MAX_TEAMS,
    teams: db.prepare('SELECT id,name,platform,wins,losses,kills FROM teams ORDER BY wins DESC, kills DESC, name').all()
  });
});

app.post('/api/register', limited, (req, res) => {
  const name = clean(req.body.name, 30), captain = clean(req.body.captain, 30);
  const email = clean(req.body.email, 80), platform = clean(req.body.platform, 10);
  const members = clean(req.body.members, 150);
  if (!name || !captain || !members) return res.status(400).json({ error: 'Fill in team name, captain and squad gamertags.' });
  if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email)) return res.status(400).json({ error: 'Enter a valid email address.' });
  if (!['PC', 'PlayStation', 'Xbox'].includes(platform)) return res.status(400).json({ error: 'Choose a platform.' });
  if (db.prepare('SELECT COUNT(*) c FROM teams').get().c >= MAX_TEAMS) return res.status(409).json({ error: 'Registration is full.' });
  try {
    db.prepare('INSERT INTO teams (name,captain,email,platform,members) VALUES (?,?,?,?,?)').run(name, captain, email, platform, members);
    res.status(201).json({ ok: true });
  } catch (e) {
    if (String(e.message).includes('UNIQUE')) return res.status(409).json({ error: 'That team name is taken.' });
    res.status(500).json({ error: 'Something went wrong. Try again.' });
  }
});

// Admin: record a match result. Header: x-admin-token
app.post('/api/admin/result', (req, res) => {
  if (req.get('x-admin-token') !== ADMIN_TOKEN) return res.status(401).json({ error: 'Unauthorized' });
  const { winnerId, loserId, winnerKills = 0, loserKills = 0 } = req.body;
  const tx = db.transaction(() => {
    db.prepare('UPDATE teams SET wins=wins+1, kills=kills+? WHERE id=?').run(+winnerKills || 0, winnerId);
    db.prepare('UPDATE teams SET losses=losses+1, kills=kills+? WHERE id=?').run(+loserKills || 0, loserId);
  });
  tx();
  res.json({ ok: true });
});

app.delete('/api/admin/teams/:id', (req, res) => {
  if (req.get('x-admin-token') !== ADMIN_TOKEN) return res.status(401).json({ error: 'Unauthorized' });
  db.prepare('DELETE FROM teams WHERE id=?').run(req.params.id);
  res.json({ ok: true });
});

app.listen(PORT, () => console.log(`Tournament site running on http://localhost:${PORT}`));
