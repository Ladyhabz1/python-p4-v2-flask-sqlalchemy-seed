#!/usr/bin/env python3
# server/seed.py

from random import choice as rc
from faker import Faker
from app import app
from models import db, Pet

with app.app_context():
    fake = Faker()

    # Delete all existing rows
    Pet.query.delete()

    # List of species
    species = ['Dog', 'Cat', 'Chicken', 'Hamster', 'Turtle']

    # Create and insert 10 random pets
    pets = [Pet(name=fake.first_name(), species=rc(species)) for _ in range(10)]
    
    db.session.add_all(pets)
    db.session.commit()

    print("Database seeded successfully!")
