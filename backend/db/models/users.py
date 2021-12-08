from sqlalchemy import Column, Date, String, Boolean, Integer, ForeignKey
from sqlalchemy.orm import relationship

from db.base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String,unique=True, nullable=False, index=True)
    hashed_password = Column(String,nullable=False)
    is_active = Column(Boolean(), default=True)
    is_admin = Column(Boolean(), default=False)
    jobs = relationship("Job", back_populates="owner")