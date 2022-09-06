#!/usr/bin/python3
"""
this is the base model that all common attributes/methods
for other classes
"""

from unittest import result
import uuid
import datetime


class BaseModel:
    """ the base model"""

    def __init__(self, *args, **kwargs):
        """
        initialize object with the attributes

        Args:
            *args (tuple): Ignored.
            kwargs: A dictionary of attribute keys-value pairs.
        """
        if len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "__class__":
                    continue
                if key == 'created_at' or key == 'update_at':
                    value = datetime.datetime.fromisoformat(value)
                setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()

            from models import storage
            storage.new(self)

    def __str__(self):
        """ the string for instance
        class name, id, dict
        """
        return "[{}] ({}) \
{}".format(self.__class__.__name__, self.id, self.__dict__)

    def save(self):
        """updates the public instance attribute
         updated_at with the current datetime"""

        from models import storage
        self.updated_at = datetime.datetime.now()
        storage.save()

    def to_dict(self):
        """returns a dictionary containing all
        keys/values of __dict__ of the instance:"""
        result = {}
        for key, value in self.__dict__.items():
            if isinstance(value, datetime.datetime):
                result[key] = value.isoformat()
            else:
                result[key] = value
            result["__class__"] = self.__class__.__name__

        return result
