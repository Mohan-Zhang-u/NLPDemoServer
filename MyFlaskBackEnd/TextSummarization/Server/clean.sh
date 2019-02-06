#!/usr/bin/env bash

if (( $# == 0 ))
then
    echo "clean the To_Be_Clean dir"
    rm -rf ../To_Be_Clean
else
    for var in "$@"
    do
        rm -rf ../To_Be_Clean/$var
    done
fi