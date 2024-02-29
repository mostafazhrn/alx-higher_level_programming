#!/bin/bash
# This script shall make req to srvr & mk the server respond with sentence
curl -o /dev/null -s -w "You got me!" 0.0.0.0:5000/catch_me
