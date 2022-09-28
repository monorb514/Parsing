from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy import Column, Integer, String

from decouple import config

Base = declarative_base()
engine = create_engine(config('URL'), echo=True)
