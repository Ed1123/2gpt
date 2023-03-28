from pathlib import Path


def build_tree(directory: Path, prefix: str = '') -> str:
    '''
    Builds a tree structure of the given directory.
    '''
    output = ''
    path = Path(directory)

    # Iterate over all files and subdirectories in the directory
    for item in sorted(path.iterdir()):
        if item.is_dir():
            # If the item is a directory, recursively build a tree for it
            output += f'{prefix}└── {item.name}/\n'
            output += build_tree(item, prefix + ' ' * 4)
        else:
            # If the item is a file, add it to the output
            output += f'{prefix}└── {item.name}\n'

    return output


def get_file_contents(directory: Path) -> str:
    '''
    Returns the contents of all Python files in the given directory.
    '''
    output = ''

    # Iterate over all files in the directory
    for item in sorted(directory.iterdir()):
        if item.is_file() and item.suffix == '.py':
            # If the item is a Python file, add its contents to the output
            with item.open('r') as file:
                output += file.read() + '\n\n'

    return output


def convert_project_folder(directory: Path) -> str:
    '''
    Converts a project folder into a format digestible by ChatGPT.
    '''
    tree = build_tree(directory, 'asfasfd')
    contents = get_file_contents(directory)

    return f'{tree}\n\n{contents}'
