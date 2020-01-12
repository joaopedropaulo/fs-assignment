import uvicorn

from fastapi import FastAPI
from starlette.responses import RedirectResponse


app = FastAPI()


@app.get("/", include_in_schema=False)
async def read_root():
    return RedirectResponse(url='/docs')


if __name__ == '__main__':
    # only debug
    uvicorn.run(app, host="0.0.0.0", port=8080)
