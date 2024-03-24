import json

import pandas as pd 
import streamlit as st
from matplotlib import pyplot as plt
from confluent_kafka import Consumer
from Consumer_and_Producer import Producer, Consumer
from data_path import DATA_PATH
from model import Predictor 

def main():
    bootstrap_server_consume = 'localhost:9095' 
    topic_consume = ['raw_data', 'ML_results'] 
    conf_consume = {'bootstrap.servers': bootstrap_server_consume, 'group.id': 'data_visualizers'} 
    consumer = Consumer(conf_consume) 
    consumer.subscribe(topic_consume)

    st.set_page_config(
        page_title='flight price',
        layout='wide',
    )

    container_price = st.container(border=True) 
    container_price.title("Price") 
    holder_price = container_price.empty()

    container_score = st.container(border=True) 
    container_score.title("Model r2 score") 
    holder_score = container_score.empty()

    st.session_state["price"] = []
    st.session_state["r2 score"] = []
    while True:
        data, data_topic = consumer.get_message(timeout=1000)
        if data is not None:
            if data_topic == "raw_data": 
                data = pd.DataFrame(data)
                st.session_state["price"].append(data['price'])
                holder_price.line_chart(st.session_state["price"].) 
            elif data_topic == "ML_results":
                st.session_state["r2 score"].append(data["r2"]) 
                holder_score.line_chart(st.session_state["r2 score"]) 

if __name__ == '__main__':
    main()