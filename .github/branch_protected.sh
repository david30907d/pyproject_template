#!/bin/bash
protected_branch='master'
protected_branch2='prod'
current_branch=$(git symbolic-ref HEAD | sed -e 's,.*/\(.*\),\1,')
if [ $protected_branch = $current_branch ]
then
	echo "Hey dipshit, you can't commit to master."
	exit 1
elif [ $protected_branch2 = $current_branch ]
then
	echo "Hey dipshit, you can't commit to master."
	exit 1
else
	exit 0
fi