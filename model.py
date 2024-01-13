from datetime import datetime
from sqlalchemy import Boolean, Column, Integer, String, DateTime, func
from db import Base

class Log(Base):
    __tablename__ = "logs"
    id = Column(Integer, primary_key=True, index=True)
    
    timestamp = Column(DateTime, default=datetime.utcnow,server_default=func.now())
    request = Column(String(255))
    print(request)
    response = Column(String(255))
    turnaround_time = Column(Integer)