from fastapi import APIRouter
from fastapi.responses import JSONResponse
import json


router = APIRouter(
    prefix="/rrhh",
    #tags=["RRHH"],
)