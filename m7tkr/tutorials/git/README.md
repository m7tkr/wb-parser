# Git Commands

## 1 getting started

* `git config --system` applies to `[path]/etc/gitconfig` file : system-wide
* `git config --global` applies to `$HOME/.gitconfig` or `$HOME/.config/git/config` : only to current user
* `git config --local` applies to `config` in current dir : only to current dir

Each lever overrides values in previous

* `git config --list --show-origin` : show origin of every set parameter
* `man git-config` : customizable options, check this url https://git-scm.com/docs/git-config
* `git help <verb>`, `git <verb> help` or `man git-<verb>` : for help
* `git <verb> -h` : get concise help

## 2 git basics

### 2.2 record changes to repo

* `git clone <url> <reponame>` : clone repo from remote w/ name you want
* `git init` : make repo to track file
* `git add <file>` : start file indexing
* Files are either tracked or untracked
* Tracked files further divided into: 
    * unmodified
    * modified
    * staged
* `git status`, `git status -s,` or `git status --short` : which file in which state
* `.gitgnore` : store files that need not to be staged
    * `!<file> : but stage this file
* `git diff` : see changed
    * `git diff --stage`, `git diff --cached` : diffs staged file w/ previous commit
    * `git difftool` : open diff GUI
* `git commit -m` : commit changed w/ msg
    * `git commit -a -m` : skip staging area (i.e. `git add .`)
* `git rm <file>` : rmvs file from staging area and then from your working dir (untracked) the file'll be gone w/ next commit
    * simple `rm <file>` keeps your file in unstaged area
    * `-f` : force removal of staged file
    * `git rm --cached <file>` : rm file from staged, but keeps in working tree
* `git mv <file-from> <file-to> : rename file in, includes 3 commands in it:
    * `mv <from> <to>`
    * `git rm <from>`
    * `git add <to>`

### 2.3 view commit history

* `git log` : recent commits 1st
* `git log -p -2`, `git log -patch -2` : shows diffs in last 2 commits
* `git --stat` : abbrev stats for each commit
* `git log --pretty=oneline`, `=short`, `=full`, `=fuller` : `--pretty` allows to define parameters
* `git log --pretty=format:"<specifiers>"` : `format` option allows to specify you your own parameters
    * check link https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History#pretty_format
* `git log --pretty=format:"<specifiers>" --graph` : useful when working w/ branches
* check link for `git log` common options https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History#log_options
* limiting options here https://git-scm.com/book/en/v2/Git-Basics-Viewing-the-Commit-History#limit_options

### 2.4 undo things

* `git commit --amend` : used for minor changed
    * if no change since last commit, changes only commit message
* `git reset HEAD <file>` : from staged to unstaged (still tracked)
    * git restore --staged <file>` : since Git 2.23.0
* `git checkout -- <file>` : reset all changes made back to last stage/commit
    * `gis restore <file>` : since Git 2.23.0

### 2.5 remotes

* `git remote` : see configured remotes
* `git remote -v` : show URL of remotes
    * git clone implicitly adds `origin` remote for you
* `git remote add <name> <url>` : add new remote
* `git fetch <remote-name>` : fetches remote to you local repo, but no merge
* `git pull` : fetch 1st then merge w/ you local
    * `git config --global pull.rebase "false"` : no rebase, merge instead
    * `git config --global pull.rebase "true"` : no merge, rebase instead
* `git push origin master` : push changes to remote if no upstream commits from others
* `git remote show <remote>` : inspect remote deeper
    * `git remote show` : show list of remotes
* `git remote rename <remote>` : rename remote
* `git remote remove <remote>` : remove remote

### 2.6 tagging (to be added)

### 2.7 aliases

* git config --global alias.<alias_name> <command> : set alias
    * `git config --global alias.ci checkout` : type `git ci` to get `git checkout`
    * `git config --global alias.unstage 'reset HEAD --'`
        * type `git unstage <file>` to get `git reset HEAD -- <file>`
* `!<external_cmd_name>` : use `!` for commands outside git

## 3 branches

### 3.1 basics

* `git branch <name>` : create new branch
* `git log --oneline --decorate` : show pointer and pointees
* `git checkout <branch>` : switch to existing branch
* `git log --all` : show every branch
    * without `--all` shows logs only under current branch
* `git log --oneline --decorate --graph --all` : shows divergent history
* `git checkout -b <branch>` : 1st create new branch, 2nd switch there
* `git swtich` : Git 2.23 onwards instead of `git checkout` to:
    * `git switch <branch>` : switch to existing branch
    * `git switch -c <branch>` : create and switch, `--create` full flag name
    * `git switch -` : return to previously checked branch
* `git merge <branch> : merge <branch> into <you_current_branch>
* `git branch -d <branch> : delete branch
* `git mergetool` : runs graphical merge tool
    * don't forger to run `git add <file>` after resolution to stage file
* `git branch` : shows all the branches
* `git branch -v` : see last commit on each branch
* `git branch --merged` : show merged branches, safe to dlt
* `git branch --no-merged` : show unmerged branches, not safe to dlt
* `git branch --no-merged master` : shows what is not merged into master branch, no chekcout req
* `git branch --move <old_branch_name> <new_branch name>` : change branch name
* `git push --set-upstream origin <new-branch-name>` : push changed branch name into remote
    * `git push origin --delete old-branch-name` : remove old branch from remote
* `git branch --move <master> <main>` : rename master branch (VERY CAREFULLY)
    * dont forget to run remove

### 3.5 remote branches

* `git ls-remote <remote>` : list of remote references
* `git remote show <remote>` : inspect remote
* `git push <remote> <branch>` : push branch into remote
    * `git push origin <branch-name-local>:<branch-name-remote> : says "take my local branch and make it remote"
* `git config --global credential.helper cache` : set credential cache to not enter psswrd w/ each push
* `git merge <remote>/<branch>` : ran after fetch command to get local copies of FILES
* `git chekcout -b <branch-local> <remote>/<branch-remote>` : gives you LOCAL <branch-local> based on <branch-remote>
    * `git checkout --track <remote>/<branch-remote>` : same as above
    * `git chekcout <remote>` : same as above, but works if the branch name you’re trying to checkout:
        * doesn't exist
        * exactly matches a name on only one remote
* `git branch -u <origin>/<remote>` : sets existing local branch as a remote, or changes upstream branch `--set-upstream-to`
* `git branch -vv` : shows tracking branches
* `git fetch --all` : fetches changes for all tracking branches
* `git push origin --delete serverfix` : deletes tracking branch
