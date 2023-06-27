#!/bin/bash
# Bash script takes URL as arg, sends GET request to URL & disp body response
curl -s -H "X-School-User-Id: 98" "$1"
