import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.feature_selection import mutual_info_regression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error,mean_absolute_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from utils import load_data, make_mi_scores

from Consumer_and_Producer import Producer, Consumer
from data_path import DATA_PATH
from model import Predictor 


bootstrap_server_consume = 'localhost:9097' 
topic_consume = ['processed_data'] 
conf_consume = {'bootstrap.servers': bootstrap_server_consume, 'group.id': 'ML_inference'} 
consumer = Consumer(conf_consume) 
consumer.subscribe(topic_consume) 

bootstrap_server_produce = 'localhost:9094'
topic_produce = 'ML_results' 
conf_produce = {'bootstrap.servers': bootstrap_server_produce} 
producer = Producer(conf_produce) 


Predictor = Predictor()

while True:
    data, _ = consumer.get_message(timeout=1000) 
    if data is not None:
        pred = Predictor.predict(data.drop('price', axis=1)).tolist()       
        score = r2_score(data['price'], pred) 
        results = {"true": data['price'], "pred": pred, "r2": score} 
        
        producer.send_message(topic_produce, key='1', value=results)