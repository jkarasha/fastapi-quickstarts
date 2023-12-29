from fastapi import FastAPI, APIRouter, status
app = FastAPI(title="Recipe API", openapi_url="/openapi.json")

api_router = APIRouter()
app.include_router(api_router)

@api_router.get("/", status_code=status.HTTP_200_OK)
def root() -> dict:
    """
    Root GET
    """
    return {"message": "Hello World"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, log_level="debug")
