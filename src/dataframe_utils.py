"""
download_dataframe_as_csv(df): This function takes a pandas DataFrame (df) as input and generates a CSV file for download. 
It encodes the DataFrame as a CSV, converts it to base64 format, and creates a download link for the generated file. 
The downloaded file will have a name based on the current date and time.
load_pickle_file(file_path): This function loads a pickle file specified by the file_path parameter using the joblib library. 
It returns the loaded object from the pickle file.
"""
import pandas as pd
import base64
from datetime import datetime
import joblib

def download_dataframe_as_csv(df):
    datetime_now = datetime.now().strftime("%d%b%Y_%Hh%Mmin%Ss")
    csv = df.to_csv().encode()
    b64 = base64.b64encode(csv).decode()
    href = f'<a href="data:file/csv;base64,{b64}" download="Report {datetime_now}.csv" target="_blank">Download Report</a>'
    return href

def load_pickle_file(file_path):
    return joblib.load(file_path)
