import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Dashboard Penyewaan Sepeda")

data = pd.read_csv('main_data.csv')

st.header("Data Penyewaan Sepeda")
st.write("Menampilkan 5 baris pertama dari dataset:")
st.dataframe(data.head())

# Visualisasi Pengaruh Cuaca terhadap Penyewaan Sepeda
st.header("Pengaruh Cuaca terhadap Penyewaan Sepeda")
st.write("Visualisasi jumlah penyewaan sepeda berdasarkan kondisi cuaca.")

fig1, ax1 = plt.subplots(figsize=(10, 5))
sns.barplot(x='weathersit', y='cnt', data=data, ax=ax1, ci=None, palette='Blues')
ax1.set_title('Jumlah Penyewaan Berdasarkan Kondisi Cuaca', fontsize=15)
ax1.set_xlabel('Weathersit (1: Cerah, 2: Sedang, 3: Buruk)', fontsize=12)
ax1.set_ylabel('Jumlah Penyewaan Sepeda', fontsize=12)
st.pyplot(fig1)

# Visualisasi Hari Kerja vs Akhir Pekan
st.header("Penyewaan Sepeda pada Hari Kerja vs Akhir Pekan")
data['is_weekend'] = data['weekday'].apply(lambda x: 'Akhir Pekan' if x in [0, 6] else 'Hari Kerja')

fig2, ax2 = plt.subplots(figsize=(10, 5))
sns.barplot(x='is_weekend', y='cnt', data=data, ax=ax2, ci=None, palette='coolwarm')
ax2.set_title('Perbandingan Penyewaan Sepeda pada Hari Kerja vs Akhir Pekan', fontsize=15)
ax2.set_xlabel('Hari Kerja vs Akhir Pekan', fontsize=12)
ax2.set_ylabel('Jumlah Penyewaan Sepeda', fontsize=12)
st.pyplot(fig2)

st.sidebar.header("Filter Data Penyewaan")
st.sidebar.write("Gunakan filter di bawah ini untuk menyesuaikan data:")

unique_weather = sorted(data['weathersit'].unique())
weather_option = st.sidebar.selectbox("Pilih Kondisi Cuaca:", options=unique_weather, index=0)

day_option = st.sidebar.radio("Pilih Hari:", ['Hari Kerja', 'Akhir Pekan'])

# Filter data berdasarkan cuaca dan hari yang dipilih
filtered_data = data[(data['weathersit'] == weather_option) & (data['is_weekend'] == day_option)]
st.write(f"Data penyewaan untuk cuaca: {weather_option} dan hari: {day_option}")
st.dataframe(filtered_data)

# Statistik tambahan untuk cuaca dan hari yang dipilih
st.write(f"Statistik penyewaan sepeda untuk cuaca: {weather_option} dan hari: {day_option}")
st.write(filtered_data[['cnt']].describe())

# Footer
st.write("© 2024 Dashboard Penyewaan Sepeda - Visualisasi data penyewaan sepeda berdasarkan cuaca dan hari.")
