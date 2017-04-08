#!/bin/bash

for file in `ls`
do
	if [ -d $file ] ; then
		echo $file
	fi
done
