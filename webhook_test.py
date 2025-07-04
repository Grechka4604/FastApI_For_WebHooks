from flask import Flask, request, jsonify
import json

app = Flask(__name__)

@app.route("/tilda-webhook", methods=["POST"])
def webhook():
    data = request.form.to_dict()
    print("Получен Webhook от Tilda:", data)
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(json.dumps(data, ensure_ascii=False) + "\n")
    return jsonify(status="ok")

@app.route("/matomba-webhook", methods=["POST"])
def matomba():
    data = request.get_json(force=True)
    print("🔥 Пришёл Webhook от Matomba:", data)
    return jsonify(status="ok")
