import streamlit as st
import pandas as pd

# Function to load CSV files into dataframes
@st.cache_data
def load_data():
    trips = pd.read_csv("datasets/trips.csv")
    cars = pd.read_csv("datasets/cars.csv")
    cities = pd.read_csv("datasets/cities.csv")
    return trips, cars, cities

#load data
trips, cars, cities = load_data()

# Merge trips with cars (joining on car_id)
trips_merged = trips.merge(cars, left_on="car_id", right_on="id")

# Merge with cities for car's city (joining on city_id)
trips_merged = trips_merged.merge(cities, on="city_id")

trips_merged = trips_merged.drop(columns=["car_id", "city_id", "customer_id"])

# Convert pickup_time to datetime and extract pickup_date
trips_merged['pickup_time'] = pd.to_datetime(trips_merged['pickup_time'])
trips_merged['dropoff_time'] = pd.to_datetime(trips_merged['dropoff_time'])
trips_merged['pickup_date'] = trips_merged['pickup_time'].dt.date

cars_brand = st.sidebar.multiselect("Select the Car Brand", trips_merged['brand'].unique())
if cars_brand:
    trips_merged = trips_merged[trips_merged['brand'].isin(cars_brand)]

# Compute business performance metrics
total_trips = len(trips_merged)
total_distance = trips_merged['distance'].sum()
# Car model with the highest revenue
grouped_revenue = trips_merged.groupby('model')['revenue'].sum()
if not grouped_revenue.empty:
    top_car = grouped_revenue.idxmax()
else:
    top_car="Null"
    print("No data available for revenue calculation.")
# Display metrics in columns
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Total Trips", value=total_trips)
with col2:
    st.metric(label="Top Car Model by Revenue", value=top_car)
with col3:
    st.metric(label="Total Distance (km)", value=f"{total_distance:,.2f}")

st.write(trips_merged.head())

#Trips Over Time
st.subheader("Trips Over Time")
Trips_Count = trips_merged["pickup_date"].value_counts()
st.line_chart(Trips_Count)

#Revenue Per Car Model
st.subheader("Revenue by Car Model")
revenue_by_car = trips_merged.groupby('model')['revenue'].sum()
st.bar_chart(revenue_by_car)

#Cumulative Revenue Growth Over Time
st.subheader("Cumulative Revenue Growth Over Time")
cum_revenue_over_time = trips_merged.groupby('pickup_date')['revenue'].sum().cumsum()
st.area_chart(cum_revenue_over_time)

# Trips by Car Model
st.subheader("Trips by Car Model")
trips_by_car_model = trips_merged['model'].value_counts()
st.bar_chart(trips_by_car_model)

# Average Trip Duration by City
st.subheader("Average Trip Duration by City")
trips_merged["trip_duration"] = (trips_merged["dropoff_time"] - trips_merged["pickup_time"]).dt.total_seconds() / 60
avg_trip_duration = trips_merged.groupby('city_name')['trip_duration'].mean()
st.bar_chart(avg_trip_duration)

# Revenue by City
st.subheader("Revenue by City")
revenue_by_city = trips_merged.groupby('city_name')['revenue'].sum()
st.bar_chart(revenue_by_city)

# Trips per Day of the Week
st.subheader("Trips per Day of the Week")
trips_merged['Day of Week'] = pd.to_datetime(trips_merged['pickup_time']).dt.day_name()
trips_by_day = trips_merged['Day of Week'].value_counts().reindex(
    ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
)
st.bar_chart(trips_by_day)