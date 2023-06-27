#!/bin/bash
# Bash script that makes reuest that causes the server to respond with message
curl -s -X PUT -H "Content-Length: 0" -H "X-HolbertonSchool-User-Id: 98" -H "Origin: HolbertonSchool" -L "0.0.0.0:5000/catch_me" -o /dev/null -w "You got me!"
