import os
from pathlib import Path
from flask import jsonify, send_from_directory
from models.download_model import find_upload

def download_file(filename):
    record = find_upload(filename)
    if not record:
        return jsonify({"error": "Arquivo não encontrado."}), 404

    storage_dir = Path(os.getenv("UPLOAD_FOLDER", "uploads"))
    if not (storage_dir / record["filename"]).is_file():
        return jsonify({"error": "O registro existe, mas o arquivo não está disponível no armazenamento."}), 404

    return send_from_directory(
        storage_dir,
        record["filename"],
        as_attachment=True,
        download_name=record["original_name"],
        mimetype=record["content_type"] or "application/octet-stream"
    )
