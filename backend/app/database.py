from sqlalchemy import create_engine

from sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://root:root@mysql:3306/mydatabase"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
