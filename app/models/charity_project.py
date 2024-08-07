from sqlalchemy import Column, String, Text

from .base_donation import BaseDonation


class CharityProject(BaseDonation):
    __tablename__ = 'charityproject'

    name = Column(String(100), unique=True, nullable=False)
    description = Column(Text, nullable=False)
