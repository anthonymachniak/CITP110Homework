

class petData:
    
    def __init__(self, name, petType, age):
        self.__name = name
        self.__petType = petType
        self.__age = age
        
    def set_name(self, name):
        self.__name = name
        
    def set_pet_type(self, petType):
        self.__petType = petType
        
    def set_age(self, age):
        self.__age = age
        
    def get_name(self):
        return self.__name
    
    def get_pet_type(self):
        return self.__petType
    
    def get_age(self):
        return self.__age
