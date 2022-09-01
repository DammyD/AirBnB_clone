#!/usr/bin/python3
""" 
this is the base model that all common attributes/methods 
for other classes
"""

import uuid
import datetime


class BaseModel:

    """ the base model"""
    def __init__(self):
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()
        
