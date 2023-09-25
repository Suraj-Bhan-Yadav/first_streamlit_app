
import streamlit as st


import requests
import pandas

import snowflake.connector 
from urllib.error import URLError

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



def get_fruityvice_data(this_fruit_choice):
  fruityvice_response = requests.get("https://fruityvice.com/api/fruit/"+fruit_choice)
  fruityvice_normalized = pandas.json_normalize(fruityvice_response.json())
  return fruityvice_normalized
      

st.header("Fruityvice Fruit Advice!")

try:
   fruit_choice = st.text_input('What fruit would you like information about?','Kiwi')
   if not fruit_choice:
        st.error('please select a fruit to get a information.')
   else:
        back_from_function=get_fruityvice_data(fruit_choice)
        st.dataframe(back_from_function)
except URLError as e:
    st.error()
     
 
#st.write('The user entered ', fruit_choice)

#st.stop()

st.header("View Our Fruit List-Add Your Favorites!")
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
         my_cur.execute("select * from fruit_load_list")
         return my_cur.fetchall()
         



if st.button('Get Fruit List'):
   my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
   my_data_row = get_fruit_load_list()
   my_cnx.close()
   st.dataframe(my_data_row)


def insert_row_snowflake(new_fruit):
    with my_cnx.cursor() as my_cur:
         my_cur.execute("insert into fruit_load_list values ('jackfruit')")
         return "Thanks for adding " + new_fruit


add_my_fruit = st.text_input('What fruit would you like add?')
if st.button('Add a Fruit to the List'):
   my_cnx = snowflake.connector.connect(**st.secrets["snowflake"])
   st.text(back_from_function)

