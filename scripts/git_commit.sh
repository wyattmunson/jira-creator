#!/bin/bash

# $1    REPO_LOCATION       Absolute file path to git repo location
# $2    COMMIT_TIMESTAMP    UTC timestamp to make commit  

echo ".....START: Create and amend git commit....."
echo "...Using env vars..."
echo REPO_LOCATION $1
echo COMMIT_TIMESTAMP $2

cd $1
echo ...Moved to dir: $1 ...

echo "..Adding commits.."
git add .

echo "..Committing.."
git commit --quiet -m "generated commit message"
if [[ $? -eq "0" ]]; then echo "..Success.."; else echo "..Failed.."; fi

echo "..Amending commit.."
git commit --quiet --amend --date="$2" --no-edit
if [[ $? -eq "0" ]]; then echo "..Success.."; else echo "..Failed.."; fi

echo ".....END: Create and amend git commit....."