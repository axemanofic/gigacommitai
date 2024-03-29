import typer

from .config import Config


class AppContext(typer.Context):
    obj: Config


def config_callback(ctx: typer.Context):
    config = Config.create()
    ctx.obj = config.load()
