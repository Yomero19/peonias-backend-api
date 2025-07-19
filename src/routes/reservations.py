from flask import Blueprint, request, jsonify
from datetime import datetime, date, time
from src.models.user import db
from src.models.reservation import Reservation, ReservationService
from src.models.service import Service

reservations_bp = Blueprint('reservations', __name__)

@reservations_bp.route('/reservations', methods=['GET'])
def get_reservations():
    try:
        # Obtener parámetros de filtro
        date_filter = request.args.get('date')
        
        query = Reservation.query
        
        if date_filter:
            query = query.filter(Reservation.appointment_date == date_filter)
        
        reservations = query.order_by(Reservation.appointment_date.desc(), Reservation.appointment_time.desc()).all()
        
        # Incluir servicios en cada reserva
        result = []
        for reservation in reservations:
            reservation_dict = reservation.to_dict()
            
            # Obtener servicios de la reserva
            reservation_services = ReservationService.query.filter_by(reservation_id=reservation.id).all()
            reservation_dict['services'] = [rs.to_dict() for rs in reservation_services]
            
            result.append(reservation_dict)
        
        return jsonify(result)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@reservations_bp.route('/reservations/<int:reservation_id>', methods=['GET'])
def get_reservation(reservation_id):
    try:
        reservation = Reservation.query.get_or_404(reservation_id)
        reservation_dict = reservation.to_dict()
        
        # Obtener servicios de la reserva
        reservation_services = ReservationService.query.filter_by(reservation_id=reservation.id).all()
        reservation_dict['services'] = [rs.to_dict() for rs in reservation_services]
        
        return jsonify(reservation_dict)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@reservations_bp.route('/reservations', methods=['POST'])
def create_reservation():
    try:
        data = request.get_json()
        
        # Crear la reserva
        reservation = Reservation(
            client_name=data['client_name'],
            phone=data['phone'],
            email=data.get('email', ''),
            appointment_date=datetime.strptime(data['appointment_date'], '%Y-%m-%d').date(),
            appointment_time=datetime.strptime(data['appointment_time'], '%H:%M').time(),
            total_amount=float(data['total_amount']),
            specialist_id=data.get('specialist_id')
        )
        
        db.session.add(reservation)
        db.session.flush()  # Para obtener el ID de la reserva
        
        # Agregar servicios a la reserva
        total_amount = 0
        for service_id in data['services']:
            service = Service.query.get(service_id)
            if service:
                reservation_service = ReservationService(
                    reservation_id=reservation.id,
                    service_id=service_id,
                    quantity=1,
                    price_at_time=service.price
                )
                db.session.add(reservation_service)
                total_amount += service.price
        
        # Actualizar el total
        reservation.total_amount = total_amount
        
        db.session.commit()
        
        return jsonify(reservation.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@reservations_bp.route('/reservations/<int:reservation_id>', methods=['PUT'])
def update_reservation(reservation_id):
    try:
        reservation = Reservation.query.get_or_404(reservation_id)
        data = request.get_json()
        
        reservation.client_name = data.get('client_name', reservation.client_name)
        reservation.phone = data.get('phone', reservation.phone)
        reservation.email = data.get('email', reservation.email)
        
        if 'appointment_date' in data:
            reservation.appointment_date = datetime.strptime(data['appointment_date'], '%Y-%m-%d').date()
        
        if 'appointment_time' in data:
            reservation.appointment_time = datetime.strptime(data['appointment_time'], '%H:%M').time()
        
        reservation.specialist_id = data.get('specialist_id', reservation.specialist_id)
        reservation.status = data.get('status', reservation.status)
        
        db.session.commit()
        
        return jsonify(reservation.to_dict())
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@reservations_bp.route('/reservations/<int:reservation_id>/payment', methods=['POST'])
def process_payment(reservation_id):
    try:
        reservation = Reservation.query.get_or_404(reservation_id)
        data = request.get_json()
        
        reservation.payment_method = data['payment_method']
        reservation.status = data.get('status', 'completado')
        
        db.session.commit()
        
        return jsonify(reservation.to_dict())
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@reservations_bp.route('/reservations/<int:reservation_id>/services', methods=['POST'])
def add_service_to_reservation(reservation_id):
    try:
        reservation = Reservation.query.get_or_404(reservation_id)
        data = request.get_json()
        
        service = Service.query.get_or_404(data['service_id'])
        
        reservation_service = ReservationService(
            reservation_id=reservation_id,
            service_id=data['service_id'],
            quantity=data.get('quantity', 1),
            price_at_time=service.price
        )
        
        db.session.add(reservation_service)
        
        # Actualizar el total de la reserva
        reservation.total_amount += service.price * data.get('quantity', 1)
        
        db.session.commit()
        
        return jsonify(reservation_service.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@reservations_bp.route('/reservations/<int:reservation_id>', methods=['DELETE'])
def delete_reservation(reservation_id):
    try:
        reservation = Reservation.query.get_or_404(reservation_id)
        
        # Eliminar servicios asociados
        ReservationService.query.filter_by(reservation_id=reservation_id).delete()
        
        # Eliminar la reserva
        db.session.delete(reservation)
        db.session.commit()
        
        return jsonify({'message': 'Reserva eliminada exitosamente'})
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

