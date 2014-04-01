git add . -A # key for deleting deleted files from index
git push origin +master # --force like, overpowers HEAD being mismatched
git reflog # all local commits HEAD was ever referring to
git checkout origin/master -- filename # rollback a file
git submodule --update # sync the submodule git repo manually


# setting to use ssl keys for authentication
git config --local --edit
# url = https://github.com/sowingocorp/api --> url = git@github.com:sowingocorp/api

# remove cashed file
git rm --cached file.txt

# show list of affected files for a commit
git diff-tree --no-commit-id --name-only -r bd61ad98

# go back a commit
git reset --hard HEAD~


