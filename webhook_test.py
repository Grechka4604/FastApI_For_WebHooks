from flask import Flask, request

app = Flask(__name__)

@app.route('/tilda-webhook', methods=['POST'])
def webhook():
    data = request.json
    print("Получен Webhook от Tilda:", data)
    return {"status": "ok"}

if __name__ == '__main__':
    app.run(port=8000)
