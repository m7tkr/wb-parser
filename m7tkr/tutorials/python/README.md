# python cheatsheet

## python bash

## virtualenv

> intended to separate packaged, version of python
> don't store your project data files here

* `virtualenv <project-name>` : runs virtenv in current dir
* `source <project-name>/bin/activate` : activate virtenv
* `deactivate` : get out of virtenv
* `rm -rf <project-name>/` : remove virtenv
* `virtualenv -p <python-path> <project-name>` : make virtenv to use specific version of python

## python pip

* `pip3 help`, `pip help <command>` : get help
* `pip search <package-name>` : search in pip servers
* `pip install <package-name>` : install locally
* `pip list` : list installed packages
* `pip uninstall <package>` : unistall package
* `pip list -o`, `pip list --outdated` : list outdated packages
* `pip install -U <package>` : upgrade packaged
* `pip freeze > req.txt` : outputs all installed packages w/ version numbers into req.txt file
* `pip install -r req.txt` : install packages listed in req.txt file
> check how to upgrade all the packages at once
