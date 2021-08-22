from quart import g, render_template

from lnbits.decorators import check_user_exists, validate_uuids

from . import usermanager_ext
from fastapi import Request
from fastapi.templating import Jinja2Templates

templates = Jinja2Templates(directory="templates")

@usermanager_ext.get("/")
@validate_uuids(["usr"], required=True)
@check_user_exists()
async def index(request: Request):
    return await templates.TemplateResponse("usermanager/index.html", {"request":request,"user":g.user})