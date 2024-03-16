#1/usr/bin/env bash
if ! which nginx >/dev/null 2>&1; then
	echo "installed"
else
	echo "not installed"
fi
