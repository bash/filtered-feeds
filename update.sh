#!/usr/bin/env bash

set -euo pipefail

if [[ -z "${FEEDS_OUTPUT_DIR:-}" ]]
then
    echo "error: FEEDS_OUTPUT_DIR is not set"
    exit 1
fi

mkdir -p -- "$FEEDS_OUTPUT_DIR"
curl --fail https://github.blog/changelog/feed/ \
	| uv run github-changelog/filter.py \
	> "$FEEDS_OUTPUT_DIR/github-changelog.xml"
