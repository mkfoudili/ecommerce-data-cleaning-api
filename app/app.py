from db import init_app, db
from routes import bp
from flasgger import Swagger

app = init_app()
swagger = Swagger(app)
app.register_blueprint(bp, url_prefix="/api")

with app.app_context():
    db.create_all()

if __name__ == "__main__":
    app.run(debug=True)