
import streamlit as st


import requests
import pandas

import snowflake.connector from urllib.error import URLError

st.title('My First Streamlit App')
st.header('Breakfast Menu')
st.text('🥣 Omega 3 & Blueberry Oatmeal')
st.text('🥗 Kale, Spinach & Rocket Smoothie')
st.text('🐔 Hard-Boiled Free-Range Egg')
st.text('🥑🍞 Avacodo Toast')
 
st.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')

my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')
fruits_selected=st.multiselect("Pick some fruits:", list(my_fruit_list.index),['Grapefruit','Grapes'])
fruits_to_show = my_fruit_list.loc[fruits_selected]
st.dataframe(fruits_to_show)


st.header("Fruityvice Fruit Advice!")


fruit_choice = st.text_input('What fruit would you like information about?','Kiwi')
st.write('The user entered ', fruit_choice)

fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
#st.text(fruityvice_response.json())

# write your own comment -what does the next line do? 
fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
# write your own comment - what does this do?
st.dataframe(fruityvice_normalized)

streamlit.stop()

my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
my_cur = my_cnx.cursor()
my_cur.execute("insert into fruit_load_list values ('from streamlit')")
my_data_row = my_cur.fetchall()
st.header("The fruit load list contains:")
st.dataframe(my_data_row)

add_my_fruit = st.text_input('What fruit would you like add?','jackfruit')
st.write('Thanks for adding', add_my_fruit)

