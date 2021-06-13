from sqlalchemy import Column, Integer, ForeignKey, String
from sqlalchemy.orm import relationship
from restfulpy.orm import DeclarativeBase, Field, OrderingMixin, \
    FilteringMixin, PaginationMixin


class RoomMember(DeclarativeBase):
    __tablename__ = 'room_member'

    member_id= Column(Integer, ForeignKey('member.id'), primary_key=True)
    room_id= Column(Integer, ForeignKey('room.id'), primary_key=True)


class RoomAdmin(DeclarativeBase):
    __tablename__ = 'room_admin'

    admin_id= Column(Integer, ForeignKey('member.id'), primary_key=True)
    room_id= Column(Integer, ForeignKey('room.id'), primary_key=True)

class Room(DeclarativeBase):
    __tablename__ = 'room'

    id = Column(Integer, primary_key=True)
    title = Column(String)

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

