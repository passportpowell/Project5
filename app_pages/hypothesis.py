"""
Introduces the hypothesis that a powdery mildew detection tool can accurately differentiate between healthy cherry leaves and those affected by powdery mildew.
It outlines the validation approach, which involves using the detection tool on a sample of cherry leaves suspected of infection.
It expects the tool to classify leaves as healthy or powdery mildew-infected based on the presence or absence of the characteristic white growth.
It mentions that visual inspections and expert assessments will be used as a reference to evaluate the tool's accuracy.
"""

import streamlit as st
import matplotlib.pyplot as plt
version = 'v2'

def hypothesis_body():
    st.write("### Powdery Mildew Detection Hypothesis and Validation Approach")

    st.write(
       "- Our hypothesis is that by utilizing a powdery mildew detection tool specifically designed for cherry leaves, "
        "we can accurately differentiate between healthy leaves and those affected by powdery mildew. The presence of a distinctive white growth, "
        "characteristic of powdery mildew, should provide a noticeable contrast against the green foliage of cherry trees.\n\n"

        "- To validate our hypothesis, we will employ the powdery mildew detection tool on a sample of cherry leaves suspected of infection. "
        "We expect that the tool will successfully identify and classify leaves as either healthy or powdery mildew-infected based on the presence or "
        "absence of the characteristic white growth. We will compare the tool's classifications with visual inspections and expert assessments to determine "
        "its accuracy in differentiating between healthy and affected leaves."
    )