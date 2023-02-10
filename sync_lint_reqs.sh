#!/usr/bin/env bash

blackv=$(cat .pre-commit-config.yaml | shyaml get-value repos.0.rev | xargs)
isortv=$(cat .pre-commit-config.yaml | shyaml get-value repos.1.rev | xargs)
flk8v=$(cat .pre-commit-config.yaml | shyaml get-value repos.2.rev | xargs)

echo "pre-commit" > tests/lint_requirements.txt
echo "black==$blackv" >> tests/lint_requirements.txt
echo "isort==$isortv" >> tests/lint_requirements.txt
echo "flake8==$flk8v" >> tests/lint_requirements.txt
