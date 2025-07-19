from src.models.user import db

class Specialist(db.Model):
    id = db.Column(db.String(50), primary_key=True)  # ID alfanumérico único
    name = db.Column(db.String(100), nullable=False)
    specialty = db.Column(db.String(100), nullable=False)
    created_at = db.Column(db.DateTime, default=db.func.current_timestamp())

    def __repr__(self):
        return f'<Specialist {self.name}>'

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'specialty': self.specialty,
            'created_at': self.created_at.isoformat() if self.created_at else None
        }

