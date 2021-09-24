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