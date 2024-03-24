import subprocess 

subprocess.run(["docker-compose", "up", "-d"]) 

PYTHON_PATH = 'C:\Users\User-PC\AppData\Local\Programs\Python\Python312'

processes = {} 
processes["1"] = subprocess.Popen([PYTHON_PATH,'./run/data_generation.py']) 
processes["2"] = subprocess.Popen([PYTHON_PATH,'./run/processing.py']) 
processes["3"] = subprocess.Popen([PYTHON_PATH,'./run/inference.py']) 
processes["4"] = subprocess.Popen([PYTHON_PATH, '-m', 'streamlit', 'run', './run/visualization.py']) 
