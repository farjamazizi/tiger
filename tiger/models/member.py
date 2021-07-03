from datetime import date

from sqlalchemy import String, Date, Integer, extract, Enum
from sqlalchemy.orm import column_property, relationship
from restfulpy.orm import DeclarativeBase, Field


member_statuses = [
    'active',
    'deactive',
]


class Member(DeclarativeBase):
    __tablename__ = 'member'

    id = Field(Integer, primary_key=True, autoincrement=True)
    first_name = Field(String)
    last_name = Field(String)
    user_name = Field(String, unique=True)
    password = Field(String)
    birth_date = Field(Date)
    status = Field(
        Enum(*member_statuses, name='member_statuses'),
        nullable=False,
    )
    age = column_property(date.today().year - extract('year', birth_date))
    fullname = column_property(first_name + ' ' + last_name)

    error_reports = relationship(
        'ErrorReport',
        back_populates='member',
    )
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

