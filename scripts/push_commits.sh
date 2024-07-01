#!/bin/bash

# REPO_LOCATION     $1      Absolute file path to git repo location
# BRANCH_NAME       $2      Branch name

echo ".....START: Push commits......"

cd $1 
echo ...Moved to dir: $1 ...

git push -u origin $2

# URL="https://git.harness.io/MQGesbQCQ2WNqoJhvEsw1w/default/default_project/fake-commits.git"

# git remote set-url origin https://USERNAME:PAT@github.com/user/repo.git

# git push -u origin main


