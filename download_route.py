from flask import Blueprint
from controllers.download_controller import download_file

download_bp = Blueprint("download", __name__)
download_bp.add_url_rule(
    "/download/<path:filename>",
    view_func=download_file,
    methods=["GET"]
)
