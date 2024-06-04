#!/bin/bash

# ARGS
# REPO_LOCATION  $1  Username of git user
# CODE_USERNAME  $2
# CODE_PAT

echo "...Setting git config file..."

if [[ -z "$1" ]]; then echo "FATAL: Missing REPO_LOCATION" && exit 1; fi
if [[ -z "$2" ]]; then echo "FATAL: Missing CODE_USERNAME" && exit 1; fi

cd $1

echo "$2:$3" > ./my-creds
git config credential.helper "store --file ./my-creds"


# git config credential.helper '!fzy [ -z "{password}" ] && echo "username:{token}"'
# git config credential.helper '!fzy [ -z "{password}" ] && echo "$CODE_USERNAME:{token}"'
