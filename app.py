from flask import Flask
from controllers.about import about_bp
from controllers.home import home_bp
from controllers.map import map_bp
from controllers.contact import contact_bp

app = Flask(__name__, template_folder = 'templates')

app.register_blueprint(about_bp)
app.register_blueprint(home_bp)
app.register_blueprint(map_bp)
app.register_blueprint(contact_bp)


if __name__ == '__main__':
    app.run(debug=True)