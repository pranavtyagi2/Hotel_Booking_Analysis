# 🏨 Hotel Booking Analysis Dashboard

**Interactive Dashboard to Analyze Hotel Booking Data and Cancellation Patterns**

---

## 📖 Project Overview
This project uses **Python and Streamlit** to explore and visualize hotel booking data.  
It helps understand **booking trends, cancellation rates, lead times, and customer behavior**, providing actionable insights for hotel management and business decisions.

---

## 🛠 Features

- **Interactive Filters:**  
  - Hotel Type (City / Resort)  
  - Arrival Year  
  - Month  
  - Country  

- **Key Metrics (KPIs):**  
  - Total Bookings  
  - Cancelled Bookings  
  - Cancellation Rate (%)  
  - Average Lead Time  
  - Average Daily Rate (ADR)  

- **Visualizations:**  
  - Monthly Booking Trend  
  - Cancellation by Hotel Type  
  - Lead Time vs Cancellation  
  - Top 10 Countries by Bookings  

- **Technology Stack:**  
  - Python, Pandas, NumPy  
  - Matplotlib & Seaborn  
  - Streamlit for interactive UI  

---

## 📂 Dataset
- The dataset contains hotel booking information including:  
`hotel, is_canceled, lead_time, arrival_date_year, arrival_date_month, stays_in_weekend_nights, stays_in_week_nights, adults, children, country, adr, customer_type, total_of_special_requests, reservation_status`  
- Sensitive columns like `name, email, phone-number, credit_card` are **not displayed** in the dashboard for privacy.
