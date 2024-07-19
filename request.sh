#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 <user_content>"
    exit 1
fi

USER_CONTENT=$1

RESPONSE=$(curl -s -X POST "http://localhost:8000/chat/completions" \
     -H "Content-Type: application/json" \
     -d '{
       "model": "gemma-2b-oasst2-01",
       "messages": [
         {"role": "human", "content": "'"$USER_CONTENT"'"}
       ]
     }')

echo "$RESPONSE" | jq
