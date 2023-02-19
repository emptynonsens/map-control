import streamlit as st
import pandas as pd
from library.dummy_data import data

class Data:
    def __init__(self):
        self.data = self.upload_file()
        self.downlaod_data = self.downlaod_data(self.data)
    def upload_file(self):
        uploaded_file = st.file_uploader("Choose a file")
        if uploaded_file is not None:
            df = pd.read_csv(uploaded_file)
            st.write(df)
        else:
        # Create DataFrame from dict
            df = pd.DataFrame.from_dict(data)
        return df

    def downlaod_data(self, data_to_download):
        @st.cache_data 
        def convert_df(data_to_download):
            return data_to_download.to_csv().encode('utf-8')

        df_download = convert_df(data_to_download)
        downlaod_data = st.download_button(
            label="Download data as CSV",
            data=df_download,
            file_name='df.csv',
            mime='text/csv',
        )
