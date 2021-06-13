from sqlalchemy import Column, Integer, ForeignKey, Text
from sqlalchemy.orm import relationship
from restfulpy.orm import DeclarativeBase, Field, OrderingMixin, \
    FilteringMixin, PaginationMixin


class Message(DeclarativeBase):
    __tablename__ = 'message'

    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(Text)
    sender_id = Column(Integer, ForeignKey('member.id'))
    room_id = Column(Integer, ForeignKey('room.id'))

    room = relationship(
        'Room',
        back_populates='messages',
    )
    sender = relationship(
        'Member',
        back_populates='messages',
    )

