import uuid
from fastapi import APIRouter, File, Request

from .schemas import Advert, EditAdvert
from .utils import get_all_adverts_from_db, get_one_advert_from_db, save_advert, edit_advert

advert_router = APIRouter(prefix="/v1/adverts", tags=["Объявления"])


@advert_router.get("/")
async def get_all_adverts():
    return await get_all_adverts_from_db()


@advert_router.get("/{id}")
async def get_advert(id):
    return await get_one_advert_from_db(id)


@advert_router.post("/")
async def add_advert(
    request: Request,
    advert: Advert,
):
    await save_advert(advert)


@advert_router.patch("/{id}")
async def edit_advert(
    id: uuid.UUID,
    advert: EditAdvert
):
    await edit_advert(id, advert)
