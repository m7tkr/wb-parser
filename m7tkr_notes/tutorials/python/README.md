# python cheatsheet

## python bash
* `python -m <package> --version` : shows <package> version

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
<<<<<<< HEAD
=======

## pipenv

> one tool for both pip and virtualenv

* `pipenv install <package>` : creates virtenv and installs <package>
* `pipenv shell` : run virtenv
* `exit` : exit virtenv, not `deactivate`
* `pipenv run <command>` : run command inside virtenv w/out `pipenv shell`
* `pipenv run python <script>` : run script inside virtenv w/out starting it
* `pipenv install -r <path-to-req.txt>` : install packages from req.txt
* `pipenv lock -r` : show dependencies will be added to req.txt
* `pipenv install <package> --dev` : install package into dev env only, not production
* `pipenv uninstall <package>` : uninstall package
* `pipenv --python 3.6` : recreate env w/ python@3.6
* `pipenv --rm` : removes virenv you'r currently in
* `pipenv install` : updates from pipfile and pipfile.lock, if no env, then creates one
* `pipenv --venv` : gives path to you venv
* `pipenv check` : displays safety issues in reqs
* `pipenv graph` : shows packages and dependencies for them
* `pipenv lock` : create / update pipfile.lock w/ current dependencies
* `pipenv install --ignore-pipfile` : creates env w/ what in pipfile.lock, not w/ default pipfile
* `.env` file : keeps venv specific variables in it, accessible w/ `os.environ['<var-name>']`

> `.env` is supposed to be in .gitignore

## django

* `django-admin startproject <project-name>` : start new project
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a05e9fd (django models)
* `python manage.py runserver` : run server of created app
* `Ctrl-C` : stop server
* `python manage.py startapp <name>` : create new app
<<<<<<< HEAD
>>>>>>> 2b9a8bc (django tutorials started)
=======
* `python manage.py makemigrations` : detects db changes, and prepares django to apply them
* `python manage.py migrate` : apply db changes into django
* `python manage.py createsuperuser` : creates admin page credentials
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
=======
>>>>>>> a05e9fd (django models)
>>>>>>> 12d6ebe (tut: admin page setup completed)
=======
* `python manage.py sqlmigrate <app-name> <migration-no>` : shows sql code that will be run
* `python manage.py shell` : runs python shell that allows to work w/ django objects

>>>>>>> ea31f01 (django models tut)
<<<<<<< HEAD
=======
<<<<<<< HEAD
>>>>>>> 12d6ebe (tut: admin page setup completed)
>>>>>>> 3e84eca (admin page setup completed)
=======
* `python manage.py runserver` : run server
* `Ctrl-C` : stop server
* `python manage.py startapp <name>` : create new app
>>>>>>> 2b9a8bc (django tutorials started)
>>>>>>> 6d69347 (django tutorials started)
>>>>>>> e972cd4 (django tutorials)
=======
>>>>>>> a05e9fd (django models)
