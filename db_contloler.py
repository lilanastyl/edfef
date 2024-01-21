from typing import List, Optional
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from sqlalchemy import String, ForeignKey


class DatabaseManager:
    def __init__(self, engine_url: str):
        self.engine = create_engine(engine_url, echo=True)
        self.Base = DeclarativeBase
        self.Base.metadata.create_all(self.engine)
        self.session = Session(self.engine)

    def close_session(self):
        self.session.close()

    def add_user(self, user):
        self.session.add(user)
        self.session.commit()

    def get_user_by_name(self, username):
        stmt = select(User).where(User.name == username)
        return self.session.scalars(stmt).one()

    def add_address_to_user(self, user, email_address):
        address = Address(email_address=email_address, user=user)
        user.addresses.append(address)
        self.session.commit()

    def update_address(self, user, old_email, new_email):
        stmt = select(Address).join(Address.user).where(User.id == user.id).where(
            Address.email_address == old_email
        )
        address = self.session.scalars(stmt).one()
        address.email_address = new_email
        self.session.commit()

    def remove_address_from_user(self, user, email_address):
        stmt = select(Address).join(Address.user).where(User.id == user.id).where(
            Address.email_address == email_address
        )
        address = self.session.scalars(stmt).one()
        user.addresses.remove(address)
        self.session.commit()

    def delete_user(self, user):
        self.session.delete(user)
        self.session.commit()


class User(DatabaseManager):
    __tablename__ = "user_account"
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30))
    fullname: Mapped[Optional[str]]
    addresses: Mapped[List["Address"]] = relationship(
        back_populates="user", cascade="all, delete-orphan"
    )
    def __repr__(self) -> str:
        return f"User(id={self.id!r}, name={self.name!r}, fullname={self.fullname!r})"
    

class Address(DatabaseManager):
    __tablename__ = "address"
    id: Mapped[int] = mapped_column(primary_key=True)
    email_address: Mapped[str]
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
    user: Mapped["User"] = relationship(back_populates="addresses")
    def __repr__(self) -> str:
        return f"Address(id={self.id!r}, email_address={self.email_address!r})"
