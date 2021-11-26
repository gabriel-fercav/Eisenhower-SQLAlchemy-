from flask import Blueprint, request, current_app, jsonify
from app.models.leads_exceptions import PhoneExistsError, NotEmailError, EmailExistsError, EmailNotExistsError, DataTypeError, InvalidKeyError
from app.models.leads_model import Leads
from datetime import datetime, timedelta

bp = Blueprint('leads_card', __name__, url_prefix='/api')

@bp.post('/leads')
def create():
    data = request.get_json()
    correct_keys = ['name', 'email', 'phone']
    full_table = Leads.query.all()
    
    email_table = []
    for item in full_table:
        email_table.append(item.email)
        
    phone_table = []
    for item in full_table:
        phone_table.append(item.phone)    
        
    try:  
        for item in data.values():
            if type(item) is not str:
                raise DataTypeError() # VERIFICA SE TUDO É STRING
            
        for item in list(data.keys()):
            if item not in correct_keys:
                data.pop(item) # REMOVE KEYS ADICIONAIS
                    
        for item in correct_keys:
            if item not in list(data.keys()):
                raise InvalidKeyError() # VERIFICA SE EXISTEM KEYS INVÁLIDAS SOBRANDO
                    
        if data['phone'] in phone_table:
            raise PhoneExistsError() # VERIFICA SE TELEFONE É ÚNICO
        
        if data['email'] in email_table:
            raise EmailExistsError() # VERIFICA SE E-MAIL É ÚNICO

        add_lead = Leads(
                **data,
                creation_date = datetime.now(),
                last_visit = datetime.now(),
                visits = 1
        )
        
        session = current_app.db.session
        session.add(add_lead)
        session.commit()

        return jsonify(add_lead), 201
    
    except PhoneExistsError as err:
        return err.message
    
    except EmailExistsError as err:
        return err.message
    
    except DataTypeError as err:
        return err.message
    
    except InvalidKeyError as err:
        return err.message


@bp.get('/leads')
def get():
    query = Leads.query.all()

    return jsonify(query), 200

@bp.delete('/leads')
def delete():
    data = request.get_json()
    
    try:
        if len(data.keys()) > 1:
            raise NotEmailError
        
        if 'email' not in list(data.keys()):
            raise NotEmailError 
         
        query = Leads.query.filter_by(email = data['email']).delete()
        
        if query == 0:
            return "", 404
        
        current_app.db.session.commit()

        return "", 204
    
    except NotEmailError as err:
        return err.message
    
@bp.patch('/leads')    
def update():
    data = request.get_json()
    full_table = Leads.query.all()
    
    email_table = []
    for item in full_table:
        email_table.append(item.email)

    try:
        
        if data.keys() != 'email':
            return { 'error': 'Only email allowed.' }, 400
        
        if data['email'] not in email_table:
            raise EmailNotExistsError()

        lead = Leads.query.filter_by(email = data['email']).first()
        
        lead.visits += 1
        lead.last_visit = datetime.now()
        session = current_app.db.session
        session.add(lead)
        session.commit()

        return jsonify(lead), 200

    except InvalidKeyError as err:
        return err.message
    
    except EmailNotExistsError as err:
        return err.message
