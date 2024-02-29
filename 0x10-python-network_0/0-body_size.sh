#!/bin/bash
# This script shall take URL and send request and disp size of body

curl -s "$1" | wc -c
