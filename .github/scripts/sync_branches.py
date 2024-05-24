import subprocess

def run_command(command):
    result = subprocess.run(command, capture_output=True, text=True, check=True)
    return result.stdout.strip()

def get_branches(remote):
    branches = run_command(['git', 'ls-remote', '--heads', remote]).splitlines()
    return {line.split()[1].replace('refs/heads/', ''): line.split()[0] for line in branches}

# Fetch upstream and origin branches
upstream_branches = get_branches('upstream')
origin_branches = get_branches('origin')

# Check for new or updated branches
new_or_updated_branches = [
    branch for branch in upstream_branches
    if branch not in origin_branches or upstream_branches[branch] != origin_branches[branch]
]

updated = 'false'

# Sync new or updated branches to origin
if new_or_updated_branches:
    updated = 'true'
    for branch in new_or_updated_branches:
        print(f"Syncing branch: {branch}")
        run_command(['git', 'fetch', 'upstream', f'{branch}:{branch}'])
        run_command(['git', 'push', 'origin', branch])

# Set output variable
print(f"::set-output name=updated::{updated}")
