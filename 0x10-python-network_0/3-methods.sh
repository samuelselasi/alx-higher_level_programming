#!/bin/bash
# Bash script that takes URL and displays all HTTP methods server will accept
curl -s -I "$1" | grep "Allow" | cut -d " " -f 2-
