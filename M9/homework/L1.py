def write_file(filename, content):
try:
with open(filename, "w", encoding="utf-8") as f:
f.write(content)
print(f"Successfully wrote to {filename}")
except Exception as e:
print(f"Error writing file: {e}")


# Function to read data from a file


def read_file(filename):
try:
with open(filename, "r", encoding="utf-8") as f:
data = f.read()
print(f"Contents of {filename}:")
print(data)
except FileNotFoundError:
print(f"File '{filename}' not found.")
except Exception as e:
print(f"Error reading file: {e}")


# Function to append data to a file


def append_file(filename, content):
try:
with open(filename, "a", encoding="utf-8") as f:
f.write(content)
print(f"Successfully appended to {filename}")
except Exception as e:
print(f"Error appending to file: {e}")



if __name__ == "__main__":
file_name = "demo.txt"


write_file(file_name, "Hello! This is the first line.\n")


append_file(file_name, "This is an appended line.\n")



read_file(file_name)