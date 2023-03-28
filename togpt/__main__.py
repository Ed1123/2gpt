from pathlib import Path
from togpt.togpt import convert_project_folder
import typer


app = typer.Typer()


@app.command()
def main(directory: Path = typer.Argument(..., help='The directory to convert.')):
    '''
    Converts a project folder into a format digestible by ChatGPT.
    '''
    if not Path(directory).is_dir():
        typer.echo(f'Error: {directory} is not a valid directory.')
        raise typer.Abort()

    output = convert_project_folder(directory)
    typer.echo(output)


if __name__ == '__main__':
    app()
