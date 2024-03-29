from typing import Optional

import typer

from rich.progress import Progress, SpinnerColumn, TextColumn

from ..callbacks import AppContext
from ..git import Commit


def commit(
    ctx: AppContext,
    dry_run: Optional[bool] = False,
    is_ask: Optional[bool] = True,
):
    typer.secho("Welcome to Gigacommit!", fg=typer.colors.GREEN, bold=True)

    commit = Commit(config=ctx.obj, dry_run=dry_run)

    with Progress(
        SpinnerColumn(),
        TextColumn("[progress.description]{task.description}"),
        transient=True,
    ) as progress:
        progress.add_task(description="Generating commit message...", total=None)
        commit.generate_commit_message()

    commit_message = commit.get_commit_message()

    staged_files = commit.get_staged_files()
    typer.echo(f"Staged files:\n{staged_files}")
    typer.echo(f"Commit message: {commit_message}")

    is_accept = typer.confirm("Accept commit?", default=True)

    if is_accept:
        stdout = commit.create_commit(commit_message)
        typer.echo(f"\n{stdout}")
