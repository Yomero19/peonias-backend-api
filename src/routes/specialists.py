from flask import Blueprint, request, jsonify
from src.models.user import db
from src.models.specialist import Specialist

specialists_bp = Blueprint('specialists', __name__)

@specialists_bp.route('/specialists', methods=['GET'])
def get_specialists():
    try:
        specialists = Specialist.query.all()
        return jsonify([specialist.to_dict() for specialist in specialists])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@specialists_bp.route('/specialists', methods=['POST'])
def create_specialist():
    try:
        data = request.get_json()
        
        # Verificar si ya existe un especialista con ese ID
        existing = Specialist.query.filter_by(id=data['id']).first()
        if existing:
            return jsonify({'error': 'Ya existe un especialista con ese ID'}), 400
        
        specialist = Specialist(
            id=data['id'],
            name=data['name'],
            specialty=data['specialty']
        )
        
        db.session.add(specialist)
        db.session.commit()
        
        return jsonify(specialist.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@specialists_bp.route('/specialists/<specialist_id>', methods=['PUT'])
def update_specialist(specialist_id):
    try:
        specialist = Specialist.query.get_or_404(specialist_id)
        data = request.get_json()
        
        specialist.name = data.get('name', specialist.name)
        specialist.specialty = data.get('specialty', specialist.specialty)
        
        db.session.commit()
        
        return jsonify(specialist.to_dict())
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@specialists_bp.route('/specialists/<specialist_id>', methods=['DELETE'])
def delete_specialist(specialist_id):
    try:
        specialist = Specialist.query.get_or_404(specialist_id)
        db.session.delete(specialist)
        db.session.commit()
        
        return jsonify({'message': 'Especialista eliminado exitosamente'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

