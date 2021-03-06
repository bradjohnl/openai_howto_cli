#!/usr/bin/env python3

import os
import openai
import sys

openai.api_key = os.environ.get('OPENAI_API_KEY')

# Take the request as a command line parameter and return the answer
request = sys.argv[1]


print(openai.Completion.create(
  engine="text-davinci-002",
  prompt="Convert this text to a linux shell command.\n\nExample: Show all filesystems usage, space and mount point in human format\nOutput: df -h\n\nExample: Check the size of the pCloudDrive folder every 3 seconds\nOutput: while true; do du -sh pCloudDrive; sleep 1s; clear; done;\n\nExample: Find the smallest file in a directory and in all its subdirectories\nOutput: find . -type f -exec du -sh {} + | sort -n\nExample: "+request+"\nOutput:",
  temperature=0,
  max_tokens=1000,
  top_p=1,
  frequency_penalty=0,
  presence_penalty=0
).choices[0].text)