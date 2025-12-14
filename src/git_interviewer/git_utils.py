# git utilities file.....
import subprocess
import os
import sys

def get_staged_diff() -> str: 
    """
    
    """
    try: 
        # run git diff --cached
        result = subprocess.run(["git", "diff", "--cached"], 
                                capture_output=True, text=True, check=True)
        return result.stdout.strip()
    
    except subprocess.CalledProcessError as e: 
        print(f"Error getting staged diff: {e}", file=sys.stderr)
        return None
    
    
def install_hook() -> bool: 
    """ Installs pre commit hook """
    hook_path = ".git/hooks/pre-commit"
    
    if not os.path.exists(".git"): 
        print("This is not a git repo yet! ")
        return False
    
     hook_script = """#!/bin/sh
# Git Interviewer Hook
exec git-interviewer interview
"""
    with open(hook_path, "w") as f:
        f.write(hook_script)
        
    os.chmod(hook_path, 0o755) # owner rwx, groups read and execute, others read and execute
    print(f"Pre-commit hook installed at {hook_path}")
    return True