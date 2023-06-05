#!/bin/bash

uvicorn web_socket:app --reload --host 0.0.0.0 --port ${WEBSOCKET_PORT}
