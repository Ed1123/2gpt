# Project to GPT

A simple terminal app that converts a given project folder into text feedable to ChatGPT (or any other LLM).

## Features

- Outputs the file tree of the project follow by the content of each file
- Ignores dot files/folders (e.g. .git folder)
- Ignores files/folders in .gitignore (e.g. venv, build files, etc.)

## Installation

```Console
git clone https://github.com/Ed1123/2gpt.git
cd 2gpt
pip install .
```

## Usage

```Console
2gpt path_to_project
```

Inside your project directory:

```Console
2gpt .
```

## Motivation

I wanted to get feedback for a project I have and I couldn't find anything similar online so I build it.

I may consider uploading it to PyPi.
