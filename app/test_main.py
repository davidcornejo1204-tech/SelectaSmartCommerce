from fastapi import FastAPI, APIRouter

app = FastAPI()

router = APIRouter(
    prefix="/test",
    tags=["Test"]
)

@router.get("/")
def hello():
    return {"ok": True}

app.include_router(router)

@app.get("/")
def root():
    return {"hello": "world"}