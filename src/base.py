import pandas as pd
import requests

class Base:
    def __init__(self):
        self.df = None
        self.api_url ='https://api.scryfall.com/bulk-data'
        self.get_data()
        return
    
    def return_string(self):
        return self.api_url
    
    
    def get_data(self):
        ''' Scraping data from the API and creating a dataframe object from it '''
        response = requests.get(self.api_url)
        r = response.json()['data'][0]['download_uri']
        response_1 = requests.get(r)

        self.df = pd.DataFrame.from_dict(response_1.json())
        return self.df
    
if __name__ == '__main__':
    c = Base()
    print(c.return_string())
    print(c.get_data())
    c.get_data().to_csv('oracle_cards.csv')