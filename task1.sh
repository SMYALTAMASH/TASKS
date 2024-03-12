#!/bin/bash
# To Run this script use below command
# sudo bash -x ./task1.sh /path/to/shared/directory

if [ "$(id -u)" != "0" ]; then
    echo "This script must be run as root" 
    exit 1
fi

if [ $# -eq 0 ]; then
    echo "Usage: $0 <directory_path>" 
    exit 1
fi
echo $1
shared_dir=$1

if [ -d "$shared_dir" ]; then
    echo "Directory already exists"
else
    mkdir -p "$shared_dir"
    echo "Shared directory created at $shared_dir"
fi

chmod 777 "$shared_dir"

# Allow any developer to modify existing files and directories
chmod +t "$shared_dir"

echo "Permissions set for the shared directory:"
ls -ld "$shared_dir"

# Assumptions
echo -e "It needs to be run with root privileges to create and set permissions on directories.\nAbsolute path need to be given and not relative path\nThe script accepts one argument, which is the path to the directory where the "shared" directory will be created.\nDevelopers have SSH/SFTP access to the server.\nThe script checks if the shared directory already exists and creates it if it doesn't.\nIt sets the permissions of the shared directory to allow any developer to read, write, and modify existing files and directories within it.\nThe "+t" option sets the sticky bit on the directory, which means that only the owner of a file can delete or rename it within the directory, preventing other developers from deleting or renaming files they don't own.\nThe script informs the user about the permissions set for the shared directory.
"
