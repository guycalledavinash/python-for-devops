# Directory Listing CLI

`cli-argument.py` lists entries in one or more directories. It can include subdirectories recursively and filter names by file extension.

Run these commands from the repository root:

```bash
# List entries in one directory or several directories
python Day-10/cli-argument.py ./Day-10 ./Day-11

# Include files in subdirectories
python Day-10/cli-argument.py ./Day-10 --recursive

# Include only Python and text files
python Day-10/cli-argument.py ./Day-10 --extensions .py .txt
```

Names are sorted alphabetically without regard to letter case. Recursive mode also sorts directory names before visiting them. Deterministic ordering makes command output easier to compare and helps automation produce repeatable results.
