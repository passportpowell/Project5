"""
The `summary_body` function displays the summary page of a Streamlit application. 
It writes a predefined summary text using `st.write`. 
The text includes project details, dataset information, business requirements, and a link to the project's README.
"""

import streamlit as st

def summary_body():
    """ Function to show the summary page """
    st.write("**Project Summary:**")

    summary_text = """
        - This project aims to develop a system for visually determining whether a cherry leaf has powdery mildew or not.
          Powdery mildew is a fungal infection that affects plants and can lead to stunted growth, yellowing leaves, and reduced yields in crops if left untreated.
          The project focuses on two main business requirements: visually differentiating healthy cherry leaves from those with powdery mildew and predicting 
          whether a cherry leaf is healthy or infected.

        - It can inhibit photosynthesis, leading to stunted growth, yellowing leaves, and reduced yields in crops.
          Severe infestations can cause leaf drop and ultimately result in plant death if left untreated.

        **Project Dataset**:
        - The project utilizes a dataset of 4208 images of cherry leaves with and without powdery mildew obtained from Kaggle.

        **Business requirements**:
        - The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one that contains powdery mildew.
        - The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

        **Project README**:
        - Please refer to the [README file](https://github.com/passportpowell/project5/blob/main/README.md) in the project repository for detailed information on the project, including installation instructions, dataset description,
          usage guidelines, and additional resources.
    """

    st.write(summary_text)


#---------------------------------------
