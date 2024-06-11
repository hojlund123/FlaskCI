from web.app import create_app
from utils.job import start_worker
import subprocess

app = create_app()

if __name__ == '__main__':
    start_worker()  # Start the job worker

    # Run the Flask app
    app_process = subprocess.Popen(["python", "-m", "flask", "run", "--port", "5000"])

    # Expose the Flask app using Localtunnel
    try:
        subprocess.run(["lt", "--port", "5000", "--subdomain", "larslars1337"])
    except KeyboardInterrupt:
        app_process.terminate()
