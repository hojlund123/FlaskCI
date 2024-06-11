from utils.job import start_worker
import subprocess
import os
import time

# Set the FLASK_APP environment variable
os.environ['FLASK_APP'] = 'web.app:create_app'

def start_flask():
    # Change the working directory to where Flask can find the app
    os.chdir(os.path.dirname(os.path.abspath(__file__)))
    # Run the Flask app in a subprocess
    app_process = subprocess.Popen(["flask", "run", "--host", "0.0.0.0", "--port", "5000"])
    return app_process

if __name__ == '__main__':
    start_worker()  # Start the job worker

    app_process = start_flask()

    # Expose the Flask app using Localtunnel
    try:
        result = subprocess.run(["lt", "--port", "5000", "--subdomain", "larslars1337"], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Localtunnel connection failed: {e}")
        app_process.terminate()
    except KeyboardInterrupt:
        app_process.terminate()
