from fastapi import FastAPI

from .schemas import LoginRequest

app = FastAPI(title="ISES Backend")


@app.get("/health")
def health():
    """Simple health check endpoint."""
    return {"status": "ok"}


@app.post("/login")
def login(request: LoginRequest):
    """Placeholder login endpoint."""
    return {"message": f"Login for {request.username} not implemented"}


@app.post("/routes")
def generate_routes():
    """Placeholder route generation endpoint."""
    return {"routes": []}
