#!/bin/bash

echo set configs

# cd ~/code/fake-python
cd $1
# git config --global credential.helper '!f() { sleep 1; echo 'username=$2 token=$3'; }; f'

echo "URL is" $2

# git remote set-url --push origin "$2"
git remote set-url origin "$2"

# ./scripts/git_cred.sh "/Users/wyatt/code/fake-python" "https://git.harness.io/MQGesbQCQ2WNqoJhvEsw1w/default/default_projectset configsts.git"

# "https://git.harness.io/MQGesbQCQ2WNqoJhvEsw1w/default/default_projectset configsts.git"

# "https://Wyatt Munson:pat.MQGesbQCQ2WNqoJhvEsw1w.665ec2233a4cba134c657a9d.X7JfC0vKdmbsK0fjeNmw@git.harness.io/MQGesbQCQ2WNqoJhvEsw1w/default/default_project/fake-commits.git"

# git remote set-url --push origin "https://Wyatt%20Munson:pat.MQGesbQCQ2WNqoJhvEsw1w.665ec2233a4cba134c657a9d.X7JfC0vKdmbsK0fjeNmw@git.harness.io/MQGesbQCQ2WNqoJhvEsw1w/default/default_project/fake-commits.git"
# git remote add origin "https://Wyatt%20Munson:pat.MQGesbQCQ2WNqoJhvEsw1w.665ec2233a4cba134c657a9d.X7JfC0vKdmbsK0fjeNmw@git.harness.io/MQGesbQCQ2WNqoJhvEsw1w/default/default_project/fake-commits.git"