# vshell

vshell is a custom Python mini-shell that lets you interact with your filesystem and run Python scripts from a colorized command-line interface. Designed as a learning project, it mimics basic Unix-like shell behavior while providing a playground for Python scripting and process management.

## Features

- Navigate directories with ```cd``` and view contents with ```ls```

- Create files (touch) and directories (mkdir)

- Edit files using nano via the ```edit``` command

- Delete files with ```rm```

- Run Python scripts with ```py <filename>```

- Built-in echo, clear, and exit commands

- Friendly, colorized CLI prompt

- Handles Ctrl+C gracefully and ignores Ctrl+Z

- Run any command using ```run <command>``` even if its not on vshell!
  
example:
```
run clitube --play --id dQw4w9WgXcQ --loop --no-video
**video runs**
```

## Installation

1. Clone the repository:
```
git clone https://github.com/VxidDev/vshell.git
```
2. Navigate to the project folder:
```
cd vshell
```
3. Run using python.
```
python main.py
```
(PACKAGING COMING SOON!)

### Example usage
```
vshell @ /home/vxid-dev > echo example
example
vshell @ /home/vxid-dev > touch file 
vshell @ /home/vxid-dev > mkdir folder
vshell @ /home/vxid-dev > exit
```
## Requirements

- Python 3.8+

- Unix-like OS recommended (Linux/macOS)

- nano editor installed for edit command

## Notes

This is a learning project to understand shell internals, process handling, and file management in Python.

Works as a standalone CLI; doesn’t require additional libraries except colorama.
