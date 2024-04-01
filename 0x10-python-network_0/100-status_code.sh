#!/bin/bash
#Script to send request to URL passed as argument,display only status code response
curl -s -L -X HEAD -w "%{http_code}" "$1"
