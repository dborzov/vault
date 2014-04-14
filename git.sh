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

ssh-add -l # list ssh
chmod 600 file # to please their permission demands

#pulling remote branches
git branch -r # see remote branches
git fetch origin prod
git checkout prod

# gitconfig
[alias]
    lg  = log --graph --decorate
    llg = log --oneline --graph --decorate
    ll  = log --oneline

    dc = diff --cached
    st = status --short
    ci = commit
    rb = rebase
    br = branch
    co = checkout

ssh-add -K # to add keys to macos keychain
