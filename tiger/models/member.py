from datetime import date

from sqlalchemy import Column, String, Date, Integer, select, func, extract
from sqlalchemy.orm import column_property, relationship
from restfulpy.orm import DeclarativeBase, Field, OrderingMixin, \
    FilteringMixin, PaginationMixin


class Member(DeclarativeBase):
    __tablename__ = 'member'

    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String)
    last_name = Column(String)
    user_name = Column(String, unique=True)
    password = Column(String)
    birth_date = Column(Date)

    messages = relationship(
        'Message',
        back_populates='sender',
    )
    rooms = relationship(
        'Room',
        secondary='room_member',
        back_populates='members',
    )

    admin_rooms = relationship(
        'Room',
        secondary='room_admin',
        back_populates='admins',
    )

    age = column_property(date.today().year - extract('year', birth_date))
    fullname = column_property(first_name + ' ' + last_name)

