from typing import List, Dict, Any, Iterable
import pandas as pd
import logging

logger = logging.getLogger(__name__)

logging.basicConfig(level=logging.INFO, format= "%(asctime)s - %(levelname)s : %(message)s")



class DataEnricher:
  """the enrisher class to clean and enrich the user and product dataframe"""
  
  def __innit__(self):
    self.missing_user_products = pd.DataFrame
  
  def data_enrich(self, products_list :List[Dict[str, Any]], users_list: List[Dict[str, Any]] )  -> pd.DataFrame:

    logging.info('enriching data')

    logging.info('coverting json data to dataframe')
    
    products_df = pd.DataFrame(products_list)
    users_df = pd.DataFrame(users_list)

    #breaking down products df
    logging.info('creating new products columns from nested dictionary')
    products_df['rate'] =  products_df['rating'].apply(lambda dict: dict['rate'])
    products_df['count'] =  products_df['rating'].apply(lambda dict: dict['count'])
    #products_cols =  [ col for col in products_df.columns if col not in [ 'rating', 'password' ,'username','__v'] ]
    products_cols =  ['rating','image'] 
    #print(products_cols)

    
   # logging.info('The user dataframe will have this columns: %s', products_df.columns)

    new_products_df = products_df.drop(products_cols, axis=1)
    #print(new_productd_df.columns)

    #breaking down users df
    
    logging.info('The product dataframe will have this columns: %s', new_products_df.columns)

    users_df['lat']=users_df['address'].apply(lambda dict: dict['geolocation']['lat'])
    users_df['long']=users_df['address'].apply(lambda dict: dict['geolocation']['long'])
    users_df['firstname'] = users_df['name'].apply(lambda dict: dict['firstname'])
    users_df['lastname'] = users_df['name'].apply(lambda dict: dict['lastname'])
    users_df['name'] = users_df['firstname'] + ' ' + users_df['lastname']
    
    #users_cols =  [ col for col in users_df.columns if col not in ['firstname', 'lastname','__v','image'] ]
    users_cols = ['address','firstname', 'lastname','__v', 'password' ,'username'] 
    
    
   # logging.info('The user dataframe will have this columns: %s', users_df.columns)
    #print(users_cols)
    new_users_df = users_df.drop(users_cols, axis=1)
    logging.info('The user dataframe will have this columns: %s', new_users_df.columns)

    #logging.info('The products dataframe has the shape: %s', new_products_df.shape)
    #print(new_products_df.head())
    
    logging.info('The users dataframe has the shape: %s', new_users_df.shape)

    #print(new_users_df.head())

    logging.info('merging new products and users together')

    merged_df = pd.merge(new_products_df, new_users_df,  how='left')
    merged_df['revenue'] = merged_df['price'] * merged_df['count'] #apply(lambda dict: dict['count'])

    logging.info('The merged df has the shape: %s', merged_df.shape)


    logging.info('checking missing user id')

    known_user_ids = list(new_users_df['id'].unique())

    missing_user_products = new_products_df[~new_products_df['id'].isin(known_user_ids)]
    
    self.missing_user_products  = missing_user_products 
    logging.info('Missing id found %s', missing_user_products.shape[0])
    logging.info('The missing id are %s', missing_user_products['id'].unique())
  #  logging.info('The merged dataframe %s', merged_df.head())

    merged_df.to_csv('merged_df.csv')

    return  merged_df