import os

# Specify the directory path; use '.' for current directory
path = '/home/ayush/workspace_git'

# List all entries in the directory
entries = os.listdir(path)

# Print the entries
print(f"Contents of directory '{path}':")
for entry in entries:
    print(entry)
