class PhoneExistsError(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.message = {
            "error": "Phone already exists."
        }, 409  

class EmailExistsError(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.message = {
            "error": "Email already exists."
        }, 409  
        
class EmailNotExistsError(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.message = {
            "error": "Email does not exist."
        }, 409         
        
class DataTypeError(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.message = {
            "error": "Key values must be string."
        }, 400          
        
class InvalidKeyError(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.message = {
            "error": "Invalid key.", 'correct_keys': ['name', 'email', 'phone']
        }, 400           
        
class NotEmailError(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.message = {
            "error": "Invalid key. Only 'email' allowed." 
            }, 400              