class CPFError(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.message = {
            "error": "CPF should be composed of 11 digits."
        }, 400   

class CPFExistsError(Exception):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.message = {
            "error": "CPF already exists."
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
            "error": "Invalid key.", 'correct_keys': ['cpf', 'name', 'vaccine_name', 'health_unit_name']
        }, 400           
        