import typer
import rich

from ..callbacks import AppContext


app = typer.Typer()


@app.command("get")
def config_get(ctx: AppContext, key: str):
    typer.echo(ctx.obj.get(key))


@app.command("set")
def config_set(ctx: AppContext, key: str, value: str):
    ctx.obj.set(key, value)


@app.command("show")
def config_show(ctx: AppContext):
    config = ctx.obj.load()
    rich.print(config.config)
