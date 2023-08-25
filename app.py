from fastapi import FastAPI, Request
import uvicorn

app = FastAPI()


@app.get("/")
async def signin(request:Request):
    return {"message": "Hello World"}

if __name__ == '__main__':
        uvicorn.run(
        "app:app",
        host    = "0.0.0.0",
        port    = 8037,
        reload  = True
    )
