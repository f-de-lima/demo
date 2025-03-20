import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("This is the data reader")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
  df = pd.read_csv(uploaded_file)
  st.write("Here is the preview of the Uploaded CSV: ")
  st.dataframe(df.head())

# Chart 1: Bar chart of customers by country
  st.subheader("Customers by City")
  country_counts = df['customer_city'].value_counts()
  #st.write(country_counts)
  st.bar_chart(country_counts)

  cars_brand = st.sidebar.multiselect("Select the car brand", df["car_brand"].unique(),  df["car_brand"].unique())
  df = df[df["car_brand"].isin(cars_brand)]

  col1, col2, col3, col4  = st.columns(4)

  col1.metric("Number of Trips", df.shape[0], border=True)
  col2.metric("Unique Customers",  df["customer_email"].nunique(),border=True)
  with col3:
    total_distance = df['distance'].sum() / 1000
    st.metric("Total Distance", value=f"{total_distance:.2f} K", border=True)
  with col4:
    average_revenue = df['revenue'].mean()
    st.metric("Average Revenue Per Trip", value=f"{average_revenue:.2f} €", border=True)



  col1, col2, col3 = st.columns(3)
  # Chart 1: Bar chart of customers by country
  with col1:
    st.subheader("Customers by City")
    country_counts = df['customer_city'].value_counts()
    st.bar_chart(country_counts)

  # Chart 2 : Revenue by Car Model
  with col2:
    st.subheader("Revenue by Car Model")
    revenue_by_car = df.groupby('car_model')['revenue'].sum()
    st.bar_chart(revenue_by_car)
  # Chart 3 : Average Trip distance per city
  with col3:
    st.subheader("Average Trip Distance per city")
    avg_distance_by_city = df.groupby('customer_city')['distance'].mean()
    st.bar_chart(avg_distance_by_city)
  # Convert the pickup time to a date type column 
  df['Trips Date'] = pd.to_datetime(df['pickup_time']).dt.date

  # Chart 3: Revenue over time 
  st.subheader("Revenue Over Time")
  revenue_over_time = df.groupby('Trips Date')['revenue'].sum()
  st.area_chart(revenue_over_time)

  # Chart 4: Line chart of Trips over time
  st.subheader("Trips Over Time")
  Trips_Count = df["Trips Date"].value_counts()
  st.line_chart(Trips_Count)



































#st.title("User CSV File Viewer")

# Request the user to Upload the File 
# uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

# if uploaded_file:
#     df = pd.read_csv(uploaded_file)
#     st.write("Here is the preview of the Uploaded CSV: ")
#     st.dataframe(df.head())

#     # Chart 1: Bar chart of customers by country
#     st.subheader("Customers by City")
#     country_counts = df['customer_city'].value_counts()
#     st.write(country_counts)
#     st.bar_chart(country_counts)

#     # Chart 2: Line chart of subscriptions over time
#     st.subheader("Trips Over Time")
#     df['Trip Date'] = pd.to_datetime(df['pickup_time']).dt.date
#     subscriptions_by_date = df.groupby('Trip Date').size().reset_index(name='Count')
#     st.line_chart(subscriptions_by_date.set_index('Trip Date'))




