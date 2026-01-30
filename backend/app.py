from flask import Flask
from flask_cors import CORS

from controllers.health_controller import health_bp
def create_app():
    app = Flask(__name__)
    CORS(app)
    app.register_blueprint(health_bp)
    return app

app = create_app()

# Run once on startup
app = create_app()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)