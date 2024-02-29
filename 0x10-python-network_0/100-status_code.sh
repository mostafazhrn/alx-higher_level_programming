#!/bin/bash
# THis script shall send request and disp status code of respone
curl -s -o /dev/null -w "%{http_code}" "$1"
