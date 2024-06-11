from web.app import create_app
from utils.job import start_worker

app = create_app()

if __name__ == '__main__':
    start_worker()  # Start the job worker
    app.run(port=5000)
