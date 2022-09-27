#!/bin/bash
#display he size of the body of the response in bytes
curl -sI "$1" | awk '/Content-Length/{print $2}'