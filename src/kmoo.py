from fastapi import FastAPI
import common

app = FastAPI()

@app.get("/")
def read_root():
    """Default endpoint, only returns the KMOO version."""
    return {"message": "KMOO " + common.KMOO_VERSION + "!"}
