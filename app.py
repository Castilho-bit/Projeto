import os
from flask import Flask, jsonify
from routes.upload_route import upload_bp
from routes.download_route import download_bp
from database.db import init_db

def create_app():
    app = Flask(__name__)
    app.config["MAX_CONTENT_LENGTH"] = int(os.getenv("MAX_CONTENT_LENGTH", 16 * 1024 * 1024))
    app.register_blueprint(upload_bp)
    app.register_blueprint(download_bp)

    @app.get("/")
    def home():
        return jsonify({
            "message": "API de upload e download está funcionando!",
            "endpoints": {
                "health": "/health",
                "upload": "POST /upload (multipart/form-data, campo 'file')",
                "download": "GET /download/<filename>"
            }
        })

    @app.get("/health")
    def health():
        return jsonify({"status": "ok"}), 200

    init_db()
    return app

app = create_app()

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
