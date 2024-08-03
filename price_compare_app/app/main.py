# app/main.py
from fastapi import FastAPI
from app.routers import products

app = FastAPI()

app.include_router(products.router)

@app.get("/")
async def root():
    return {"message": "Welcome to Price Compare App"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)