from flask import Flask

app = Flask(__name__)
app.config['ENVIRONMENT'] = "dev"

from main import main_api
app.register_blueprint(main_api)
