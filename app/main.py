from fastapi import FastAPI
from app.api import auth, bottles, pos, analytics, hardware, credits

app = FastAPI()

app.include_router(auth.router)
app.include_router(bottles.router)
app.include_router(pos.router)
app.include_router(analytics.router)
app.include_router(hardware.router)
app.include_router(credits.router)

@app.get("/health")
def health():
    return {"status": "ok"}
