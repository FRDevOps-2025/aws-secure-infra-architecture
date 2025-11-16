from flask import Flask
app = Flask(__name__)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/info")
def info():
    return {"app": "python-backend", "version": "1.0"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
