from flask import Flask
import logging
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

# Logging setup
logger = logging.getLogger("myapp")
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler("logs/app.log")
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

# Prometheus metrics
REQUEST_COUNT = Counter("app_requests_total", "Total requests")

@app.route("/")
def home():
    logger.info("Home page visited")
    REQUEST_COUNT.inc()
    return "Welcome to the Flask App!"

@app.route("/metrics")
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

