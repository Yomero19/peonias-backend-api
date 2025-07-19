from flask import Blueprint, request, jsonify
from src.models.user import db
from src.models.service import Service

services_bp = Blueprint('services', __name__)

@services_bp.route('/services', methods=['GET'])
def get_services():
    try:
        services = Service.query.all()
        return jsonify([service.to_dict() for service in services])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@services_bp.route('/services/<int:service_id>', methods=['GET'])
def get_service(service_id):
    try:
        service = Service.query.get_or_404(service_id)
        return jsonify(service.to_dict())
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@services_bp.route('/services', methods=['POST'])
def create_service():
    try:
        data = request.get_json()
        
        service = Service(
            name=data['name'],
            price=float(data['price']),
            category=data.get('category', '')
        )
        
        db.session.add(service)
        db.session.commit()
        
        return jsonify(service.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@services_bp.route('/services/<int:service_id>', methods=['PUT'])
def update_service(service_id):
    try:
        service = Service.query.get_or_404(service_id)
        data = request.get_json()
        
        service.name = data.get('name', service.name)
        service.price = float(data.get('price', service.price))
        service.category = data.get('category', service.category)
        
        db.session.commit()
        
        return jsonify(service.to_dict())
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@services_bp.route('/services/<int:service_id>', methods=['DELETE'])
def delete_service(service_id):
    try:
        service = Service.query.get_or_404(service_id)
        db.session.delete(service)
        db.session.commit()
        
        return jsonify({'message': 'Servicio eliminado exitosamente'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@services_bp.route('/services/category/<category>', methods=['GET'])
def get_services_by_category(category):
    try:
        services = Service.query.filter_by(category=category).all()
        return jsonify([service.to_dict() for service in services])
    except Exception as e:
        return jsonify({'error': str(e)}), 500

