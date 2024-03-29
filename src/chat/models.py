from database import Base
from sqlalchemy import Integer, String, Column

class Message(Base):
    __tablename__ = "message"
    id = Column(Integer, primary_key=True)
    message = Column(String)

    def as_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}