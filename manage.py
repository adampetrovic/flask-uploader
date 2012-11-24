from flask.ext.script import Manager
from api import app

if app.config['ENVIRONMENT'] == 'production':
    import logging
    from logging.handlers import RotatingFileHandler

    file_handler = RotatingFileHandler('logs/errors.log', maxBytes=13107200)
    file_handler.setLevel(logging.WARNING)
    app.logger.addHandler(file_handler)

manager = Manager(app)
@manager.command
def runserver():
    app.run(host='0.0.0.0', port=5002, debug=app.config['ENVIRONMENT'] != 'production')

if __name__ == '__main__':
    if app.config['ENVIRONMENT'] != 'production':
        manager.run()
    else:
        app.run()
