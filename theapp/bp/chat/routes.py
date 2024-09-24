from flask import Blueprint, render_template, current_app, request, redirect, jsonify
from theapp.utils.G4F import G4F

import datetime
import json
import time

chat_bp = Blueprint('chat_bp', __name__, template_folder='template', static_folder='static', static_url_path='/chat-static')

@chat_bp.route('/api/chat/helloworld', methods=["GET"])
def api_chat_helloworld():   
    res = {"message": "Hello world !"}

    return jsonify(res)

@chat_bp.route('/api/chat/discussion', methods=["POST"])
def api_chat_discussion():   
    res = {"success": False}

    data = request.get_json()

    model = data.get("model") if data.get("model") else None
    messages = data.get("messages") if data.get("messages") else None
    stream = data.get("stream") if data.get("stream") else False
    proxy = data.get("proxy") if data.get("proxy") else None
    find_proxy = data.get("find_proxy") if data.get("find_proxy") else False

    gf = G4F()

    response = gf.get_chat_answer(model = model, messages = messages, stream = stream, proxy = proxy, find_proxy = find_proxy)
    if response.get("success") :
        res["success"] = True
        res["answer"] = response.get("answer")

    return jsonify(res)

@chat_bp.route('/api/chat/models', methods=["GET"])
def api_chat_models():   
    res = {"models": []}

    gf = G4F()
    models = gf.get_all_models()
    res["models"] = models

    return jsonify(res)