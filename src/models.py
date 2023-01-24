import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__="user"
    id = Column(Integer, primary_key=True)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(80), unique=False, nullable=False)

    def __repr__(self):
        return '<User %r>' % self.email

    def serialize(self):
        return {
            "id": self.id,
            "email": self.email,
            # do not serialize the password, its a security breach
        }

class Planet(Base):
    __tablename__="planet"
    id = Column(Integer, primary_key=True)
    name = Column(String(120),nullable=False)
    diameter = Column(Integer(),nullable=False)
    rotation_period = Column(Integer())
    orbital_period = Column(Integer())
    gravity = Column(Integer(),nullable=False)
    population = Column(Integer())
    climate = Column(String(120),nullable=False)
    terrain = Column(String(120),nullable=False)
    surface_water = Column(Integer())
    # residents = done by Table "Residents"
    # films array = done by Table "Location"
    url = Column(String(120),nullable=False)
    created = Column(Integer(),nullable=False)
    edited = Column(Integer(),nullable=False)
    created_by_id=Column(Integer,ForeignKey("user.id",ondelete="cascade"))
    created_by=relationship(User, cascade="all, delete", passive_deletes=True)
    

    def __repr__(self):
        return '<Planet %r>' % self.name
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "diameter": self.diameter,
            "rotation_period": self.rotation_period,
            "orbital_period": self.orbital_period,
            "gravity": self.gravity,
            "population": self.population,
            "climate": self.climate,
            "terrain": self.terrain,
            "surface_water": self.surface_water,
            "created": self.created,
            "edited": self.edited
        }
    def serialize_simple(self):
        return {
            "id": self.id,
            "name": self.name,
        }

class Specie(Base):
    __tablename__="specie"
    id = Column(Integer, primary_key=True)
    name = Column(String(120),nullable=False)
    classification = Column(String(120),nullable=False)
    designation = Column(String(120),nullable=False)
    average_height = Column(String(120),nullable=False)
    average_lifespan = Column(String(120),nullable=False)
    eye_colors = Column(String(120),nullable=False)
    hair_colors = Column(String(120),nullable=False)
    skin_colors = Column(String(120),nullable=False)
    language = Column(String(120),nullable=False)
    homeworld_by_id = Column(Integer(),ForeignKey("planet.id",ondelete="cascade"))
    homeworld = relationship(Planet,cascade="all, delete", passive_deletes=True)
    # people array = done by table "Members_specie"
    # films array = done by table "specie_filmography"
    url = Column(String(120),nullable=False)
    created = Column(Integer(),nullable=False)
    edited = Column(Integer(),nullable=False)

    def __repr__(self):
        return '<Specie %r>' % self.name
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "classification" : self.classification,
            "designation" : self.designation,
            "average_height" : self.average_height,
            "average_lifespan" : self.average_lifespan,
            "eye_colors" : self.eye_colors,
            "hair_colors" : self.hair_colors,
            "skin_colors" : self.skin_colors,
            "language" : self.language,
            "homeworld" : self.homeworld.name,
            "url" : self.url,
            "created" : self.created,
            "edited" : self.edited
        }
    def serialize_simple(self):
        return {
            "id": self.id,
            "name": self.name,
        }

class People(Base):
    __tablename__="people"
    id = Column(Integer, primary_key=True)
    name = Column(String(120),nullable=False)
    birth_year = Column(String(120),nullable=False)
    eye_color = Column(String(120),nullable=False)
    gender = Column(String(120),nullable=False)
    hair_color = Column(String(120),nullable=False)
    height = Column(Integer())
    mass = Column(Integer())
    skin_color = Column(String(120),nullable=False)
    homeworld_by_id = Column(Integer, ForeignKey("planet.id",ondelete="cascade"))
    homeworld = relationship(Planet,cascade="all, delete", passive_deletes=True)
    # films - done by Table "Filmography"
    specie_id = Column(Integer,ForeignKey("specie.id",ondelete="cascade"))
    specie = relationship(Specie, cascade="all, delete", passive_deletes=True)
    # starships - done by table "Reg_starship"
    # vehicles - done by table "Reg_vehicle"
    url = Column(String(120),nullable=False)
    created = Column(Integer(),nullable=False)
    edited = Column(Integer(),nullable=False)
    

    def __repr__(self):
        return '<Character %r>' % self.name
    
    def serialize(self):
        return {
            "id": self.id,
            "name" : self.name,
            "birth_year" : self.birth_year,
            "eye_color" : self.eye_color,
            "gender" : self.gender,
            "hair_color" : self.hair_color,
            "height" : self.height,
            "mass" : self.mass,
            "skin_color" : self.skin_color,
            "homeworld" : self.homeworld.name,
            "specie" : self.specie.name,
            "url" : self.url,
            "created" : self.created,
            "edited" : self.edited
        }
    
    def serialize_simple(self):
        return {
            "id": self.id,
            "name": self.name
        }

