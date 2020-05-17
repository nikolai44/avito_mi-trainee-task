from fastapi import FastAPI, HTTPException

import settings
from router import api_router

docs_kwargs = {}  # noqa: pylint=invalid-name
if settings.ENVIRONMENT == 'production':
    docs_kwargs = dict(docs_url=None, redoc_url=None)

app = FastAPI(**docs_kwargs)

# app.add_event_handler("startup", connect_to_mongo)
# app.add_event_handler("shutdown", close_mongo_connection)
#
# app.add_exception_handler(HTTPException, http_error_handler)
# app.add_exception_handler(HTTP_422_UNPROCESSABLE_ENTITY, http_422_error_handler)

app.include_router(api_router)
