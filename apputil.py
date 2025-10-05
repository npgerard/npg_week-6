# your code here ...

import tqdm
import requests
import pandas as pd
class Genius:

    #define the initialization function
    def __init__(self, access_token):
        '''Initialization Function for class Genius; Sets the access_token attribute.'''
        self.access_token = access_token

    def get_artist(self, search_term):
        '''Returns details about artists specified by search_term'''
        
        genius_search_url = f"http://api.genius.com/search?q={search_term}"

        response = requests.get(genius_search_url, 
                        headers={"Authorization": "Bearer " + self.access_token})
        
        json_data = response.json()

        # set the primary artist to the value we pull from JSON based on this structure
        # json_data
        # └── 'response'
        #     └── 'hits'
        #         └── [0]
        #                 └── 'result'
        #                     ├── 'primary_artist'      ← dict
        #                     └── 'primary_artists'     ← list of dicts
        primary_artist = json_data['response']['hits'][0]['result']['primary_artist']['id']

        # create the URL for the artist API
        genius_artist_url = f"http://api.genius.com/artists/{primary_artist}"

        # define the call for the artist api with the URL and the access token
        artist_response = requests.get(genius_artist_url,
                                       headers={"Authorization": "Bearer " + self.access_token})
        
        # get the JSON
        artist_json = artist_response.json()

        #return the JSON
        return artist_json
    
    def get_artists(self, search_terms):
        '''Returns a dataframe of details for all artists specified by search_terms'''
        
        # define the dataframe to hold the results
        df_artists = pd.DataFrame(columns=['search_term', 'artist_name', 'artist_id', 'followers_count'])

        #loop the search terms and call artist_json for each
        for search_term in search_terms:
            artist_json = self.get_artist(search_term)

            artist_name = artist_json['response']['artist']['name']
            artist_id = artist_json['response']['artist']['id']
            followers_count = artist_json['response']['artist']['followers_count']

            # create the row with the results
            row = {
                'search_term': search_term,
                'artist_name': artist_name,
                'artist_id': artist_id,
                'followers_count': followers_count
            }
            # append the row to the dataframe
            df_artists = pd.concat([df_artists, pd.DataFrame([row])], ignore_index=True)

        # return the dataframe
        return df_artists

