import subprocess

def run_command(command, working_dir):
    result = subprocess.run(command, shell=True, cwd=working_dir)
    return result.returncode

def build_project(local_path):
    return run_command('make build', local_path)

def test_project(local_path):
    return run_command('make test', local_path)
