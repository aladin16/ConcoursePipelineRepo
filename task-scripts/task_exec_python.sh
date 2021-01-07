#!/bin/sh

git clone aladin-repo aladin-repo-updated

cd aladin-repo
date > bumpme

git config --global user.email "nobody@concourse-ci.org"
git config --global user.name "Concourse"

git add .
git commit -m "Bumped date"