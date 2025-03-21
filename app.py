import streamlit as st
import pandas as pd

st.set_page_config(layout="wide")
st.title("This is the data reader")

uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

if uploaded_file:
  df = pd.read_csv(uploaded_file)

# getting info
  cars_brand = st.sidebar.multiselect("Select the car brand", df["car_brand"].unique(),  df["car_brand"].unique())
  df = df[df["car_brand"].isin(cars_brand)]
# setting cols to show numbers
  col1, col2, col3, col4  = st.columns(4)
# col1 = number of trips
  col1.metric("Number of Trips", df.shape[0], border=True)
# col2 = unique customers
  col2.metric("Unique Customers",  df["customer_email"].nunique(),border=True)
# col3 = calculating total distance
  with col3:
    total_distance = df['distance'].sum() / 1000
    st.metric("Total Distance", value=f"{total_distance:.2f} K", border=True)
# col4 calculating average revenue per trip
  with col4:
    average_revenue = df['revenue'].mean()
    st.metric("Average Revenue Per Trip", value=f"{average_revenue:.2f} €", border=True)

# setting new cols for plotting
  col1, col2, col3 = st.columns(3)
# col1 = customers by country
  with col1:
    st.subheader("Customers by City")
    country_counts = df['customer_city'].value_counts()
    st.bar_chart(country_counts)
# col2 = Revenue by Car Model
  with col2:
    st.subheader("Revenue by Car Model")
    revenue_by_car = df.groupby('car_model')['revenue'].sum()
    st.bar_chart(revenue_by_car)
# col3 = Average Trip distance per city
  with col3:
    st.subheader("Average Trip Distance per city")
    avg_distance_by_city = df.groupby('customer_city')['distance'].mean()
    st.bar_chart(avg_distance_by_city)

# Convert the pickup time to a date type column 
  df['Trips Date'] = pd.to_datetime(df['pickup_time']).dt.date

# Revenue over time 
  st.subheader("Revenue Over Time")
  revenue_over_time = df.groupby('Trips Date')['revenue'].sum()
  st.area_chart(revenue_over_time)

# Line chart of Trips over time
  st.subheader("Trips Over Time")
  Trips_Count = df["Trips Date"].value_counts()
  st.line_chart(Trips_Count)

  st.write("Here is the preview of the Uploaded CSV: ")
  st.dataframe(df.head())

#Cumulative Revenue Growth Over Time
st.subheader("Cumulative Revenue Growth Over Time")
cum_revenue_over_time = df.groupby('Trips Date')['revenue'].cumsum()
st.area_chart(cum_revenue_over_time)

# Trips by Car Model
st.subheader("Trips by Car Model")
trips_by_car_model = df['car_model'].value_counts()
st.bar_chart(trips_by_car_model)

# Average Trip Duration by City
st.subheader("Average Trip Duration by City")

df["pickup_time"] = pd.to_datetime(df["pickup_time"])
df["dropoff_time"] = pd.to_datetime(df["dropoff_time"])

df["trip_duration"] = (df["dropoff_time"] - df["pickup_time"]).dt.total_seconds() / 60
avg_trip_duration = df.groupby('customer_city')['trip_duration'].mean()
st.bar_chart(avg_trip_duration)

# Revenue by City
st.subheader("Revenue by City")
revenue_by_city = df.groupby('customer_city')['revenue'].sum()
st.bar_chart(revenue_by_city)

# Bonus: Trips per Day of the Week
st.subheader("Trips per Day of the Week")
df['Day of Week'] = pd.to_datetime(df['pickup_time']).dt.day_name()  # Extract day name
trips_by_day = df['Day of Week'].value_counts().reindex(
    ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
)
st.bar_chart(trips_by_day)