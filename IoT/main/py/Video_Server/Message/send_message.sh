#!/bin/bash

# Function to get the formatted date
get_formatted_date() {
	date +%y%m%d%H%M
}

# Assign a date-based name to the folder
folder_name=$(get_formatted_date)

# Create a new folder
mkdir -p "$folder_name"

# Move data to the new folder
mv temp/* "$folder_name"

# Reduce file permissions to a safer level
chmod 600 I9E101T.pem

# Transfer files using scp command
scp -i I9E101T.pem -r "$folder_name" ubuntu@i9E101.p.ssafy.io:/home/ubuntu/message/

# Delete the folder
rm -r "$folder_name"
