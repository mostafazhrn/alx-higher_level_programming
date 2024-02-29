#!/bin/bash
# This script shall take URL and display all methods acc
curl -sI "$1" | grep "Allow" | cut -d ' ' -f2-
