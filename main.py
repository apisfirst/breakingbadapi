from fastapi import FastAPI
from routes import router as api_router

app = FastAPI()

# Include all routers from routes/__init__.py
app.include_router(api_router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)
