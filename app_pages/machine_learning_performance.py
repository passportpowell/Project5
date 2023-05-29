"""
It displays the distribution of labels on the train, validation, and test sets using pie charts and bar charts.
It shows the loss and accuracy metrics obtained from the evaluation of the machine learning model.
It presents the model's accuracy history through visualizations of the training accuracy and training losses.
"""

import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd
from src.machine_learning.ml_evaluation import load_evaluation_results

def ml_performance_body():
    version = 'v2'

    st.write("### Train, Validation and Test Set: Labels Frequencies")


    labels_distribution_pie = plt.imread(f"outputs/{version}/labels_distribution_pie.png")
    st.image(labels_distribution_pie, caption='Labels Distribution on Train, Validation and Test Sets')

    labels_distribution = plt.imread(f"outputs/{version}/labels_distribution.png")
    st.image(labels_distribution, caption='Labels Distribution on Train, Validation and Test Sets')
    st.write("---")

    st.write("### Loss vs Accuracy")
    st.dataframe(pd.DataFrame(load_evaluation_results(version),
                 index=['Loss', 'Accuracy'],
                 columns=['Performance']))

    st.write("### Model Accuracy History")
    col1, col2 = st.columns(2)
    with col1: 
        model_acc = plt.imread(f"outputs/{version}/model_training_acc.png")
        st.image(model_acc, caption='Model Training Accuracy')
    with col2:
        model_loss = plt.imread(f"outputs/{version}/model_training_losses.png")
        st.image(model_loss, caption='Model Training Losses')
    st.write("---")


