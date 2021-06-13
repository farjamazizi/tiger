from datetime import date

from sqlalchemy import String, Date, Integer, extract
from sqlalchemy.orm import column_property, relationship
from restfulpy.orm import DeclarativeBase, Field


class Member(DeclarativeBase):
    __tablename__ = 'member'

    id = Field(Integer, primary_key=True, autoincrement=True)
    first_name = Field(String)
    last_name = Field(String)
    user_name = Field(String, unique=True)
    password = Field(String)
    birth_date = Field(Date)

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

