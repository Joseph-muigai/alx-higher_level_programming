#!/bin/bash
#script that sends a DELETE request to the url passed as an argument and displays the responce
curl -sX DELETE "$1"
