import typer

from src.config.config import AppContext


app = typer.Typer()


@app.command("get")
def config_get(ctx: AppContext, key: str):
    typer.echo(ctx.obj.get(key))


@app.command("set")
def config_set(ctx: AppContext, key: str, value: str):
    ctx.obj.set(key, value)
    ctx.obj.update()


@app.command("list")
def config_list(key: str):
    return key
