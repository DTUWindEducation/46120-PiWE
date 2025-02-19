import subprocess
import sys

def run_command(command):
    """Runs a shell command and returns the output, error, and exit code."""
    try:
        result = subprocess.run(command, shell=True, text=True, capture_output=True)
        if result.returncode != 0:
            print(f"Error: {result.stderr.strip()}")
            sys.exit(result.returncode)
        return result.stdout.strip()
    except Exception as e:
        print(f"Unexpected error: {e}")
        sys.exit(1)

def main():
    print("Syncing fork with upstream...")
    run_command("git pull upstream main")

    print(f"Pushing merged changes to origin/main...")
    run_command(f"git push origin main")

    print("Sync complete! Your fork is now up to date with the upstream repository.")

"""
    # Check if inside a Git repository
    print("Checking if this is a Git repository...")
    run_command("git rev-parse --is-inside-work-tree")

    # Fetch upstream changes
    print("Fetching updates from upstream...")
    run_command("git fetch upstream")

    # Get the current branch
    print("Getting current branch...")
    current_branch = run_command("git branch --show-current")
    print(f"Current branch: {current_branch}")

    # Merge upstream changes
    print(f"Merging upstream/{current_branch} into {current_branch}...")
    run_command(f"git merge upstream/{current_branch}")

    # Push to fork
    print(f"Pushing merged changes to origin/{current_branch}...")
    run_command(f"git push origin {current_branch}")

    print("Sync complete! Your fork is now up to date with the upstream repository.")
"""



if __name__ == "__main__":
    main()
