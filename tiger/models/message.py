from sqlalchemy import Integer, ForeignKey, Text
from sqlalchemy.orm import relationship
from restfulpy.orm import DeclarativeBase, Field


class Message(DeclarativeBase):
    __tablename__ = 'message'

    id = Field(Integer, primary_key=True, autoincrement=True)
    text = Field(Text)
    sender_id = Field(Integer, ForeignKey('member.id'))
    room_id = Field(Integer, ForeignKey('room.id'))

    room = relationship(
        'Room',
        back_populates='messages',
    )
    sender = relationship(
        'Member',
        back_populates='messages',
    )

