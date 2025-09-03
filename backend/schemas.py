from pydantic import BaseModel


class LoginRequest(BaseModel):
    username: str
    password: str


class Order(BaseModel):
    id_referencia: str
    direccion: str
    localidad: str
    tiempo_inspeccion: int
