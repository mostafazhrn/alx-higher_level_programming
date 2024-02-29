#!/bin/bash
# THis script shall take URL and send POST and disp respone
curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1"
