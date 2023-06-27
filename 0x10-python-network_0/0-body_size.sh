#!/bin/bash
# Bash script takes URL, sends request to URL & displays size of body response
curl -s "$1" | wc -c
