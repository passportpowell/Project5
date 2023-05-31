"""
The leaves_mildew_detector_body function is part of a Streamlit application's 
It provides an interface to upload leaf images.
It performs predictions on whether the uploaded leaves contain powdery mildew.
It displays the uploaded images, their sizes, and the corresponding prediction results.
It generates a report table summarizing the image names and predictions.
It allows the user to download the report as a CSV file.
"""

import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
from src.dataframe_utils import download_dataframe_as_csv
from src.machine_learning.leaf_prediction import (load_model_and_predict, resize_input_image, plot_predictions_probabilities)


def leaves_mildew_detector_body():
    st.write("* The client is interested in telling whether a given leaf contains powdery mildew or not.")
    st.write("* If you'd like to make real-time predictions, you can obtain a series of cherry leaf images representing both healthy specimens and those with powdery mildew. You can acquire the image collection from this [location](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves).")

    images_buffer = st.file_uploader('Upload leaf images below.', type=['jpg', 'jpeg', 'png', 'gif', 'bmp', 'tiff', 'svg', 'ico', 'jfif', 'webp'], accept_multiple_files=True)
    if images_buffer:
        df_report = pd.DataFrame([])
        for image in images_buffer:
            img_pil = Image.open(image)
            st.info(f"Cherry leaf image: **{image.name}**")
            st.image(img_pil, caption=f"Image Size: {img_pil.size[0]}px width x {img_pil.size[1]}px height")
            version = 'v2'
            resized_img = resize_input_image(img=img_pil, version=version)
            pred_proba, pred_class = load_model_and_predict(resized_img, version=version)
            plot_predictions_probabilities(pred_proba, pred_class)
            # df_report = df_report.concat({"Name":image.name, 'Result': pred_class })
        if not df_report.empty:
            st.success("Analysis Report")
            st.table(df_report)
            st.markdown(download_dataframe_as_csv(df_report), unsafe_allow_html=True)
            
# -----------------------------------------
