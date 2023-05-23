import streamlit as st
import os
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.image import imread

import itertools
import random



def leaves_visualizer_body():
    st.info("The client is interested in determining whether a given leaf contains powdery mildew or not.")
    st.write("You can download a set of healthy and powdery mildew cherry leaf images for live prediction. "
             "Download the images from [here](https://www.kaggle.com/datasets/codeinstitute/cherry-leaves).")
    st.write("---")

    images_buffer = st.file_uploader('Upload cherry leaf images. You may select more than one.',
                                     type='png', accept_multiple_files=True)

    if images_buffer is not None:
        df_report = pd.DataFrame([])
        for image in images_buffer:
            img_pil = Image.open(image)
            st.info(f"Cherry leaf image: **{image.name}**")
            img_array = np.array(img_pil)
            st.image(img_pil, caption=f"Image Size: {img_array.shape[1]}px width x {img_array.shape[0]}px height")

            version = 'v1'
            resized_img = resize_input_image(img=img_pil, version=version)
            pred_proba, pred_class = load_model_and_predict(resized_img, version=version)
            plot_predictions_probabilities(pred_proba, pred_class)

            df_report = df_report.append({"Name": image.name, 'Result': pred_class}, ignore_index=True)

        if not df_report.empty:
            st.success("Analysis Report")
            st.table(df_report)
            st.markdown(download_dataframe_as_csv(df_report), unsafe_allow_html=True)
# #-------------------------------
