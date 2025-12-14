import typer
from rich.console import Console # allows us to create a console instance
from rich.panel import Panel # allows us to create a panel instance
from rich.prompt import Prompt # allows us to create a prompt instance
import sys

from git_interviewer.git_utils import get_staged_diff, install_hook


app = typer.Typer()
console = Console()

@app.command()
def init(): 
    """ install the git interviewer pre commit hook """
    install_hook()
    
@app.command()
def interview(): 
    """ Analyse staged changes and interview the developer """
    diff = get_staged_diff()
    
    if not diff: 
        # no staged changes or empty diff
        # git handles this naturally i think
        return
    
    console.print(f"[bold blue] 🎤 Git Interviewer ({GIT_INTERVIEWER_MODE} mode) [/bold blue]")
    console.print(f"[bold green] Analyzing changes... [/bold green]", style="dim")
    
    pass # TODO IMPLEMENTATIN AFTER FIGUREING OUT HOW TF TO ACTUALLY GET THE API KEYS
