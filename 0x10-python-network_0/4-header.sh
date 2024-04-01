#!/bin/bash
#Script to take in URL as argument,send GET request to URL,display body response
curl -s "$1" -H "X-School-User-Id: 98"
