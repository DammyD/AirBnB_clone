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
		"""
		initialize object with the attributes
		"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.datetime.now()
        self.updated_at = datetime.datetime.now()

    def __str__(self):
        """ the string for instance
		class name, id, dict
		"""
        return "[{}] ({}) {}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute
         updated_at with the current datetime"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """returns a dictionary containing all
        keys/values of __dict__ of the instance:"""
        result = {}
        for key, value in self.__dict__.items():
            if isinstance(value, datetime.datetime):
                result[key] = value.isoformat()
            else:
                result[key] = value
            result[__class__] = self.__class__.__name__

        return result
