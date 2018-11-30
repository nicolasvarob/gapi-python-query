import pandas as pd
from sqlalchemy import create_engine

from secret.private import POSTGRES_ENGINE

def create_funnel(df):
    df['ga:date'] = pd.to_datetime(df['ga:date'])
    engine = create_engine(POSTGRES_ENGINE)

    df.to_sql('test', engine)

    
