import typer

from .cmd import config, commit
from .callbacks import config_callback


app = typer.Typer(
    callback=config_callback,
    invoke_without_command=True,
)

app.add_typer(config.app, name="config")

app.command()(commit.commit)
