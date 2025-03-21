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
load_data()

# Merge trips with cars (joining on car_id)
trips_merged = trips.merge(car_id)

# Merge with cities for car's city (joining on city_id)
trips_merged = trips_merged.merge(city_id)

trips_merged = trips_merged.drop(columns=["id_car", "city_id", "id_customer","id"])

df['pickup_date'] = pd.to_datetime(df['pickup_time']).dt.date

df['pickup_date'] = pd.to_datetime(df['pickup_time']).dt.date

cars_brand = st.sidebar.multiselect("Select the Car Brand", unique(trips_merged))

trips_merged = trips_merged[isin(brand)]

# Compute business performance metrics
total_trips = sum(trips) # Total number of trips
total_distance = sum(distances) # Sum of all trip distances
# Car model with the highest revenue
top_car = car_model.max(revenue)
# Display metrics in columns
col1, col2, col3 = st.columns(3)
with col1:
    st.metric(label="Total Trips", value=total_trips)
with col2:
    st.metric(label="Top Car Model by Revenue", value=top_car)
with col3:
    st.metric(label="Total Distance (km)", value=f"{total_distance:,.2f}")

st.write(dataframe(trips_merged.head()))

#Trips Over Time
st.subheader("Trips Over Time")
Trips_Count = df["Trips Date"].value_counts()
st.line_chart(Trips_Count)

#Revenue Per Car Model
st.subheader("Revenue by Car Model")
revenue_by_car = df.groupby('car_model')['revenue'].sum()
st.bar_chart(revenue_by_car)

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

# Trips per Day of the Week
st.subheader("Trips per Day of the Week")
df['Day of Week'] = pd.to_datetime(df['pickup_time']).dt.day_name()
trips_by_day = df['Day of Week'].value_counts().reindex(
    ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
)
st.bar_chart(trips_by_day)