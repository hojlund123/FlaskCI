from utils.build import run_command

def deploy_project(local_path):
    return run_command('make deploy', local_path)
