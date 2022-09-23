from flask import Blueprint

catalog = Blueprint("catalog", __name__,static_folder="static", template_folder="templates")

from app.catalog import routes