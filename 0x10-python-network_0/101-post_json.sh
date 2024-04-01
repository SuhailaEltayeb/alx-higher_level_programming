#!/bin/bash
#Script to send  JSON POST request to URL passed as 1st argument, display body response.
curl -s "$1" -d "@$2" -X POST -H "Content-Type: application/json"
