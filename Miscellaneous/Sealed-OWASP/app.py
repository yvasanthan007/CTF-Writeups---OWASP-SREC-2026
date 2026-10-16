"""Internal file sealing service."""

import os
import random
import time
from pathlib import Path

from flask import Flask, jsonify


def create_app(secret_path: Path, output_path: Path) -> Flask:
    app = Flask(__name__)

    @app.get("/health")
    def health():
        return jsonify(status="ok")

    @app.post("/api/v1/seal")
    def seal():
        secret = secret_path.read_bytes()
        rng = random.Random(int(time.time()))
        receipt = rng.randbytes(8).hex()
        mask = rng.randbytes(len(secret))
        output_path.write_bytes(bytes(a ^ b for a, b in zip(secret, mask)))
        return jsonify(receipt=receipt, file=output_path.name, size=len(secret))

    return app


if __name__ == "__main__":
    create_app(
        Path(os.environ.get("FLAG_FILE", "flag.txt")),
        Path(os.environ.get("OUTPUT_FILE", "flag.enc")),
    ).run(host="127.0.0.1", port=8080)
