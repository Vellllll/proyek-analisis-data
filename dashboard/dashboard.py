import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

sum_products_df = pd.read_csv('https://raw.githubusercontent.com/Vellllll/proyek-analisis-data/main/dashboard/sum_products_df.csv')
sum_sellers_df = pd.read_csv('https://raw.githubusercontent.com/Vellllll/proyek-analisis-data/main/dashboard/sum_sellers_df.csv')

st.header('Brazilian E-commerce Dashboard :sparkles:')
st.subheader('Products distribution')

product_options = st.radio(
    label = 'Urutkan berdasarkan jumlah penjualan produk',
    options = ('Tertinggi', 'Terendah'),
    horizontal = True
)

product_category_name_english = st.multiselect(
    label="What's your favorite movie genre",
    options = sum_products_df['product_category_name_english'].unique()
)

fig, ax = plt.subplots(figsize = (20,10))

if len(product_category_name_english) > 0:
    sum_products_df = sum_products_df[sum_products_df['product_category_name_english'].isin(product_category_name_english)]

sns.barplot(
    x = 'product_id',
    y = 'product_category_name_english',
    data = sum_products_df.sort_values(by = 'product_id', ascending = False).head(10) if product_options == 'Tertinggi' else sum_products_df.sort_values(by = 'product_id', ascending = True).head(10),
    ax = ax
)

ax.tick_params(axis = 'x', labelsize = 30)
ax.tick_params(axis = 'y', labelsize = 30)
ax.set_title('Products distribution by its category', loc = 'center', fontsize = 30)
st.pyplot(fig)

st.subheader('Sellers performance')

sellers_options = st.radio(
    label = 'Urutkan berdasarkan jumlah omset seller',
    options = ('Tertinggi', 'Terendah'),
    horizontal = True
)

seller_states = sum_sellers_df['seller_state'].unique()
seller_states.sort()

sellers_select_by_state = st.selectbox(
    label="Filter berdasarkan state seller",
    options=seller_states
)

sum_sellers_df = sum_sellers_df[sum_sellers_df['seller_state'] == sellers_select_by_state]

col1, col2, col3 = st.columns(3)

# with col1:
fig, ax = plt.subplots(figsize = (20,10))

sns.barplot(
    x = 'price',
    y = 'seller_city',
    data = sum_sellers_df.sort_values(by = 'price', ascending = False).head(10) if sellers_options == 'Tertinggi' else sum_sellers_df.sort_values(by = 'price', ascending = True).head(10),
    ax = ax
)

ax.tick_params(axis = 'x', labelsize = 30)
ax.tick_params(axis = 'y', labelsize = 30)
ax.set_title('Omset produk', loc = 'center', fontsize = 30)
st.pyplot(fig)

# with col2:
fig, ax = plt.subplots(figsize = (20,10))

sns.barplot(
    x = 'product_id',
    y = 'seller_city',
    data = sum_sellers_df.sort_values(by = 'product_id', ascending = False).head(10) if sellers_options == 'Tertinggi' else sum_sellers_df.sort_values(by = 'product_id', ascending = True).head(10),
    ax = ax
)

ax.tick_params(axis = 'x', labelsize = 30)
ax.tick_params(axis = 'y', labelsize = 30)
ax.set_title('Jumlah penjualan produk', loc = 'center', fontsize = 30)
st.pyplot(fig)

# with col3:
fig, ax = plt.subplots(figsize = (20,10))

sns.barplot(
    x = 'order_item_id',
    y = 'seller_city',
    data = sum_sellers_df.sort_values(by = 'order_item_id', ascending = False).head(10) if sellers_options == 'Tertinggi' else sum_sellers_df.sort_values(by = 'order_item_id', ascending = True).head(10),
    ax = ax
)

ax.tick_params(axis = 'x', labelsize = 30)
ax.tick_params(axis = 'y', labelsize = 30)
ax.set_title('', loc = 'center', fontsize = 30)
st.pyplot(fig)

