#!/bin/bash

# Search for files with names that match "password" in the provided path recursively
files=$(find "$1" -type f -name "*password*")

if [ -z "$files" ]; then   
    echo "[]"
else
    echo "$files" | tr '\n' ' ' | sed 's/ $//'
fi
