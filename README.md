# one-page-a-day

# Setup project
This project has been setup on MacOS with VSCode

## Install MacTex
Install MacTax from http://www.tug.org/mactex/

## Setup Python env
```
sudo pip install -r requirements.txt
```
## Setup VS Code
Install extensions:
* LaText Workshop
* Python

Use xelatex as the default latex compiler for Chinese support 
```
"latex-workshop.latex.toolchain": [
        {
            "command": "xelatex",
            "args": [
                "-synctex=1",
                "-interaction=nonstopmode",
                "-file-line-error",
                "-pdf",
                "%DOC%"
            ]
        }
    ],
```

## Code snippets
.vscode/python.json has some snippets for adding section/exercie.

Copy to VS Code's snippet for Python. 
```
Code -> Preferences -> User Snippets
Choose Python
``` 
