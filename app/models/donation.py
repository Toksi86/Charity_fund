from sqlalchemy import Column, ForeignKey, Integer, String

from .base_donation import BaseDonation


class Donation(BaseDonation):
    __tablename__ = 'donation'

    user_id = Column(Integer, ForeignKey('user.id'))
    comment = Column(String, nullable=True)
