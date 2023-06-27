#!/bin/bash
# Bash script sends DELETE request to URL as 1st arg & displays body response
curl -s -X DELETE "$1"
