from src.models.user import db

class Reservation(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    client_name = db.Column(db.String(100), nullable=False)
    phone = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), nullable=True)
    appointment_date = db.Column(db.Date, nullable=False)
    appointment_time = db.Column(db.Time, nullable=False)
    total_amount = db.Column(db.Float, nullable=False, default=0.0)
    payment_method = db.Column(db.String(20), nullable=True)  # 'tarjeta' o 'efectivo'
    status = db.Column(db.String(20), nullable=False, default='pendiente')  # 'pendiente', 'completado', 'cancelado'
    specialist_id = db.Column(db.String(50), db.ForeignKey('specialist.id'), nullable=True)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    # Relación con especialista
    specialist = db.relationship('Specialist', backref='reservations')

    def __repr__(self):
        return f'<Reservation {self.client_name} - {self.appointment_date}>'

    def to_dict(self):
        return {
            'id': self.id,
            'client_name': self.client_name,
            'phone': self.phone,
            'email': self.email,
            'appointment_date': self.appointment_date.isoformat() if self.appointment_date else None,
            'appointment_time': self.appointment_time.isoformat() if self.appointment_time else None,
            'total_amount': self.total_amount,
            'payment_method': self.payment_method,
            'status': self.status,
            'specialist_id': self.specialist_id,
            'specialist_name': self.specialist.name if self.specialist else None,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

class ReservationService(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    reservation_id = db.Column(db.Integer, db.ForeignKey('reservation.id'), nullable=False)
    service_id = db.Column(db.Integer, db.ForeignKey('service.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False, default=1)
    price_at_time = db.Column(db.Float, nullable=False)  # Precio del servicio al momento de la reserva

    # Relaciones
    reservation = db.relationship('Reservation', backref='services')
    service = db.relationship('Service', backref='reservations')

    def __repr__(self):
        return f'<ReservationService {self.reservation_id} - {self.service_id}>'

    def to_dict(self):
        return {
            'id': self.id,
            'reservation_id': self.reservation_id,
            'service_id': self.service_id,
            'service_name': self.service.name if self.service else None,
            'quantity': self.quantity,
            'price_at_time': self.price_at_time,
            'subtotal': self.quantity * self.price_at_time
        }

