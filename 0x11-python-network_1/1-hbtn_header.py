#!/usr/bin/python3
"""
a Python script that takes in a URL, sends a request to the URL and displays the value of
the X-Request-Id variable found in the header of the response.
"""
import sys
from urllib import response
import urllib.request


if __name__ == "__main__":
     url = sys.argv[1]

     requestData = urllib.request.Request(url)
     with urllib.request.urlopen(requestData) as responseData:
         print(dict(responseData.headers).get("X-Request-Id"))
