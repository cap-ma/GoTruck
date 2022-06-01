from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
"""from settings.setting import DATABASE_URL"""

engine=create_engine("postgres://postgres:19832011@localhost/db")
SessionLocal=sessionmaker(bind=engine,autocommit=False,autoflush=False)
Base=declarative_base()


