import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Table, create_engine, Float
from sqlalchemy.orm import relationship, declarative_base
from eralchemy2 import render_er

Base = declarative_base()

# Association Tables
films_characters = Table('films_characters', Base.metadata,
    Column('film_id', Integer, ForeignKey('films.id'), primary_key=True),
    Column('character_id', Integer, ForeignKey('characters.id'), primary_key=True)
)

films_planets = Table('films_planets', Base.metadata,
    Column('film_id', Integer, ForeignKey('films.id'), primary_key=True),
    Column('planet_id', Integer, ForeignKey('planets.id'), primary_key=True)
)

films_starships = Table('films_starships', Base.metadata,
    Column('film_id', Integer, ForeignKey('films.id'), primary_key=True),
    Column('starship_id', Integer, ForeignKey('starships.id'), primary_key=True)
)

films_species = Table('films_species', Base.metadata,
    Column('film_id', Integer, ForeignKey('films.id'), primary_key=True),
    Column('species_id', Integer, ForeignKey('species.id'), primary_key=True)
)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    nick_name = Column(String(250), nullable=False, unique=True)
    first_name = Column(String(250))
    last_name = Column(String(250))
    email = Column(String(250), nullable=False, unique=True)
    password = Column(String(250), nullable=False)
    liked_items = relationship("Liked", back_populates="user")

class Planets(Base):
    __tablename__ = 'planets'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    diameter = Column(Float)
    rotation_period = Column(Integer)
    orbital_period = Column(Integer)
    gravity = Column(String(250))
    population = Column(Integer)
    climate = Column(String(250))
    terrain = Column(String(250))
    surface_water = Column(Integer)
    films = relationship("Films", secondary=films_planets, back_populates="planets")
    liked_items = relationship("Liked", back_populates="planet")

class Starships(Base):
    __tablename__ = 'starships'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    starship_class = Column(String(250))
    manufacturer = Column(String(250))
    cost_in_credits = Column(String(250))
    length = Column(String(250))
    crew = Column(String(250))
    passengers = Column(String(250))
    max_atmosphering_speed = Column(Integer)
    hyperdrive_rating = Column(String(250))
    MGLT = Column(String(250))
    cargo_capacity = Column(String(250))
    consumables = Column(String(250))
    pilots = Column(String(250))
    films = relationship("Films", secondary=films_starships, back_populates="starships")
    liked_items = relationship("Liked", back_populates="starship")

class Characters(Base):
    __tablename__ = 'characters'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    height = Column(String(250))
    mass = Column(String(250))
    hair_color = Column(String(250))
    skin_color = Column(String(250))
    eye_color = Column(String(250))
    birth_year = Column(String(250))
    gender = Column(String(250))
    homeworld = Column(String(250))
    force_side = Column(String(250))
    films = relationship("Films", secondary=films_characters, back_populates="characters")
    liked_items = relationship("Liked", back_populates="character")

class Species(Base):
    __tablename__ = 'species'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    classification = Column(String(250))
    designation = Column(String(250))
    average_height = Column(String(250))
    average_lifespan = Column(String(250))
    hair_colors = Column(String(250))
    skin_colors = Column(String(250))
    eye_colors = Column(String(250))
    homeworld = Column(String(250))
    language = Column(String(250))
    films = relationship("Films", secondary=films_species, back_populates="species")
    liked_items = relationship("Liked", back_populates="species")

class Films(Base):
    __tablename__ = 'films'
    id = Column(Integer, primary_key=True)
    title = Column(String(250), nullable=False)
    episode_num = Column(Integer)
    release_date = Column(Integer)
    director = Column(String(250))

    characters = relationship('Characters', secondary=films_characters, back_populates='films')
    planets = relationship('Planets', secondary=films_planets, back_populates='films')
    starships = relationship('Starships', secondary=films_starships, back_populates='films')
    species = relationship('Species', secondary=films_species, back_populates='films')

class Liked(Base):
    __tablename__ = 'liked'
    user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
    item_id = Column(Integer, primary_key=True)
    item_type = Column(String(50))  

    character_id = Column(Integer, ForeignKey('characters.id'))
    planet_id = Column(Integer, ForeignKey('planets.id'))
    starship_id = Column(Integer, ForeignKey('starships.id'))
    species_id = Column(Integer, ForeignKey('species.id'))

    user = relationship('User', back_populates="liked_items")
    character = relationship('Characters', back_populates="liked_items")
    planet = relationship('Planets', back_populates="liked_items")
    starship = relationship('Starships', back_populates="liked_items")
    species = relationship('Species', back_populates="liked_items")


## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print(" :( ")
    raise e