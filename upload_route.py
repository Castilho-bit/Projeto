from flask import Blueprint
from controllers.upload_controller import upload_file, get_uploads

upload_bp = Blueprint("upload", __name__)
upload_bp.add_url_rule("/upload", view_func=upload_file, methods=["POST"])
upload_bp.add_url_rule("/uploads", view_func=get_uploads, methods=["GET"])
