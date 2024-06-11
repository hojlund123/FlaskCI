import git

def clone_repo(repo_url, local_path):
    git.Repo.clone_from(repo_url, local_path)

def pull_latest_changes(local_path):
    repo = git.Repo(local_path)
    repo.remotes.origin.pull()
