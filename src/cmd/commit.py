import typer
from src.config.config import AppContext
from src.llm.model import GptModel

from src.git import get_diff

def commit(ctx: AppContext):
    diff = get_diff()
    model = GptModel(ctx.obj)
    typer.echo(model.get_commit_message(diff))
