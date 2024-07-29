import configparser
import pandas as pd
import streamlit as st
import boto3


#config = configparser.ConfigParser()

#config.read('aws.cfg')

#aws_access_key = config['AWS']['aws_access_key_id']
#aws_secret_key = config['AWS']['aws_secret_access_key']

#s3 = boto3.client('s3', aws_access_key_id = aws_access_key, aws_secret_access_key = aws_secret_key)

st.title['NYC Taxi Data Analysis']

#output = s3.download_file(Bucket="capstone-techcatalyst-raw", Key='yellow_taxi")

df = pd.read_parquet('nyc.parquet')

cols = st.multiselect('Select Columns', df.columns)

if len(cols) > 0:
    st.dataframe(df[cols])

if st.chckbox("Show Data"):
    st.dataframe(df[cols].head(20))

#read CSV file
file = st.file_uploader("Upload your CSV data", type = ["csv"])
st.write(file)

read_file = pd.read_csv(file)

st.dataframe(read_file.head(10))


ts = df[['tpep_pickup_datetime', 'total_amount']]


if st.chckbox("Show Line Chart"):
    st.line_chart(ts_sum set_index("date"))

st.write("Top 10 Pick up Locations")
st.dataframe(df["PULocationID"]).value_counts().head()

st.write('Filter data by date')
date = st.date_input('Date', df['tpep_pickup_datetime'].max())
st.write(df[df['tpep_pickup_datetime'].dt.date == date])


st.balloons()