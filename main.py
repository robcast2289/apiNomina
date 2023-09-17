from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import routers

app = FastAPI()
app.include_router(routers.UsuarioRouter.router)
app.include_router(routers.SeguridadRouter.router)

origins = [
    "http://localhost",
    "http://localhost:8888",
    "http://localhost:8080",
    "http://localhost:4200",
    "http://localhost:80",
    "http://nomina.robcastgt.com",
    "http://34.71.87.248:80",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def index():
    return "Api funcionando"
