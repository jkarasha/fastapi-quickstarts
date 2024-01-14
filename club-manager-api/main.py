from fastapi import FastAPI

app = FastAPI(title="Club manager API", openapi_url="/openapi.json")

@app.get("/")
def root():
    return {"message": "Hello World"}