#!/bin/bash
#Script to take in URL, sends POST request to passed URL,display body response
curl -s "$1" -X POST -d "email=test@gmail.com&subject=I will always be here for PLD"