class Film(Base):
    __tablename__="film"
    id = Column(Integer, primary_key=True)
    title = Column(String(120),nullable=False)
    episode_id = Column(Integer())
    opening_crawl = Column(String(600),nullable=False)
    director = Column(String(120),nullable=False)
    producer = Column(String(120),nullable=False)
    release_date = Column(String(),nullable=False)
    # species array = done by table "Specie_filmography"
    # starships array = done by table "Featuring_starship"
    # vehicles array = done by table "Featuring_vehicle"
    # characters array = done by table "Filmography"
    # planets array = done by table "Location"
    url = Column(String(120),nullable=False)
    created = Column(Integer(),nullable=False)
    edited = Column(Integer(),nullable=False)
    

    def __repr__(self):
        return '<Film %r>' % self.title
    
    def serialize(self):
        return {
            "id": self.id,
            "title" : self.title,
            "episode_id" : self.episode_id,
            "opening_crawl" : self.opening_crawl,
            "director" : self.director,
            "producer" : self.producer,
            "release_date" : self.release_date,
            "url" : self.url,
            "created" : self.created,
            "edited" : self.edited
        }
    def serialize_simple(self):
        return {
            "id": self.id,
            "name": self.title
        }

class Starship(Base):
    __tablename__="starship"
    id = Column(Integer, primary_key=True)
    name = Column(String(120),nullable=False)
    Base = Column(String(120),nullable=False)
    starship_class = Column(String(120),nullable=False)
    manufacturer = Column(String(120),nullable=False)
    cost_in_credits = Column(Integer())
    length = Column(Integer()) #Integer
    crew = Column(String(120),nullable=False)
    passengers = Column(Integer())
    max_atmosphering_speed = Column(Integer())
    hyperdrive_rating = Column(String(120),nullable=False)
    mglt = Column(Integer())
    cargo_capacity = Column(Integer())
    # films array = done by table "Featuring_starship"
    # pilots array = done by table "Reg_starship"
    url = Column(String(120),nullable=False)
    created = Column(Integer(),nullable=False)
    edited = Column(Integer(),nullable=False)
    

    def __repr__(self):
        return '<Starship %r>' % self.name
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "Base" : self.Base,
            "starship_class" : self.starship_class,
            "manufacturer" : self.manufacturer,
            "cost_in_credits" : self.cost_in_credits,
            "length" : self.length,
            "crew" : self.crew,
            "passengers" : self.passengers,
            "max_atmosphering_speed" : self.max_atmosphering_speed,
            "hyperdrive_rating" : self.hyperdrive_rating,
            "mglt" : self.mglt,
            "url" : self.url,
            "created" : self.created,
            "edited" : self.edited,
        }
    def serialize_simple(self):
        return {
            "id": self.id,
            "name": self.name
        }

class Vehicle(Base):
    __tablename__="vehicle"
    id = Column(Integer, primary_key=True)
    name = Column(String(120),nullable=False)
    Base = Column(String(120),nullable=False)
    vehicle_class = Column(String(120),nullable=False)
    manufacturer = Column(String(120),nullable=False)
    length = Column(Integer())
    cost_in_credits = Column(Integer())
    crew = Column(String(120),nullable=False)
    passengers = Column(Integer())
    max_atmosphering_speed = Column(Integer())
    cargo_capacity = Column(Integer())
    # films array = 
    # pilots array = 
    url = Column(String(120),nullable=False)
    created = Column(Integer(),nullable=False)
    edited = Column(Integer(),nullable=False)

    def __repr__(self):
        return '<Vehicle %r>' % self.name
    
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "Base" : self.Base,
            "vehicle_class" : self.vehicle_class,
            "manufacturer" : self.manufacturer,
            "length" : self.length,
            "cost_in_credits" : self.cost_in_credits,
            "crew" : self.crew,
            "passengers" : self.passengers,
            "max_atmosphering_speed" : self.max_atmosphering_speed,
            "cargo_capacity" : self.cargo_capacity,
            "url" : self.url,
            "created" : self.created,
            "edited" : self.edited
        }
    def serialize_simple(self):
        return {
            "id": self.id,
            "name": self.name
        }

class Location(Base):
    __tablename__="location"
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer(),ForeignKey("planet.id",ondelete="cascade"))
    planet = relationship(Planet, cascade="all, delete", passive_deletes=True)
    film_id = Column(Integer(),ForeignKey("film.id",ondelete="cascade"))
    film = relationship(Film,backref="film",lazy=True, cascade="all, delete", passive_deletes=True)

    def __repr__(self):
        return '<Film %r>' % self.film.title
    
    def serialize(self):
        return {
            "film": {
                "id": self.film_id,
                "name": self.film.title
            },
            "planet": {
                "id": self.planet_id,
                "name": self.planet.name
            }
        }
    
    def serialize_movies(self):
        return self.film.serialize_simple()

    def serialize_planet(self):
        return self.planet.serialize_simple()

