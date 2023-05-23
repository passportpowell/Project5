import streamlit as st
import matplotlib.pyplot as plt


def summary_body():
    """ Function to show the summary page """
    st.write("### Quick Project Summary")

    st.success(
        "**Introduction**:\n\n"
        "- The client is interested in conducting a study to visually determine if a cherry leaf has mildew on it.\n\n"

        "- Mildew is a common type of fungal infection that affects plants, including various types of leaves. "
        "It is caused by different species of fungi, such as powdery mildew or downy mildew. Mildew appears as "
        "a powdery or fuzzy growth on the surfaces of leaves, stems, and other plant parts.\n\n"

        "- It can inhibit photosynthesis, leading to stunted growth, yellowing leaves, and reduced yields in crops." 
        "Severe infestations can cause leaf drop and ultimately result in plant death if left untreated.\n\n"

        "**Project Dataset**:\n\n"
        "- The dataset used in this project was obtained from Kaggle and contains 4208 images of cherry leaves with and without powdery mildew."
)




    st.success(
        f"The project has 2 business requirements:\n\n"
        f"1 - The client is interested in having a study to differentiate a cherry leaf that's healthy and a cherry "
        f"leaf that has powdery mildew.\n\n"
        f"2 - The client is interested in telling whether a given cherry leaf has powdery mildew on the surface or not."
    )    
    
    st.write(
        f"[Project README file](https://github.com/passportpowell/project5/blob/main/README.md)."
    )
# #---------------------------------------
