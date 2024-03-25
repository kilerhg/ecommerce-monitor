from fastapi import APIRouter
from fastapi.responses import JSONResponse


router = APIRouter(
    prefix='/scraper',
    tags=['scraper'],
)


@router.get('/')
def index():
    return JSONResponse({'value': 'hello_world'})