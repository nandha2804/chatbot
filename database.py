from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# MySQL Workbench Connection String
DATABASE_URL = "mysql+pymysql://root:12345@localhost:3306/chatbot_db"

# Create Engine
engine = create_engine(DATABASE_URL, echo=True, pool_pre_ping=True)

# Session Maker
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base Class
Base = declarative_base()

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
