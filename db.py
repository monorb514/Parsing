from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import Column, Integer, String

from decouple import config

Base = declarative_base()
engine = create_engine(config('URL'), echo=True)

default_image = 'https://afs.googleusercontent.com/kijiji-ca/csa-image1-large.png'


class Apartment(Base):
    __tablename__ = 'apartments'
    id = Column(Integer, primary_key=True)
    price = Column(String(50))
    image = Column(String(200), default=default_image)
    published = Column(String(50))

    def __repr__(self):
        return "<Apartment(price='{}', image='{}', date={})>" \
            .format(self.price, self.image, self.published)


def save(data):
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    for i in data:
        item = Apartment(**i)
        session.add(item)
    session.commit()
    session.close()
    print("Данные сохранены")