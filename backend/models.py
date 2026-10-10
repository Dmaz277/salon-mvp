from sqlalchemy import Column, Integer, String, Date, ForeignKey, Boolean, Time
from database import Base

class User(Base):
    __tablename__ = "users"

    # id as primary key
    id = Column(Integer, primary_key=True)

    # usn string and must unique, nullable always false
    username = Column(String(50), unique=True, nullable=False)

    # stores the hashed password, never the plain text
    password_hash = Column(String(260), nullable=False)

    # valid values: admin, owner
    role = Column(String(30), nullable=False)   

class Staff(Base):
    __tablename__ = "staff"

    # id as primary key
    id = Column(Integer, primary_key=True)

    # staff name for some staff who work in the salon
    staff_name = Column(String(40), nullable=False)

    # True = active, False = resigned or inactive
    status = Column(Boolean, default=True)

class Service(Base):
    __tablename__ = "services"

    # id services as primary key
    id = Column(Integer, primary_key=True)

    # name treatment that they can choose
    treatment_name = Column(String(70), nullable=False)

    # price for they treatment
    price = Column(Integer, nullable=False)

    # duration in minute and Required field
    duration_minutes = Column(Integer, nullable=False)

class Booking(Base):
    __tablename__ = "bookings"
    # primary key, auto-generated booking ID
    id = Column(Integer, primary_key=True)

    # name of the customer who made the booking
    customer_name = Column(String(40), nullable=False) 

    # stored as string to keep the leading 0 or +62
    whatsapp_number = Column(String(15), nullable=False)

    # date of the appointment
    booking_date = Column(Date, nullable=False)

    # start time of the appointment
    booking_time = Column(Time, nullable=False)

    # valid values: pending, confirmed, cancelled
    booking_status = Column(String(40), default="pending", nullable=False)

    # valid values: qris, cash
    payment_method = Column(String(30), nullable=False)

    # valid values: unpaid, paid (set manually by admin)
    payment_status = Column(String(40), default="unpaid", nullable=False)



