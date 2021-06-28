from datetime import date

from sqlalchemy import String, Integer, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from restfulpy.orm import DeclarativeBase, Field


class ErrorReport(DeclarativeBase):
    __tablename__ = 'error_report'

    id = Field(Integer, primary_key=True)
    curl = Field(String)
    stack_trace = Field(String)
    status = Field(String)
    organization_id = Field(Integer)
    created_at = Field(DateTime)
    modified_at = Field(DateTime)
    member_id = Field(Integer, ForeignKey('member.id'))
   
    member = relationship(
        'Member', 
        back_populates='error_reports',
    )

