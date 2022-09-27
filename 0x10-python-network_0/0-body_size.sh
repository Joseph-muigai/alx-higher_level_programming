#!/bin/bash
#display he size of the body of the response in bytes
curl -sI "$1" | grep 'Content-Length:' | cut -d' ' -f2