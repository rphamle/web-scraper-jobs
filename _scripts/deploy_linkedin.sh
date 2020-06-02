#!/bin/bash

# This script deploys the base worker image, and copies the linkedin scraping application script
cd ..
docker run --rm -d -t --name worker-linkedin web-scraper-jobs/worker-base:latest
docker cp app/linkedin/scrape.py worker-linkedin:/app