class Resident(Base):
    __tablename__="resident"
    id = Column(Integer, primary_key=True)
    planet_id = Column(Integer(),ForeignKey("planet.id",ondelete="cascade"))
    planet = relationship(Planet, cascade="all, delete", passive_deletes=True)
    people_id = Column(Integer(),ForeignKey("people.id",ondelete="cascade"))
    people = relationship(People,backref="resident",lazy=True, cascade="all, delete", passive_deletes=True)

    def __repr__(self):
        return '<Resident %r>' % self.people.name
    
    def serialize(self):
        return self.people.serialize_simple()

class Filmography(Base):
    __tablename__="filmography"
    id = Column(Integer, primary_key=True)
    film_id = Column(Integer(),ForeignKey("film.id"))
    film = relationship(Film, cascade="all, delete", passive_deletes=True)
    people_id = Column(Integer(),ForeignKey("people.id",ondelete="cascade"))
    people = relationship(People,backref="filmography",lazy=True, cascade="all, delete", passive_deletes=True)

    def __repr__(self):
        return '<Filmography %r>' % self.film.title
    
    def serialize(self):
        return self.film.serialize_simple()
    def serialize_character(self):
        return self.people.serialize_simple()

class Reg_starship(Base):
    __tablename__="reg_starship"
    id = Column(Integer, primary_key=True)
    starship_id = Column(Integer(),ForeignKey("starship.id",ondelete="cascade"))
    starship = relationship(Starship, cascade="all, delete", passive_deletes=True)
    people_id = Column(Integer(),ForeignKey("people.id",ondelete="cascade"))
    people = relationship(People,backref="reg_starship",lazy=True, cascade="all, delete", passive_deletes=True)

    def __repr__(self):
        return '<Starship %r>' % self.starship.name
    
    def serialize(self):
        return self.starship.serialize_simple()
    def serialize_pilot(self):
        return self.people.serialize_simple()

class Reg_vehicles(Base):
    __tablename__="reg_vehicle"
    id = Column(Integer, primary_key=True)
    vehicle_id = Column(Integer(),ForeignKey("vehicle.id",ondelete="cascade"))
    vehicle = relationship(Vehicle, cascade="all, delete", passive_deletes=True)
    people_id = Column(Integer(),ForeignKey("people.id",ondelete="cascade"))
    people = relationship(People,backref="reg_vehicle",lazy=True, cascade="all, delete", passive_deletes=True)

    def __repr__(self):
        return '<Vehicle %r>' % self.vehicle.name
    
    def serialize(self):
        return self.vehicle.serialize_simple()
    def serialize_pilot(self):
        return self.people.serialize_simple()

class Members_specie(Base):
    __tablename__="members_specie"
    id = Column(Integer, primary_key=True)
    specie_id = Column(Integer(),ForeignKey("specie.id",ondelete="cascade"))
    specie = relationship(Specie, cascade="all, delete", passive_deletes=True)
    people_id = Column(Integer(),ForeignKey("people.id",ondelete="cascade"))
    people = relationship(People,backref="members_specie",lazy=True, cascade="all, delete", passive_deletes=True)

    def __repr__(self):
        return '<Specie %r>' % self.specie.name
    
    def serialize(self):
        return self.people.serialize_simple()

class Specie_filmography(Base):
    __tablename__="specie_filmography"
    id = Column(Integer, primary_key=True)
    specie_id = Column(Integer(),ForeignKey("specie.id",ondelete="cascade"))
    specie = relationship(Specie, cascade="all, delete", passive_deletes=True)
    film_id = Column(Integer(),ForeignKey("film.id",ondelete="cascade"))
    film = relationship(Film,backref="specie_filmography",lazy=True, cascade="all, delete", passive_deletes=True)

    def __repr__(self):
        return '<Film %r>' % self.film.title
    
    def serialize(self):
        return self.film.serialize_simple()
    def serialize_specie(self):
        return self.specie.serialize_simple()

class Featuring_starship(Base):
    __tablename__="featuring_starship"
    id = Column(Integer, primary_key=True)
    starship_id = Column(Integer(),ForeignKey("starship.id",ondelete="cascade"))
    starship = relationship(Starship, cascade="all, delete", passive_deletes=True)
    film_id = Column(Integer(),ForeignKey("film.id",ondelete="cascade"))
    film = relationship(Film,backref="featuring_starship",lazy=True, cascade="all, delete", passive_deletes=True)

    def __repr__(self):
        return '<Film %r>' % self.film.title
    
    def serialize_starship(self):
        return self.starship.serialize_simple()
    def serialize_film(self):
        return self.film.serialize_simple()

class Featuring_vehicle(Base):
    __tablename__="featuring_vehicle"
    id = Column(Integer, primary_key=True)
    vehicle_id = Column(Integer(),ForeignKey("vehicle.id",ondelete="cascade"))
    vehicle = relationship(Vehicle, cascade="all, delete", passive_deletes=True)
    film_id = Column(Integer(),ForeignKey("film.id",ondelete="cascade"))
    film = relationship(Film,backref="featuring_vehicle",lazy=True, cascade="all, delete", passive_deletes=True)

    def __repr__(self):
        return '<Film %r>' % self.film.title
    
    def serialize_vehicle(self):
        return self.vehicle.serialize_simple()
    def serialize_film(self):
        return self.film.serialize_simple()

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')
