import streamlit
import pandas
import requests
import snowflake.connector
from urllib.error import URLError

streamlit.title("My first streamlit breakfast")

streamlit.header('Breakfast Menu')
streamlit.text('Omega 3 & Blueberry Oatmeal')
streamlit.text('Kale, Spinach & Rocket Smoothie')
streamlit.text('Hard-Boiled Free-Range Egg')
streamlit.header('🍌🥭 Build Your Own Fruit Smoothie 🥝🍇')


my_fruit_list = pandas.read_csv("https://uni-lab-files.s3.us-west-2.amazonaws.com/dabw/fruit_macros.txt")
my_fruit_list = my_fruit_list.set_index('Fruit')

###streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
###streamlit.dataframe(my_fruit_list)

fruits_selected=streamlit.multiselect("Pick some fruits:",list(my_fruit_list.index),['Avocado','Strawberries'])
fruits_to_show=my_fruit_list.loc[fruits_selected]
streamlit.dataframe(fruits_to_show)

def get_fruitvice_data(this_fruit_choice):
    fruitvice_response=requests.get("https://fruityvice.com/api/fruit/"+this_fruit_choice)
    fruitvice_normalized=pandas.json_normalize(fruitvice_response.json())
    return fruitvice_normalized
  
streamlit.header('Fruitvice Fruit Advice')
try:
  fruit_choice=streamlit.text_input('What fruit would you like information about?')
  if not fruit_choice:
    streamlit.error("Select a fruit to get information about it.")
  else:
    back_from_function=get_fruitvice_data(fruit_choice)
    streamlit.dataframe(back_from_function)
except URLError as e:
  streamlit.error()
  
#my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
#my_cur = my_cnx.cursor()
#my_cur.execute("Select * from fruit_load_list")
#my_data_rows = my_cur.fetchall()

streamlit.text("The fruit load contains:")
def get_fruit_load_list():
    with my_cnx.cursor() as my_cur:
         my_cur.execute("Select * from fruit_load_list")
         return my_cur.fetchall()
if streamlit.button ('Get fruit load list'):
   my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
   my_data_rows = get_fruit_load_list() 
   my_cnx.close()
   streamlit.dataframe(my_data_rows)     
        
#streamlit.stop()

def insert_row_snowflake (new_fruit):
    with my_cnx.cursor() as my_cur:
         my_cur.execute("insert into fruit_load_list values ('" + new_fruit + "')")
         return "Thank for adding "+new_fruit
add_my_fruit=streamlit.text_input('View our fruit list! Add your favourites!')
if streamlit.button ('Add a fruit to the list list'):
    my_cnx = snowflake.connector.connect(**streamlit.secrets["snowflake"])
    back_from_function = insert_row_snowflake (add_my_fruit)
    my_cnx.close()
    streamlit.text(back_from_function)
    
#streamlit.write('Thanks for adding',add_my_fruit)

#my_cur.execute("insert into PC_RIVERY_DB.PUBLIC.FRUIT_LOAD_LIST values ('from_streamlit')")


