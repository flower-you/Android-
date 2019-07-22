from flask import request, jsonify, send_from_directory, abort
import os


def download(filename):
    if request.method == "GET":
        if os.path.isfile(os.path.join('.', filename)):
            return send_from_directory('upload', filename, as_attachment=True)
        abort(404)

download("test.txt")
