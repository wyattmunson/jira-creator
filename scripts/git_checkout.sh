#!/bin/bash

# ARGUMENTS
# $1    REPO_LOCATION
# $2    BRANCH_NAME

echo ".....Git checkout......"

cd $1
echo "Moved to dir:" $1

# check for branch
START_BRANCH=$(git branch)

echo "Starting git branch..."
echo $START_BRANCH

if [[ "$START_BRANCH" == "* main" ]]; then
    echo "On main branch. Creating new branch $2..."
    git checkout -b $2
else
    echo "Branch exists"
fi

CHECKOUT_STATUS=$?

echo "Git branch status after..."
git branch