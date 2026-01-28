import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

# Page config
st.set_page_config(page_title="Hotel Booking Analysis", layout="wide")

# Title
st.title("🏨 Hotel Booking Analysis Dashboard")
st.markdown("Interactive data analysis using Python & Streamlit")

# --- Load Data ---
@st.cache_data
def load_data():
    file_path = "hotel_booking.csv"
    if not os.path.exists(file_path):
        st.error(f"File not found: {file_path}")
        st.stop()
    return pd.read_csv(file_path)

df = load_data()

# --- Sidebar Filters ---
st.sidebar.header("🔎 Filter Data")

hotel_type = st.sidebar.multiselect(
    "Select Hotel Type",
    options=df["hotel"].unique(),
    default=df["hotel"].unique()
)

year = st.sidebar.multiselect(
    "Select Year",
    options=df["arrival_date_year"].unique(),
    default=df["arrival_date_year"].unique()
)

filtered_df = df[
    (df["hotel"].isin(hotel_type)) &
    (df["arrival_date_year"].isin(year))
]

# --- KPIs ---
total_bookings = len(filtered_df)
cancelled = filtered_df["is_canceled"].sum()
cancellation_rate = (cancelled / total_bookings) * 100 if total_bookings > 0 else 0
avg_adr = filtered_df["adr"].mean() if total_bookings > 0 else 0
avg_lead_time = filtered_df["lead_time"].mean() if total_bookings > 0 else 0

col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Bookings", total_bookings)
col2.metric("Cancelled Bookings", cancelled)
col3.metric("Cancellation Rate (%)", f"{cancellation_rate:.2f}")
col4.metric("Avg Lead Time (Days)", f"{avg_lead_time:.1f}")

st.divider()

# --- Charts ---
col5, col6 = st.columns(2)

# Monthly bookings
with col5:
    st.subheader("📈 Monthly Booking Trend")
    monthly_order = [
        'January', 'February', 'March', 'April', 'May', 'June',
        'July', 'August', 'September', 'October', 'November', 'December'
    ]
    monthly = filtered_df['arrival_date_month'].value_counts().reindex(monthly_order).fillna(0)
    fig, ax = plt.subplots()
    monthly.plot(kind="bar", ax=ax, color='skyblue')
    ax.set_ylabel("Bookings")
    ax.set_xlabel("Month")
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45)
    st.pyplot(fig)

# Cancellation by hotel type
with col6:
    st.subheader("❌ Cancellation by Hotel Type")
    cancel_hotel = filtered_df.groupby("hotel")["is_canceled"].mean()
    fig, ax = plt.subplots()
    cancel_hotel.plot(kind="bar", ax=ax, color='salmon')
    ax.set_ylabel("Cancellation Rate")
    st.pyplot(fig)

st.divider()

# Lead time vs cancellation
st.subheader("⏱ Lead Time vs Cancellation")
fig, ax = plt.subplots(figsize=(10,4))
sns.boxplot(x="is_canceled", y="lead_time", data=filtered_df, ax=ax, palette="Set2")
ax.set_xticklabels(["Not Cancelled", "Cancelled"])
st.pyplot(fig)

# Top countries
st.subheader("🌍 Top 10 Countries by Bookings")
top_countries = filtered_df["country"].value_counts().head(10)
fig, ax = plt.subplots()
top_countries.plot(kind="bar", ax=ax, color='lightgreen')
ax.set_ylabel("Bookings")
st.pyplot(fig)

st.markdown("---")
st.markdown("📌 **Built using Python, Pandas, Seaborn & Streamlit**")
