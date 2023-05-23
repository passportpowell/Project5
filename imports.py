import streamlit as st
from app_pages.multipage import MultiPage
from app_pages.summary import summary_body, hypothesis_body
from app_pages.leaves_visualizer import leaves_visualizer_body
from PIL import Image
import numpy as np
import pandas as pd
from src.data_management import download_dataframe_as_csv
from src.machine_learning.predictive_analysis import load_model_and_predict, resize_input_image, plot_predictions_probabilities
import matplotlib.pyplot as plt
from matplotlib.image import imread
from src.machine_learning.evaluate_clf import load_test_evaluation
import plotly.express as px
from tensorflow.keras.models import load_model
from src.data_management import load_pkl_file
import base64
from datetime import datetime
import joblib
