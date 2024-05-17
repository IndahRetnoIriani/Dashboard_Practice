import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os

st.write(
    """
    # Bike Sharing Dashboard
    Hello, selamat datang!
    """
)
current_dir = os.path.dirname(__file__)
day_df_path = os.path.join(current_dir, "../../submission/data/day.csv")
hour_df_path = os.path.join(current_dir, "../../submission/data/hour.csv")


day_df= pd.read_csv(day_df_path)
hour_df = pd.read_csv(hour_df_path)
    
day_df['season'] = day_df['season'].map({1: 'Spring', 2: 'Summer', 3: 'Fall', 4: 'Winter'})
day_df['mnth'] = day_df['mnth'].map({
    1: 'January',
    2: 'Februari',
    3: 'March', 
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'Desember'
})

# Visualisasi 1: Bar plot untuk total penyewaan per-musim
byseason = day_df.groupby(by="season").agg({
    "cnt": "sum"
})
plt.figure(figsize=(10, 5))
sns.barplot(
    y="cnt",
    x="season",
    data=byseason.sort_values(by="cnt", ascending=True)
)
plt.title("Jumlah penyewa berdasarkan musim", loc="center", fontsize=15)
plt.ylabel("Jumlah")
plt.xlabel("Musim")
plt.tick_params(axis='x', labelsize=12)
plt.show()
st.bar_chart(byseason)

# Visualisasi 2: Line plot untuk total penyewaan per-bulan berdasarkan tipe registered atau casual
bymonth = day_df.groupby(by="mnth").agg({
    "casual": "sum", 
    "registered": "sum"})
plt.figure(figsize=(12, 6))
sns.lineplot(data=bymonth, palette=["skyblue", "red"])
plt.title("Total Penyewaan Berdasarkan Bulan", fontsize=15)
plt.xlabel("Bulan", fontsize=12)
plt.ylabel("Jumlah Penyewaan", fontsize=12)
plt.xticks(rotation=45)
plt.legend(title="Tipe", fontsize='large')
plt.show()
st.line_chart(bymonth)