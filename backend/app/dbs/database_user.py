"""from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base"""
from app.settings.setting import DATABASE_URL

"""engine=create_engine(DATABASE_URL)
SessionLocal=sessionmaker(bind=engine,autocommit=False,autoflush=False)
Base=declarative_base()
"""

print(DATABASE_URL)