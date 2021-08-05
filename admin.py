import json
class Admin:    
    name=""
    level=0
    def __init__(self,name,level):
        self.name = name       
        self.level = level

class AdminEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Admin):
            return obj.__dict__
        return json.JSONEncoder.default(self, obj)