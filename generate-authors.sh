#!/bin/bash
set -e

{
	cat <<-'EOH'
	# This file lists all individuals having contributed content to the repository.
	# For how it is generated, see [hack](https://github.com/moby/moby/blob/master/hack/generate-authors.sh)
	EOH
	echo
	git log --format='%aN <%aE>' | sort -uf
} > AUTHORS

