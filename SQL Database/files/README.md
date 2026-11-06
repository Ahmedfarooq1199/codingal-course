# Operation Crossfire – COD Tournament Site
Stack: Node.js + Express + SQLite (better-sqlite3), vanilla HTML/CSS/JS frontend.

    npm install
    ADMIN_TOKEN=your-secret npm start      # http://localhost:3000

Record a result:
    curl -X POST localhost:3000/api/admin/result -H "content-type: application/json" \
      -H "x-admin-token: your-secret" -d '{"winnerId":1,"loserId":2,"winnerKills":38,"loserKills":29}'
Remove a team: DELETE /api/admin/teams/:id with the same header.
Edit prize pool, dates and rules directly in public/index.html.
