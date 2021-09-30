# project-scaffolds

This repo contains project-scaffolds to speed up development.
Download a subfolder (scaffold) from this repo to start a new project with some predefined structure and files.

## List of scaffolds

| scaffold | description |
| --- | --- | 
| simple-python-venv-project | A simple Python project based on python virtual environment |
| simple-python-conda-project | A simple Python project based on conda environment |
| simple-python-devontainer-project | A simple Python project based on vscode devcontainer |


## To start a new project based on project-scaffold
Example: Download simple-python-venv-project scaffold and start a new project named my-new-project
``` 
SCAFFOLD=simple-python-venv-project 
NEWPRJ=my-new-project
mkdir $NEWPRJ && curl -L https://github.com/d-xa/project-scaffolds/tarball/$SCAFFOLD | tar -xzv --strip-components=1 -C $NEWPRJ
```

## Alternative: use my helper script from https://github.com/d-xa/scripts

Example: Call script functions remotely
> scafffold.sh list

To list all available project scaffolds 
```
wget -O - https://raw.githubusercontent.com/d-xa/scripts/master/scaffold.sh | bash -s list
```

> scaffold.sh create

To create a new project based on a specified scaffold
```
wget -O - https://raw.githubusercontent.com/d-xa/scripts/master/scaffold.sh | bash -s create -s=simple-python-venv-project -n=my-new-project
```