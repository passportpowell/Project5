"""
load_evaluation_results(version): This function takes a version parameter and loads evaluation results from a pickle 
file using the load_pickle_file function from the src.dataframe_utils module. The path to the pickle file is constructed 
based on the provided version. The loaded results are returned.

from src.dataframe_utils import load_pickle_file: This line imports the load_pickle_file function from the 
src.dataframe_utils module, which is used in the load_evaluation_results function.
"""

import streamlit as st
from src.dataframe_utils import load_pickle_file

def load_evaluation_results(version):
    results = load_pickle_file(f'./outputs/v2/model training/evaluation/model_evaluation.pkl')
    print(results)
    return results
