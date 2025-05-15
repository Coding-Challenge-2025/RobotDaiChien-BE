#!/bin/bash
pushd Simulator
if [[ -n "$4" && -n "$5" ]]; then
    python main.py "$1" -p "$2" "$3" "$4" "$5"
else
    python main.py "$1" -p "$2" "$3"
fi
popd