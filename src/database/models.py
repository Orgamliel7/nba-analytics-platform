from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class Team(Base):
    __tablename__ = "teams"
    
    team_id = Column(Integer, primary_key=True)
    team_name = Column(String(100))
    city = Column(String(100))
    conference = Column(String(50))
    division = Column(String(50))

class Player(Base):
    __tablename__ = "players"
    
    player_id = Column(Integer, primary_key=True)
    team_id = Column(Integer, ForeignKey('teams.team_id'))
    first_name = Column(String(50))
    last_name = Column(String(50))
    position = Column(String(10))
    jersey_number = Column(Integer)