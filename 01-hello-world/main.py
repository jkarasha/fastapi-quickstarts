from typing import Union
from fastapi import FastAPI, responses, status

app = FastAPI()

@app.get("/hello/{name}", status_code=status.HTTP_200_OK, tags=["greetings"])
async def greeting(name: str = "World") -> Union[str, dict]:
    if name.lower() == "bob":
        return responses.JSONResponse(
            content={"error": "Bob is not allowed"},
            status_code=status.HTTP_400_BAD_REQUEST,
        )
    else:
        return responses.JSONResponse(
            content={"greeting": f"Hello, {name.title()}"},
            status_code=status.HTTP_200_OK,)