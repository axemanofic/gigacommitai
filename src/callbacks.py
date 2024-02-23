import typer

from .config.config import Config


def config_callback(ctx: typer.Context):
    config = Config.create()
    ctx.obj = config.load()
