import uvicorn
from fastapi import FastAPI, APIRouter
from pydantic import BaseModel, EmailStr
from typing import Optional

from src.core.config import uvicorn_options

from src.api import api_router


app = FastAPI(
    docs_url="/api/openapi"
)

app.include_router(api_router)


class MyGetFuncResponseSchema(BaseModel):
    app_name: str
    number_of_months: int
    pi: float


class User(BaseModel):
    name: str
    email: EmailStr
    age: Optional[int] = None


@app.get("/path", responses={
    200: {"model": MyGetFuncResponseSchema},
    404: {"description": "Response not found"},
    400: {"description": "Invalid request"},
})
def my_get_func():
    return {
        "app_name": "MyAPP",
        "number_of_months": 12,
        "pi": 3.14
    }


@app.post("/path", response_model=User)
def my_post_func(user: User):
    return user


@api_router.put("/path")
def my_put_func():
    pass


@api_router.delete("/path")
def my_delete_func():
    pass


app.include_router(api_router)

if __name__ == '__main__':
    # print для отображения настроек в терминале при локальной разработке
    print(uvicorn_options)
    uvicorn.run(
        'main:app',
        **uvicorn_options
    )