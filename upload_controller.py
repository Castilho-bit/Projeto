import os
import uuid
from pathlib import Path
from flask import current_app, jsonify, request
from werkzeug.utils import secure_filename
from models.upload_model import register_upload, list_uploads

def upload_file():
    if "file" not in request.files:
        return jsonify({"error": "Envie o arquivo no campo 'file'."}), 400
    file = request.files["file"]
    if not file or not file.filename:
        return jsonify({"error": "Nenhum arquivo selecionado."}), 400

    original_name = secure_filename(file.filename)
    if not original_name:
        return jsonify({"error": "Nome de arquivo inválido."}), 400

    storage_dir = Path(os.getenv("UPLOAD_FOLDER", "uploads"))
    storage_dir.mkdir(parents=True, exist_ok=True)
    extension = Path(original_name).suffix
    stored_name = f"{uuid.uuid4().hex}{extension}"
    destination = storage_dir / stored_name
    file.save(destination)
    size = destination.stat().st_size

    try:
        register_upload(stored_name, original_name, file.mimetype, size)
    except Exception:
        destination.unlink(missing_ok=True)
        raise

    return jsonify({
        "message": "Arquivo enviado com sucesso.",
        "file": {
            "filename": stored_name,
            "original_name": original_name,
            "size": size,
            "content_type": file.mimetype,
            "download_url": f"/download/{stored_name}"
        }
    }), 201

def get_uploads():
    return jsonify({"files": list_uploads()}), 200
