from fastapi import FastAPI, HTTPException, Depends
from starlette import status
from starlette.requests import Request

import settings

docs_kwargs = {}  # noqa: pylint=invalid-name
if settings.ENVIRONMENT == 'production':
    docs_kwargs = dict(docs_url=None, redoc_url=None)

app = FastAPI(**docs_kwargs)


app.include_router(api_router, dependencies=[Depends(check_auth_middleware)])
