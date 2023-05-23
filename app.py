import streamlit as st
from app_pages.multipage import MultiPage

from app_pages.summary_page import summary_page_body
from app_pages.leaves_visualizer_page import leaves_visualizer_page_body
from app_pages.mildew_detertor_page import mildew_detector_body
from app_pages.project_hypothesis_page import project_hypothesis_page_body
from app_pages.ml_performance_page import ml_performance_body


app = MultiPage(app_name="Powdery Mildew Detector")

pages = {
    'Quick Project Summary': summary_page_body,
    'Leaves Visualizer': leaves_visualizer_page_body,
    'Powdery Mildew Detector': mildew_detector_body,
    'Project Hypothesis': project_hypothesis_page_body,
    'ML Performance Metrics': ml_performance_body
}

for page_name, page_body in pages.items():
    app.add_page(page_name, page_body)

app.run()
