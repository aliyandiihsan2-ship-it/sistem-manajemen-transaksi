from fastapi import FastAPI 
from router.router_transaction import router_transaction
from router.router_user import router_user
from fastapi import HTTPException
from fastapi.responses import JSONResponse
app=FastAPI()
@app.exception_handler(HTTPException)
def standard_response_error(request,exc:HTTPException):
    return JSONResponse(
        status_code=exc.status_code,
        content={"code":exc.status_code,"message":exc.detail}
    )
app.include_router(router_transaction)
app.include_router(router_user) 