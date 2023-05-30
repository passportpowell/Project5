"""
-plot_predictions_probabilities(pred_proba, pred_class): This function takes pred_proba (prediction probabilities) and pred_class (predicted class) as input. 
It creates a bar plot using Plotly Express to visualize the probabilities of the 
-predicted class and the complementary class (1 - pred_proba). The resulting plot is displayed using st.plotly_chart().
resize_input_image(img, version): This function resizes the input image img based on the image shapes loaded from a 
pickle file using the load_pkl_file function from the src.data_management module. The resized image is then normalized and returned.
-load_model_and_predict(my_image, version): This function loads a trained model from a saved file (cherry_mildew_model.h5), 
predicts the probabilities of the input my_image using the model, and determines the predicted class based on a threshold of 0.5. 
The function returns the predicted probability and class.
"""

import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from tensorflow.keras.models import load_model
from PIL import Image
from src.dataframe_utils import load_pickle_file


def plot_predictions_probabilities(pred_proba, pred_class):
    prob_per_class = pd.DataFrame(
        data=[[0], [0]],
        index=['healthy', 'powdery_mildew'],
        columns=['Probability']
    )
    prob_per_class.loc[pred_class] = pred_proba
    prob_per_class.loc[~prob_per_class.index.isin([pred_class])] = 1 - pred_proba
    prob_per_class = prob_per_class.round(3)
    prob_per_class['Diagnostic'] = prob_per_class.index

    fig = px.bar(
        prob_per_class,
        x='Diagnostic',
        y='Probability',
        range_y=[0, 1],
        width=600, height=300, template='seaborn'
    )
    st.plotly_chart(fig)

#--------------------------------------------
def resize_input_image(img, version):
    images_shapes = load_pickle_file(f"outputs/{version}/images_shapes.pkl")
    img_resized = img.resize((images_shapes[1], images_shapes[0]), Image.ANTIALIAS)
    my_image = np.expand_dims(img_resized, axis=0) / 255

    return my_image

#--------------------------------------------
def load_model_and_predict(my_image, version):
    model = load_model(f"outputs/{version}/model training/cherry_mildew_model.h5")

    pred_proba = model.predict(my_image)[0, 0]

    target_map = {0: 'healthy', 1: 'powdery_mildew'}
    pred_class = target_map[int(pred_proba > 0.5)]
    if pred_class == 'healthy':
        pred_proba = 1 - pred_proba

    st.write(
        f"The predictive analysis indicates the sample leaf is "
        f"**{pred_class.lower()}**."
    )

    return pred_proba, pred_class
#------------------------------
