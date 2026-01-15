import pandas as pd
import os
from sqlalchemy import create_engine
import logging
import time

logging.basicConfig(
    filename="logs/ingestion_db.log",
    level=logging.DEBUG,
    format="%(asctime)s - %(levelname)s - %(message)s",
    filemode="a"
)

# Create SQLAlchemy engine
engine = create_engine("postgresql+psycopg2://postgres:Raja12@localhost:5434/retail")

def ingest_db(df, table_name, engine):
    '''This function ingest the DataFrame into database table'''
    df.to_sql(table_name, con = engine, if_exists="replace", index=False)

def load_raw_data():
    '''This function will load csv as DataFrame and ingest into database'''
    start = time.time()
    for file in os.listdir('data'):
        if '.csv' in file:        
            df = pd.read_csv('data/'+file)
            logging.info(f'Ingesting {file} in db')
            ingest_db(df,"customer_shopping", engine)
    end = time.time()
    total_time = (end - start)/60
    logging.info('------------Ingestion Completed-------------')
    logging.info(f'Total time taken: {total_time} minutes')
    
if __name__ == '__main__':
    load_raw_data()