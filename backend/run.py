import subprocess
import os

# Change directory to the backend
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# Start the Flask backend
subprocess.Popen(["python", "app.py"])

# Change directory to the frontend
os.chdir("../frontend")

# Start the React frontend
subprocess.Popen(["npm", "start"])
