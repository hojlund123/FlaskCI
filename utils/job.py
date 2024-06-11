from queue import Queue
import threading
from utils.build import build_project, test_project
from utils.deploy import deploy_project
from utils.notify import send_notification
from config import REPO_LOCAL_PATH, WEBHOOK_URL

job_queue = Queue()

def process_job(job):
    repo_url = job['repo_url']
    local_path = REPO_LOCAL_PATH
    
    clone_repo(repo_url, local_path)
    if pull_latest_changes(local_path) == 0:
        if build_project(local_path) == 0:
            if test_project(local_path) == 0:
                deploy_project(local_path)
                send_notification('Deployment succeeded', WEBHOOK_URL)
            else:
                send_notification('Tests failed', WEBHOOK_URL)
        else:
            send_notification('Build failed', WEBHOOK_URL)
    else:
        send_notification('Pull failed', WEBHOOK_URL)

def worker():
    while True:
        job = job_queue.get()
        if job is None:
            break
        process_job(job)
        job_queue.task_done()

def start_worker():
    thread = threading.Thread(target=worker)
    thread.start()

def add_job(job):
    job_queue.put(job)
