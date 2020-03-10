#!/bin/bash

base_dir="/srv/www/backend/backend"
app_dir="${base_dir}"
app="backend"

cd "${app_dir}"
flower -A "${app}" --broker="sqs://"  --conf="/srv/www/bin/flowerconfig.py"