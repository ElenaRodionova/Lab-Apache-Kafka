import pandas as pd
import re
from Consumer_and_Producer import Producer, Consumer
from data_path import DATA_PATH
from model import Predictor 

import warnings 
warnings.simplefilter(action='ignore', category=FutureWarning) 


bootstrap_server_consume = 'localhost:9095' 
topic_consume = ['raw_data'] 
conf_consume = {'bootstrap.servers': bootstrap_server_consume, 'group.id': 'data_processors'} 
consumer = Consumer(conf_consume) 
consumer.subscribe(topic_consume)

bootstrap_server_produce = 'localhost:9095' 
topic_produce = 'processed_data' 
conf_produce = {'bootstrap.servers': bootstrap_server_produce} 
producer = Producer(conf_produce) 

while True: 
    data, _ = consumer.get_message(timeout=1000) 
    if data is not None: 
        data = pd.DataFrame(data) 
        
        data_y = data["price"].to_numpy().tolist() 
        data_X = data.drop(columns=["price"]).to_numpy().tolist() 
        data = {"x": data_X, "y": data_y} 

        producer.send_message(topic_produce, key='1', value=data)
        print('Сообщение получено')