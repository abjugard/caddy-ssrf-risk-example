#!/bin/bash

flask run &

exec caddy run --config /etc/caddy/Caddyfile --adapter caddyfile