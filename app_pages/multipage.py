"""
This code defines a MultiPage class for creating Streamlit applications with multiple pages. 
It has methods to add pages and run the application. The class sets the page configuration and 
displays a sidebar for page selection. The selected page's function is executed to show its content.
"""

import streamlit as st

class MultiPage:
    def __init__(self, app_name):
        self.pages = []
        self.app_name = app_name

        st.set_page_config(
            page_title=self.app_name,
            page_icon="🖥️",
            layout="wide",
            initial_sidebar_state="expanded"
        )

    def add_page(self, title, func):
        self.pages.append({"title": title, "function": func})

    def run(self):
        st.title(self.app_name)
        page = st.sidebar.radio('Select a page:', self.pages, format_func=lambda page: page['title'])
        page['function']()
