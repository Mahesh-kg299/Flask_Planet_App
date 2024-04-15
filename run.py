from app import app
from routes.root import root

app.register_blueprint(root)


if __name__ == "__main__":
    app.run(debug=True)