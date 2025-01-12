from fastapi import FastAPI

app = FastAPI(title="NBA Analytics Platform")

@app.get("/")
async def root():
    return {"message": "NBA Analytics Platform API"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}