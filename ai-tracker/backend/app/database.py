from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

PASSWORD = "k5Y.7BUQV%2C%40%2BbC8"
DATABASE_URL = "postgresql://postgres.xlzqhpwbgwdfauiohbjm:"+PASSWORD+"@aws-1-ap-northeast-1.pooler.supabase.com:6543/postgres"


engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()





