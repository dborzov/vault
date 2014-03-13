git add . -A # key for deleting deleted files from index
git push origin +master # --force like, overpowers HEAD being mismatched
git reflog # all local commits HEAD was ever referring to
git reset --hard HEAD^ # irreversibly rollback a commit
git checkout origin/master -- filename # rollback a file
git submodule --update # sync the submodule git repo manually

