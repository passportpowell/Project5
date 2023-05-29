
"""
The leaves_visualizer_body function displays the leaves visualizer page of a Streamlit application. It provides options for visual representation, 
differences between average powdery mildew and healthy leaves, and an image gallery. It uses checkboxes and buttons to control the display of images 
and allows the selection of a specific label for the image gallery. When the "Create Gallery" button is clicked, it generates a gallery of images 
based on the selected label.
"""

import streamlit as st
import os
import matplotlib.pyplot as plt

def leaves_visualizer_body():
    st.info("Visualization via contrasting powdery mildew with a healthy cherry leaves.")
    version = 'v2'
    
    if st.checkbox("Visual representation of average and variability:"):
        avg_powdery_mildew = plt.imread(f"outputs/{version}/avg_var_powdery_mildew.png")
        avg_healthy = plt.imread(f"outputs/{version}/avg_var_healthy.png")
        st.warning("* The average and variability images lack discernible patterns that allow for differentiation between them \n\n* A subtle distinction can be observed in the coloration of the average images")
        st.image(avg_powdery_mildew, caption='Powedery mildew leaf - Average and Variability')
        st.image(avg_healthy, caption='Healthy leaf - Average and Variability')
    st.write("---")
    #-----------------------
    if st.checkbox("Differences between average powdery mildew and average healthy leaves:"):
        diff_between_avgs = plt.imread(f"outputs/{version}/avg_diff.png")
        st.warning("* The study outcomes reveal a lack of identifiable patterns that would facilitate intuitive differentiation between the entities being studied.")
        st.image(diff_between_avgs, caption='Visible differences in the average images.')
    st.write("---")
    #------------------------
    if st.checkbox("Image Gallery:"):
        st.write("* Click 'Create Gallery' for a new set of images")
        my_data_dir = '/workspace/project5/inputs/datasets/cherry-leaves'
        labels = os.listdir(my_data_dir+ '/validation')
        label_to_display = st.selectbox(label="Select label", options=labels, index=0)
        if st.button("Create Gallery"):
            nrows, ncols = 8, 3
            fig, axes = plt.subplots(nrows=nrows, ncols=ncols, figsize=(10,25))
            images_list = os.listdir(os.path.join(my_data_dir, 'validation', label_to_display))
            for ax, img_path in zip(axes.ravel(), images_list):
                img = plt.imread(os.path.join(my_data_dir, 'validation', label_to_display, img_path))
                img_shape = img.shape
                ax.imshow(img)
                ax.set_title(f"Width {img_shape[1]}px x Height {img_shape[0]}px")
                ax.set_xticks([])
                ax.set_yticks([])
            plt.tight_layout()
            st.pyplot(fig=fig)