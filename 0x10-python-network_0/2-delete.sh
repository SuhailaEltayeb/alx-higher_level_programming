#!/bin/bash
#Script to send DELETE request to URL passed as 1st arg display body response
curl -s "$1" -X DELETE
