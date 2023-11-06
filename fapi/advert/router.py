import uuid
from fastapi import APIRouter, File, Request

from .schemas import Advert, EditAdvert
from .utils import get_all_adverts_from_db, get_one_advert_from_db, save_advert, edit_advert

advert_router = APIRouter(prefix="/v1/adverts", tags=["Объявления"])


@advert_router.get("/")
def get_all_adverts():
    get_all_adverts_from_db()


@advert_router.get("/{id}")
def get_advert(id):
    get_one_advert_from_db(id)


@advert_router.post("/")
def add_advert(
    request: Request,
    advert: Advert,
):
    save_advert(advert, request.user)


@advert_router.patch("/{id}")
def edit_advert(
    id: uuid.UUID,
    advert: EditAdvert
):
    edit_advert(id, advert)
