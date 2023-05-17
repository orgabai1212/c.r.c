#!/bin/bash

# # Check if there are any tags in the Git repository
# tag=$(git describe --tags --abbrev=0 2> /dev/null)

# if [ -z "$tag" ]
# then
#   # If there are no tags, set major to 0, minor to 0, and patch to 1
#   major=1
#   minor=0
#   patch=0
# else
#   # If there is a tag, extract the major, minor, and patch version numbers
#   major=$(echo "$tag" | awk -F. '{print $1}')
#   minor=$(echo "$tag" | awk -F. '{print $2}')
#   patch=$(echo "$tag" | awk -F. '{print $3}')
#   patch=$((patch + 1))
# fi

# version="${major}.${minor}.${patch}"
# echo $version

branch=$(git symbolic-ref --short HEAD)
tags=$(git tag)
tags_array=()
flag=0

IFS='/' read -ra branch_parts <<< "$branch"
version=${branch_parts[1]}
echo " general version $version"
major=$(echo "$version" | awk -F. '{print $1}')
minor=$(echo "$version" | awk -F. '{print $2}')
patch=$(echo "$version" | awk -F. '{print $3}')

if [[ -z $tags ]]; then
    # echo "no tags"
    git tag $version
    exit 0
else
  # echo "start else"
  for tag in $tags; do
    echo "try for"
    if [[ $tag == $version ]]; then
      flag=1
      for tag in $tags; do
        echo "second for"
        temp_major=$(echo "$tag" | awk -F. '{print $1}')
        temp_minor=$(echo "$tag" | awk -F. '{print $2}')
        if [[ $temp_major == $major && $temp_minor == $minor ]]; then
          tags_array+=("$tag")
          echo "add tag to array tag:$tag"
        fi
      done
    fi
  done
fi
if [[ $flag == 0 ]]; then
  # echo "no tag found with the same version"
  git tag $version
  exit 0
fi

# echo "part 3"
max_patch=$patch
# echo "max patch $max_patch"
max_patch_version=""
for tag in "${tags_array[@]}"; do
    # echo "therd for "
    # Extract patch number from version
    temp_patch=$(echo "$tag" | awk -F'.' '{print $3}')
    # echo "the tag patch $temp_patch"

    # Check if patch is greater than the current max_patch
    if [[ -z "$max_patch" || "$temp_patch" -ge "$max_patch" ]]; then
        max_patch="$temp_patch"
        # echo "max path $max_patch"
        max_patch_version="$tag"
        # echo "max patch version $max_patch_version"
    fi
done
max_patch_version_patch=$(echo "$max_patch_version" | awk -F. '{print $3}')
echo "max_patch_version_patch is $max_patch_version_patch"
max_patch_version_patch=$((max_patch_version_patch + 1))
new_version="${major}.${minor}.${max_patch_version_patch}"
echo "new version $new_version" 
git tag $new_version
#abcdg