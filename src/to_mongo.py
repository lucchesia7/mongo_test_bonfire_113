from base import Base
from dotenv import load_dotenv
import pymongo
import os

class ToMongo(Base):
    """
     Designed class to transport data from base to Mongo instance
     Initializes a instance of the inherited class.
     Defined methods as follows:
     
     # TODO
    """
    def __init__(self):
        # Initialize the instance of an inherited class
        Base.__init__(self)
        
        # Load in env variables
        load_dotenv()
        self.mongo_url = os.getenv('MONGO_URL')
        
        # Connect to PyMongo
        self.client = pymongo.MongoClient(self.mongo_url)
        
        # Create a database
        self.db = self.client.db
        
        # Create a collection
        self.cards = self.db.cards

        # Set dataframe index to id column.
        self.df.set_index('id', inplace=True)
        
    # Upload cards
    def upload_one_by_one(self):
        ''' Uploads an item to MongoDB one-by-one '''
        for i in self.df.index:
            self.cards.insert_one(self.df.loc[i].to_dict())

    def upload_collection(self):
        ''' Uploads an entire list of items to MongoDB
            BE WARNED! THERE IS A MAXIMUM SIZE!!!
            Limitations to the amount of data you can upload'''
        self.cards.insert_many([self.df.to_dict()])
    
    def delete_cards(self):
        ''' Drop a database'''
        self.db.drop_collection('cards')
if __name__ == '__main__':
    c = ToMongo()
    print('Successful connection to client object')
    c.delete_cards()
    print('Deleted all cards from Database object')
    c.upload_one_by_one()
    print('Upload data has been completed')
    # c.upload_collection()
