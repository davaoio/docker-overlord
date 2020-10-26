from fastapi import FastAPI, HTTPException
from .routers import users, aws, deploy, config
from .services import util
from starlette.requests import Request
from starlette.staticfiles import StaticFiles
from starlette.responses import RedirectResponse, JSONResponse, HTMLResponse

app = FastAPI()

# This is only really for serving test files. We would probably serve static
# files from S3 directly.
app.mount("/static", StaticFiles(directory="/vue/dist"), name="static")

app.include_router(users.router, prefix="/api/users")
app.include_router(aws.router, prefix="/api/aws")
app.include_router(deploy.router, prefix="/api/deploy")
app.include_router(config.router, prefix="/api/config")

@app.get("/.*", include_in_schema=False)
def root():
    with open('/vue/dist/index.html') as f:
        return HTMLResponse(content=f.read(), status_code=200)
