from web.app import create_app
from utils.job import start_worker
import subprocess
import os
import time

# Set the FLASK_APP environment variable
os.environ['FLASK_APP'] = 'web.app:create_app'

app = create_app()

if __name__ == '__main__':
    start_worker()  # Start the job worker

    # Run the Flask app in a subprocess
    app_process = subprocess.Popen(["flask", "run", "--host", "0.0.0.0", "--port", "5000"])

    # Expose the Flask app using Localtunnel
    try:
        result = subprocess.run(["lt", "--port", "5000", "--subdomain", "larslars1337"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Localtunnel connection failed: {e}")
        app_process.terminate()
    except KeyboardInterrupt:
        app_process.terminate()
