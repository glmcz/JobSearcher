from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def hello():
    return {"msg": "Hi, i am your JobFinder. Tell me what job you are looking for"}

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)