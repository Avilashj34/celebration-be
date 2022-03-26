from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


SQLALCHEMY_DATABASE_URL = 'postgresql://agovbrlpaolnwv:6a3d860df7072c845c70e3981e02fa37de330f9cfc445603f4f7331ae5b655e6@ec2-63-32-248-14.eu-west-1.compute.amazonaws.com:5432/davc3lnsnrou92'
# 'postgresql://apirodbusr:"+Fnk9au@localhost:8000/apirodb'

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

