# This script builds the base worker image
cd ..
docker build --pull --rm -f build/Dockerfile -t web-scraper-jobs/worker-base:latest .