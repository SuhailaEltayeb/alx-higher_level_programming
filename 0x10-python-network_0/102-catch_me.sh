#!/bin/bash
#Script to make request to 0.0.0.0:5000/catch_me, cause server to respond with message, in body response.
curl -sL 0.0.0.0:5000/catch_me_3 -X PUT -d "user_id=98" -H "Origin:School"
