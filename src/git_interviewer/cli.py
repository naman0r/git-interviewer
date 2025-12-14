import typer
from rich.console import Console # allows us to create a console instance
from rich.panel import Panel # allows us to create a panel instance
from rich.prompt import Prompt # allows us to create a prompt instance
import sys
from .config import get_api_key, GIT_INTERVIEWER_MODE
from git_interviewer.git_utils import get_staged_diff, install_hook
from .llm import generate_question



app = typer.Typer() # initialization of core CLI app, returns a callable object
console = Console()

@app.command() # decorator to register the function as a CLI command
def init(): 
    """ install the git interviewer pre commit hook """
    install_hook()
    
@app.command()
def interview(): 
    """ Analyse staged changes and interview the developer """
    
    # 1. CHECK API KEY FIRST
    api_key = get_api_key()
    if not api_key: 
        console.print("[yellow]⚠️  Git Interviewer skipped: GEMINI_API_KEY not found.[/yellow]")
        console.print("   To enable, run: [bold]export GEMINI_API_KEY='your_key'[/bold]")
        
        # exit code 0 so that the commit proceeds even without the interview. s
        raise typer.Exit(code=0)
    
    
    # 2. get diff
    diff = get_staged_diff()
    
    if not diff: 
        # no staged changes or empty diff
        # git handles this naturally i think
        return
    
    console.print(f"[bold blue] 🎤 Git Interviewer ({GIT_INTERVIEWER_MODE} mode) [/bold blue]")
    console.print(f"[bold green] Analyzing changes... [/bold green]", style="dim")
    
    #pass # TODO IMPLEMENTATIN AFTER FIGUREING OUT HOW TF TO ACTUALLY GET THE API KEYS
    try: 
        question = generate_question(diff)
        
    except Exception as e: 
        console.print(f"[red] Error connecting to AI:[/red] {e}")
        # fail open
        raise typer.Exit(code=0)
    
    console.print(Panel(question, title="Interviewer", border_style="blue"))
    
    answer = Prompt.ask(f"[bold] your answer [/bold]")
    
    # validation: 
    if len(answer.split()) < 3: 
        console.print("[bold red]❌ That answer is too short! Commit rejected.[/bold red]")
        console.print("Please provide a meaningful explanation.")
        # exit code 1, do not allow commit. 
        raise typer.Exit(code=1)
    
    # want to implement back and forth with AI until AI likes all the answers. for now, just 
    # a question with an answer is good enough, no need to actually look at the answer
    console.print("[bold green]Good answer, commit allowed[/bold green]")
    raise typer.Exit(code=0)

        


