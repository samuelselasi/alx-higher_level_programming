#!/bin/bash
# Bash script sends JSON POST request to URL as 1st arg & disp body response
curl -s -H "Content-Type: application/json" -d "$(cat "$2")" "$1"
