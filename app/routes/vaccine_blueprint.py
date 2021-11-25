from flask import Blueprint, request, current_app, jsonify
from app.models.vaccine_exceptions import CPFError, CPFExistsError, DataTypeError, InvalidKeyError
from app.models.vaccine_model import Vaccine
from datetime import datetime, timedelta

bp = Blueprint('vaccine_card', __name__, url_prefix='/api')

@bp.post('/vaccination')
def create():
    data = request.get_json()
    correct_keys = ['cpf', 'name', 'vaccine_name', 'health_unit_name']
    full_table = Vaccine.query.all()
    
    CPF_table = []
    for item in full_table:
        CPF_table.append(item.cpf)
        
            
    
    try:  
        for item in data.values():
            if type(item) is not str:
                raise DataTypeError()
            
        for item in list(data.keys()):
            if item not in correct_keys:
                data.pop(item) # REMOVE KEYS ADICIONAIS
                    
        for item in correct_keys:
            if item not in list(data.keys()):
                raise InvalidKeyError()
                    
        if len(data['cpf']) != 11:
            raise CPFError()
        
        if data['cpf'] in CPF_table:
            raise CPFExistsError()
        

        add_vaccine = Vaccine(
            cpf=data['cpf'],
            name=data['name'],
            vaccine_name=data['vaccine_name'],
            health_unit_name=data['health_unit_name'],
            first_shot_date=datetime.now(),
            second_shot_date=datetime.now() + timedelta(90)
        )
        
        session = current_app.db.session
        session.add(add_vaccine)
        session.commit()

        return jsonify(add_vaccine), 201
    
    except CPFError as err:
        return err.message
    
    except CPFExistsError as err:
        return err.message
    
    except DataTypeError as err:
        return err.message
    
    except InvalidKeyError as err:
        return err.message


@bp.get('/vaccination')
def get_vaccines():
    query = Vaccine.query.all()

    return jsonify(query), 200
