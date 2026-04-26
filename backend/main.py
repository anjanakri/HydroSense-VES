from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware #Cross Origin Resource Sharing

app=FastAPI(
    title="HydroSense VES",
    description="Schlumberger VES Analysis Tool for Groundwater Exploration",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"message": "HydroSense VES API is running"}