from sqlalchemy import Column, ForeignKey, Integer, Text

from .abstract_base import AbstractBase


class Donation(AbstractBase):
    user_id = Column(Integer, ForeignKey(
        'user.id', name='fk_donation_user_id_user'))
    comment = Column(Text)