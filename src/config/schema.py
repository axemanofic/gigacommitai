from typing import Literal, Optional

from pydantic import BaseModel


SCOPE = Literal["GIGACHAT_API_PERS", "GIGACHAT_API_CORP"]


class GigachatSchema(BaseModel):
    credentials: Optional[str] = ""
    scope: SCOPE = "GIGACHAT_API_PERS"
    model: str = "GigaChat"
    verify_ssl_certs: bool = False


class AppSchema(BaseModel):
    gigachat: GigachatSchema


