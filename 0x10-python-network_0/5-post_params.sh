#!/bin/bash
# Bash script takes URL, sends POST request URL & displays body of response
curl -s -X POST -d "email=test@gmail.com&subject=I will always be here for PLD" "$1"
