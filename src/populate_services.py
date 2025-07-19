import os
import sys
sys.path.insert(0, os.path.dirname(os.path.dirname(__file__)))

from src.models.user import db
from src.models.service import Service
from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(os.path.dirname(__file__), 'database', 'app.db')}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    return app

def populate_services():
    services_data = [
        # Uñas - Gel
        {"name": "GEL - Aplicación de gel", "price": 180.00, "category": "Uñas"},
        {"name": "GEL - Retiro de gel", "price": 50.00, "category": "Uñas"},
        
        # Uñas - Acrílico
        {"name": "ACRÍLICO - Uñas acrílicas esculturales (#1-3)", "price": 440.00, "category": "Uñas"},
        {"name": "ACRÍLICO - Baño de acrílico (#1-3)", "price": 340.00, "category": "Uñas"},
        {"name": "ACRÍLICO - Retoque de acrílico (#1-3)", "price": 340.00, "category": "Uñas"},
        {"name": "ACRÍLICO - Retiro de acrílico", "price": 120.00, "category": "Uñas"},
        
        # Uñas - Rubber
        {"name": "Rubber base", "price": 200.00, "category": "Uñas"},
        {"name": "Retoque de Rubber", "price": 180.00, "category": "Uñas"},
        {"name": "Rubber + gel", "price": 300.00, "category": "Uñas"},
        {"name": "Retoque de Rubber + gel", "price": 280.00, "category": "Uñas"},
        {"name": "Retiro de Rubber", "price": 60.00, "category": "Uñas"},
        
        # Manicura
        {"name": "Manicure Ruso", "price": 150.00, "category": "Manicura"},
        {"name": "Manicure Ruso + gel", "price": 320.00, "category": "Manicura"},
        {"name": "Mani Spa", "price": 200.00, "category": "Manicura"},
        {"name": "Mani Spa + gel", "price": 350.00, "category": "Manicura"},
        {"name": "Mani Jelly", "price": 260.00, "category": "Manicura"},
        {"name": "Mani Jelly + gel", "price": 410.00, "category": "Manicura"},
        
        # Efectos y diseños
        {"name": "Efecto", "price": 80.00, "category": "Diseños"},
        {"name": "Francés", "price": 80.00, "category": "Diseños"},
        {"name": "Diseño a mano alzada", "price": 150.00, "category": "Diseños"},
        {"name": "Líneas sencillas", "price": 90.00, "category": "Diseños"},
        {"name": "Relieve", "price": 100.00, "category": "Diseños"},
        {"name": "Ojo de gato", "price": 100.00, "category": "Diseños"},
        {"name": "Aplicación de vitabase", "price": 50.00, "category": "Diseños"},
        
        # Extensiones de pestañas - Clásicas
        {"name": "Extensiones Clásicas - Set nuevo", "price": 450.00, "category": "Extensiones de Pestañas"},
        {"name": "Extensiones Clásicas - Retoque (2 semanas)", "price": 300.00, "category": "Extensiones de Pestañas"},
        
        # Extensiones de pestañas - Efecto Rímel
        {"name": "Efecto Rímel - Set nuevo", "price": 500.00, "category": "Extensiones de Pestañas"},
        {"name": "Efecto Rímel - Retoque (2 semanas)", "price": 350.00, "category": "Extensiones de Pestañas"},
        
        # Extensiones de pestañas - Vol Hawaiano
        {"name": "Vol Hawaiano - Set nuevo", "price": 580.00, "category": "Extensiones de Pestañas"},
        {"name": "Vol Hawaiano - Retoque (2 semanas)", "price": 400.00, "category": "Extensiones de Pestañas"},
        
        # Extensiones de pestañas - Vol Griego
        {"name": "Vol Griego - Set nuevo", "price": 600.00, "category": "Extensiones de Pestañas"},
        {"name": "Vol Griego - Retoque (2 semanas)", "price": 400.00, "category": "Extensiones de Pestañas"},
        
        # Depilación Láser - Bozo
        {"name": "DEPILACIÓN LÁSER - Bozo 1 SESIÓN", "price": 249.00, "category": "Depilación Láser"},
        {"name": "DEPILACIÓN LÁSER - Bozo 6 SESIÓN", "price": 1389.00, "category": "Depilación Láser"},
        {"name": "DEPILACIÓN LÁSER - Bozo 8 SESIÓN", "price": 1792.00, "category": "Depilación Láser"},
        {"name": "DEPILACIÓN LÁSER - Bozo 12 SESIÓN", "price": 2539.00, "category": "Depilación Láser"},
        
        # Depilación Láser - Patillas
        {"name": "Patillas - 1 SESIÓN", "price": 299.00, "category": "Depilación Láser"},
        {"name": "Patillas - 6 SESIÓN", "price": 1668.00, "category": "Depilación Láser"},
        {"name": "Patillas - 8 SESIÓN", "price": 2152.00, "category": "Depilación Láser"},
        {"name": "Patillas - 12 SESIÓN", "price": 3049.00, "category": "Depilación Láser"},
        
        # Depilación Láser - Rostro Completo
        {"name": "Rostro Completo - 1 SESIÓN", "price": 499.00, "category": "Depilación Láser"},
        {"name": "Rostro Completo - 6 SESIÓN", "price": 2784.00, "category": "Depilación Láser"},
        {"name": "Rostro Completo - 8 SESIÓN", "price": 3592.00, "category": "Depilación Láser"},
        {"name": "Rostro Completo - 12 SESIÓN", "price": 5089.00, "category": "Depilación Láser"},
        
        # Depilación Láser - Axilas
        {"name": "Axilas - 1 SESIÓN", "price": 349.00, "category": "Depilación Láser"},
        {"name": "Axilas - 6 SESIÓN", "price": 1947.00, "category": "Depilación Láser"},
        {"name": "Axilas - 8 SESIÓN", "price": 2512.00, "category": "Depilación Láser"},
        {"name": "Axilas - 12 SESIÓN", "price": 3559.00, "category": "Depilación Láser"},
        
        # Depilación Láser - Abdomen
        {"name": "Abdomen - 1 SESIÓN", "price": 349.00, "category": "Depilación Láser"},
        {"name": "Abdomen - 6 SESIÓN", "price": 1947.00, "category": "Depilación Láser"},
        {"name": "Abdomen - 8 SESIÓN", "price": 2512.00, "category": "Depilación Láser"},
        {"name": "Abdomen - 12 SESIÓN", "price": 3559.00, "category": "Depilación Láser"},
        
        # Depilación Láser - Brazos
        {"name": "1/2 Brazos - 1 SESIÓN", "price": 349.00, "category": "Depilación Láser"},
        {"name": "1/2 Brazos - 6 SESIÓN", "price": 1947.00, "category": "Depilación Láser"},
        {"name": "1/2 Brazos - 8 SESIÓN", "price": 2512.00, "category": "Depilación Láser"},
        {"name": "1/2 Brazos - 12 SESIÓN", "price": 3559.00, "category": "Depilación Láser"},
        
        {"name": "Brazos completos - 1 SESIÓN", "price": 599.00, "category": "Depilación Láser"},
        {"name": "Brazos completos - 6 SESIÓN", "price": 3342.00, "category": "Depilación Láser"},
        {"name": "Brazos completos - 8 SESIÓN", "price": 4312.00, "category": "Depilación Láser"},
        {"name": "Brazos completos - 12 SESIÓN", "price": 6109.00, "category": "Depilación Láser"},
        
        # Depilación Láser - Piernas
        {"name": "1/2 piernas - 1 SESIÓN", "price": 399.00, "category": "Depilación Láser"},
        {"name": "1/2 piernas - 6 SESIÓN", "price": 2226.00, "category": "Depilación Láser"},
        {"name": "1/2 piernas - 8 SESIÓN", "price": 2872.00, "category": "Depilación Láser"},
        {"name": "1/2 piernas - 12 SESIÓN", "price": 4069.00, "category": "Depilación Láser"},
        
        {"name": "Piernas completas - 1 SESIÓN", "price": 799.00, "category": "Depilación Láser"},
        {"name": "Piernas completas - 6 SESIÓN", "price": 4448.00, "category": "Depilación Láser"},
        {"name": "Piernas completas - 8 SESIÓN", "price": 5752.00, "category": "Depilación Láser"},
        {"name": "Piernas completas - 12 SESIÓN", "price": 8149.00, "category": "Depilación Láser"},
        
        # Depilación Láser - Bikini
        {"name": "Bikini Sencillo - 1 SESIÓN", "price": 349.00, "category": "Depilación Láser"},
        {"name": "Bikini Sencillo - 6 SESIÓN", "price": 1947.00, "category": "Depilación Láser"},
        {"name": "Bikini Sencillo - 8 SESIÓN", "price": 2512.00, "category": "Depilación Láser"},
        {"name": "Bikini Sencillo - 12 SESIÓN", "price": 3559.00, "category": "Depilación Láser"},
        
        {"name": "Bikini Completo - 1 SESIÓN", "price": 549.00, "category": "Depilación Láser"},
        {"name": "Bikini Completo - 6 SESIÓN", "price": 3063.00, "category": "Depilación Láser"},
        {"name": "Bikini Completo - 8 SESIÓN", "price": 3952.00, "category": "Depilación Láser"},
        {"name": "Bikini Completo - 12 SESIÓN", "price": 5599.00, "category": "Depilación Láser"},
        
        # Depilación Láser - Otros
        {"name": "Intergluteo - 1 SESIÓN", "price": 349.00, "category": "Depilación Láser"},
        {"name": "Intergluteo - 6 SESIÓN", "price": 1947.00, "category": "Depilación Láser"},
        {"name": "Intergluteo - 8 SESIÓN", "price": 2512.00, "category": "Depilación Láser"},
        {"name": "Intergluteo - 12 SESIÓN", "price": 3559.00, "category": "Depilación Láser"},
        
        {"name": "Espalda Baja - 1 SESIÓN", "price": 299.00, "category": "Depilación Láser"},
        {"name": "Espalda Baja - 6 SESIÓN", "price": 1668.00, "category": "Depilación Láser"},
        {"name": "Espalda Baja - 8 SESIÓN", "price": 2152.00, "category": "Depilación Láser"},
        {"name": "Espalda Baja - 12 SESIÓN", "price": 3049.00, "category": "Depilación Láser"},
        
        # Tratamientos Corporales - Reducción de Abdomen
        {"name": "Reducción de Abdomen - Por sesión", "price": 399.00, "category": "Tratamientos Corporales"},
        {"name": "Reducción de Abdomen - Paquete 6 sesiones", "price": 1999.00, "category": "Tratamientos Corporales"},
        
        # Tratamientos Corporales - Reducción de Muslos
        {"name": "Reducción de Muslos - Por sesión", "price": 349.00, "category": "Tratamientos Corporales"},
        {"name": "Reducción de Muslos - Paquete 6 sesiones", "price": 1772.00, "category": "Tratamientos Corporales"},
        
        # Tratamientos Corporales - Reducción de Brazos
        {"name": "Reducción de Brazos - Por sesión", "price": 249.00, "category": "Tratamientos Corporales"},
        {"name": "Reducción de Brazos - Paquete 6 sesiones", "price": 1269.00, "category": "Tratamientos Corporales"},
        
        # Tratamientos Corporales - Glúteos Perfectos
        {"name": "Glúteos Perfectos - Por sesión", "price": 249.00, "category": "Tratamientos Corporales"},
        {"name": "Glúteos Perfectos - Paquete 6 sesiones", "price": 1265.00, "category": "Tratamientos Corporales"},
        
        # Tratamientos Corporales - Anticelulítico
        {"name": "Anticelulítico - Por sesión", "price": 249.00, "category": "Tratamientos Corporales"},
        {"name": "Anticelulítico - Paquete 6 sesiones", "price": 1269.00, "category": "Tratamientos Corporales"},
    ]
    
    app = create_app()
    with app.app_context():
        # Crear todas las tablas
        db.create_all()
        
        # Limpiar servicios existentes
        Service.query.delete()
        
        # Agregar nuevos servicios
        for service_data in services_data:
            service = Service(**service_data)
            db.session.add(service)
        
        db.session.commit()
        print(f"Se agregaron {len(services_data)} servicios a la base de datos.")

if __name__ == '__main__':
    populate_services()

