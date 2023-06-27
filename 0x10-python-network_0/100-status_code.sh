#!/bin/bash
# Bash script sends request to URL as arg & displays status code of response
curl -s -o /dev/null -w "%{http_code}" "$1"
