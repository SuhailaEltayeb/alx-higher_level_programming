#!/bin/bash
#Script to take URL,send request to that URL,display response body size
curl -sI "$1" | grep -i Content-Length | cut -d " " -f 2
