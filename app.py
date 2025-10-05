import streamlit as st
import os
from apputil import Genius
from dotenv import load_dotenv

if __name__ == "__main__":
    load_dotenv()

    # set the access token 
    ACCESS_TOKEN = os.environ['ACCESS_TOKEN']

    genius = Genius(access_token=ACCESS_TOKEN)



    # calll to test get_artist
    genius.get_artist("Radiohead")

    # call to test get_artists
    df = genius.get_artists(['Rihanna', 'Tycho', 'Seal', 'U2'])

    print(df)


    st.write(
    '''
    # Week x: [Title]

    ...
    ''')

    # currently set for integer input
    amount = st.number_input("Exercise Input: ", 
                             value=None, 
                             step=1, 
                             format="%d")

    if amount is not None:
        st.write(f"The exercise input was {amount}.")

