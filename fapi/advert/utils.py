import uuid

from sqlalchemy import select
from fapi.database import SessionLocal

from .schemas import Advert, EditAdvert
from .model import Adverts


async def get_all_adverts_from_db():
    async with SessionLocal() as session:
        result = await session.execute(
            select(Adverts)
        )
    return result.scalars().all()

async def get_one_advert_from_db(id: uuid.UUID):
    async with SessionLocal() as session:
        result = await session.get(Adverts, id)
    return result

async def save_advert(advert: Advert):
    async with SessionLocal() as session:
        advert = Adverts(advert)
        session.add(advert)
        await session.commit()
    return advert

async def edit_advert(id: uuid.UUID, advert: EditAdvert):
    async with SessionLocal() as session:
        result = await session.get(Adverts, id)
        for attr in [a for a in dir(result) if not a.startswith('__')]:
            if advert[attr] and result[attr] != advert[attr]:
                result[attr] = advert[attr]
        await session.commit()
    return result