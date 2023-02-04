import sqlite3 
from flask import g  #imports global context opject within python but we can't use the word global because that is a python protected word.  g is the abbreviated 

DATABASE_URL = "main.db"  #Look up 3 criteria for constants in python

def get_db():
    db = getattr(g, "_database", None)  #use getattb to get database from g...if not return None.
    if not db:                 #if db=none then...
        db = g._database = sqlite3.connect(DATABASE_URL)  #_database is a g attribute.  This if statement should only allow one or at least fewer open connections to the database at a time.  
    return db