from sqlalchemy import String, Integer, ForeignKey
from sqlalchemy.orm import relationship
from restfulpy.orm import DeclarativeBase, Field


class Error_Report(DeclarativeBase):
    __tablename__ = 'error_report'

    curl = Field(String)
    stack_trace = Field(String)
    status = Field(String)
    organization = Field(Integer)
    created_at = Field(String)
    modified_at = Field(String)
    member_id = Field(Integer, ForeignKey('member.id'))


