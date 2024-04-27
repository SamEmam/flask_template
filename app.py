from flask import Flask, render_template


def config_app(app):
    app.config["DEBUG"] = True

def create_app() -> Flask:
    app = Flask(__name__)

    config_app(app)

    @app.route('/', methods=['GET', 'POST'])
    def index():
        return render_template(
            'index.html'
        )

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host='127.0.0.1', port=5000)