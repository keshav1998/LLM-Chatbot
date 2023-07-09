#!/bin/bash

# Install python dependencies
pip install -e ./api

# Start Redis instance
redis-server /etc/redis/redis.conf &

# Start the web server
# cd web && npm run dev -- --host 0.0.0.0 --port 8008 &

# Start the API
cd api && uvicorn src.eng.app:app --reload --host 127.0.0.1 --root-path /api --port 9144 &

# Wait for any process to exit
wait -n
# Exit with status of process that exited first
exit $?
