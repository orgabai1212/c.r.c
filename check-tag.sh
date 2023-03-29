#!/bin/bash

# Check if there are any tags in the Git repository
tag=$(git describe --tags --abbrev=0 2> /dev/null)

if [ -z "$tag" ]
then
  # If there are no tags, set major to 0, minor to 0, and patch to 1
  major=0
  minor=0
  patch=1
else
  # If there is a tag, extract the major, minor, and patch version numbers
  major=$(echo "$tag" | awk -F. '{print $1}')
  minor=$(echo "$tag" | awk -F. '{print $2}')
  patch=$(echo "$tag" | awk -F. '{print $3}')
fi

version="${major}.${minor}.${patch}"
echo $version