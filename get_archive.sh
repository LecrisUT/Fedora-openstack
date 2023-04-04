#!/bin/bash

spectool -g -s0 $1 >/dev/null 2>&1
tar_name=$(rpmspec --parse $1 | sed -En 's|^/usr/lib/rpm/rpmuncompress(.*)SOURCES/(.*)|\2|p')
echo "$tar_name"
