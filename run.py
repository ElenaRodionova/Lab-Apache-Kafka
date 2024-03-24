import subprocess 

subprocess.run(["docker-compose", "up", "-d"]) 

PYTHON_PATH = '/home/new_user/Lab-Apache-Kafka'

processes = {} 
processes["1"] = subprocess.Popen([PYTHON_PATH,'./run/data_generation.py']) 
processes["2"] = subprocess.Popen([PYTHON_PATH,'./run/processing.py']) 
processes["3"] = subprocess.Popen([PYTHON_PATH,'./run/inference.py']) 
processes["4"] = subprocess.Popen([PYTHON_PATH, '-m', 'streamlit', 'run', './run/visualization.py']) 

try: 
    while True: 
        continue 
except KeyboardInterrupt: 
    print("Interrupting by keyboard.")

    for p_id in processes.keys(): 
        processes[p_id].kill() 
        if processes[p_id].poll() is None: 
            print(f"Процесс {p_id} выполняется: {processes[p_id].pid}!")
        else: 
            print(f"Процесс {p_id} завершён!")

    subprocess.run(["docker-compose", "down"]) 