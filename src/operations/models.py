from sqlalchemy import Column, Integer, String, TIMESTAMP, Table
from sqlalchemy import MetaData 
from datetime import datetime
from database import Base
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable 

class Operations(SQLAlchemyBaseUserTable[int], Base):
    __tablename__ = "operation"
    id = Column(Integer, primary_key=True)
    quantity = Column(String),
    figi = Column(String),
    instrument_type = Column(String, nullable=True),
    date = Column(TIMESTAMP, default=datetime.utcnow),
    type = Column(String),

metadata = MetaData()

operation = Table(
    "operation", 
    metadata, 
    Column("id",Integer, primary_key=True),
    Column("quantity",String),
    Column("figi",String),
    Column("instrument_type",String, nullable=True),
    Column("date",TIMESTAMP, default=datetime.utcnow),
    Column("type",String),
)