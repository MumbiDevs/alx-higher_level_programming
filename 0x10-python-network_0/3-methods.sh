#!/bin/bash

if [ $# -ne 1 ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

URL=$1

# Send an OPTIONS request and extract the Allow header
HTTP_METHODS=$(curl -sI -X OPTIONS "$URL" | grep 'Allow:' | cut -d ' ' -f 2-)

if [ -z "$HTTP_METHODS" ]; then
    echo "No Allow header found or server does not accept any methods."
else
    echo $HTTP_METHODS
fi
