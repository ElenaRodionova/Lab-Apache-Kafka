import pandas as pd 
import random 
import time 
from Consumer_and_Producer import Producer
from data_path import DATA_PATH 
import warnings 
warnings.simplefilter(action='ignore', category=FutureWarning)


bootstrap_server_produce = 'localhost:9094'
topic_produce = 'raw_data' 
conf_produce = {'bootstrap.servers': bootstrap_server_produce} 
producer_1 = Producer(conf_produce) 
producer_2 = Producer(conf_produce)
producer_3 = Producer(conf_produce) 


dataset = pd.read_csv(f"{DATA_PATH}",  sep=',', encoding='utf8', index_col=None)
 
while True: 
    data_1 = dataset.sample(frac=random.uniform(0.001, 0.01)).to_dict() 
    data_2 = dataset.sample(frac=random.uniform(0.001, 0.01)).to_dict()
    data_3 = dataset.sample(frac=random.uniform(0.001, 0.01)).to_dict() 

    producer_1.send_message(topic_produce, key='1', value=data_1)
    producer_2.send_message(topic_produce, key='1', value=data_2)
    producer_3.send_message(topic_produce, key='1', value=data_2) 

    time.sleep(30 + random.uniform(-5.0, 5.0)) # ждём случайные n секунд