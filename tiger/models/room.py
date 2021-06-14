from sqlalchemy import  Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from restfulpy.orm import DeclarativeBase, Field


class RoomMember(DeclarativeBase):
    __tablename__ = 'room_member'

    member_id= Field(Integer, ForeignKey('member.id'), primary_key=True)
    room_id= Field(Integer, ForeignKey('room.id'), primary_key=True)


class RoomAdmin(DeclarativeBase):
    __tablename__ = 'room_admin'

    admin_id= Field(Integer, ForeignKey('member.id'), primary_key=True)
    room_id= Field(Integer, ForeignKey('room.id'), primary_key=True)


class Room(DeclarativeBase):
    __tablename__ = 'room'

    id = Field(Integer, primary_key=True)
    title = Field(String)

    messages = relationship(
        'Message',
        back_populates='room',
    )
    members=relationship(
        'Member',
        secondary='room_member',
        back_populates='rooms',
    )

    admins = relationship(
        'Member',
        secondary='room_admin',
        back_populates='admin_rooms',
    )

