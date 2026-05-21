from fastapi import FastAPI


app = FastAPI()


@app.get("/", tags=["home"])
async def home() -> dict:
    return {"message": "Hello kub", "status": True}
