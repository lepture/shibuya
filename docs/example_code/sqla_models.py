"""Example SQLAlchemy ORM models."""

from sqlalchemy import CheckConstraint, Column, ForeignKey, UniqueConstraint, orm, types

Base = orm.declarative_base()


class User(Base):
    """A ``user``."""

    __tablename__ = "dbusers"
    __table_args__ = (UniqueConstraint("first_name", "last_name"),)
    pk = Column(types.Integer, primary_key=True)
    first_name = Column(types.String, doc="The name of the user.")
    last_name = Column(types.String(255), doc="The surname of the user.")
    dob = Column(types.Date, nullable=False, doc="The date of birth.")


class Address(Base):
    """An address."""

    __tablename__ = "addresses"
    __table_args__ = (CheckConstraint("number>0", name="check1"),)
    pk = Column(types.Integer, primary_key=True)
    number = Column(types.Integer, nullable=False, doc="The number of the address.")
    postcode = Column(
        types.String, nullable=False, index=True, doc="The postcode of the address."
    )
    user_id = Column(types.Integer, ForeignKey("dbusers.pk"))
    user = orm.relationship("User")
