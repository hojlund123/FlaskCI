from web.app import create_app
from utils.job import start_worker
import subprocess
import os
import time

# Set the FLASK_APP environment variable
os.environ['FLASK_APP'] = 'web.app:create_app()'

app = create_app()

if __name__ == '__main__':
    start_worker()  # Start the job worker

    # Run the Flask app in a subprocess
    app_process = subprocess.Popen(["flask", "run", "--port", "5000"])

    # Expose the Flask app using Localtunnel
    while True:
        try:
            result = subprocess.run(["lt", "--port", "5000", "--subdomain", "larslars1337"], check=True)
            break
        except subprocess.CalledProcessError as e:
            print(f"Localtunnel connection failed: {e}")
            print("Retrying in 5 seconds...")
            time.sleep(5)
        except KeyboardInterrupt:
            app_process.terminate()
            break
