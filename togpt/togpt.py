from pathlib import Path

from gitignore_parser import parse_gitignore


class TextBuilder:
    def __init__(self, directory: Path) -> None:
        self.directory = directory
        self.gitignore = parse_gitignore(directory / '.gitignore')

    def build_text(self, directory: Path, prefix: str = '') -> tuple[str, str]:
        '''
        Builds a tree structure of the given directory.
        '''
        tree = ''
        files = ''

        # Iterate over all files and subdirectories in the directory
        for item in sorted(directory.iterdir()):
            if item.name.startswith('.') or self.gitignore(item):
                continue
            if item.is_dir():
                # If the item is a directory, recursively build a tree for it
                tree += f'{prefix}└── {item.name}/\n'
                tree_, files_ = self.build_text(item, prefix + ' ' * 4)
                tree += tree_
                files += files_
            else:
                # If the item is a file, add it to the output
                tree += f'{prefix}└── {item.name}\n'
                files += get_file_contents(item)

        return tree, files


def get_file_contents(path: Path) -> str:
    '''
    Returns the contents of all Python files in the given directory.
    '''
    with path.open('r') as file:
        header = f'# Contents of {path.name}'
        return header + '\n```\n' + file.read() + '\n```\n\n'


def convert_project_folder(directory: Path) -> str:
    '''
    Converts a project folder into a format digestible by ChatGPT.
    '''
    text_builder = TextBuilder(directory)
    text = text_builder.build_text(directory)
    return f'# Project tree structure\n```\n{text[0]}```\n\n{text[1]}\n'
