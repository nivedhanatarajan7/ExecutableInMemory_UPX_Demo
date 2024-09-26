# Running Executable Files in Memory using UPX

# Overview of Repository
1. `create_exe.py`: Creates executable files
2. `run_exe.py`: Runs executable files in memory
3. `helloworld.py`: Script that will be converted to an executable file
4. `main.py`: Driver that creates executable files and runs executable files in memory

# Execution Process

## Create Executable File
The `create_exe.py` script creates an executable file based on a Python script using the Pyinstaller library. In this demo, the helloworld.py script contains a print statement "Hello World." The Pyinstaller tool converts this script to an executable file is in the `dist/` directory.

## Run Executable Files in Memory
The `run_exe.py` script runs the created executable files in memory using the UPX packer tool (https://upx.github.io/). This tool compresses the executable file. When running the executable file, the file is decompressed and run in memory.

# How To Run Script
Run the `main.py script` using the command `python main.py`. This script will create a `helloworld.exe` executable in the `dist/` directory and run the executable file in memory using the UPX tool.
