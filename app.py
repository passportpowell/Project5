
"""
This code creates a Streamlit application with multiple pages. 
Each page has a specific body function that defines its content. 
The application is run, allowing users to navigate through the pages.
"""
import streamlit as st
from app_pages.multipage import MultiPage

from app_pages.summary import summary_body
from app_pages.leaves_visualizer import leaves_visualizer_body
from app_pages.leaves_mildew_detector import leaves_mildew_detector_body
from app_pages.hypothesis import hypothesis_body
from app_pages.machine_learning_performance import ml_performance_body

app = MultiPage(app_name="Powdery Mildew Detector")

pages = {
    'Project Summary': summary_body, #Page 1 
    'Leaves Visualizer': leaves_visualizer_body, #Page 2
    'Powdery Mildew Detector': leaves_mildew_detector_body, #Page 3
    'Project Hypothesis': hypothesis_body, #Page 4
    'ML Performance Metrics': ml_performance_body #Page 5
}

for page_name, page_body in pages.items():
    app.add_page(page_name, page_body)

app.run()
