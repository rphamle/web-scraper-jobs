#!/bin/bash

# This script builds the base worker image
cd ..
docker build --pull --rm -f build/worker-base/Dockerfile -t web-scraper-jobs/worker-base:latest .