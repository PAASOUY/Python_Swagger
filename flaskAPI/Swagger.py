from flask import Flask
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/api/hello', methods=['GET'])
def hello():
    """
    A simple hello world endpoint.
    ---
    responses:
      200:
        description: A hello world message
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Hello, World!"
    """
    return {"message": "Hello, This is Swagger UI!"}

if __name__ == '__main__':
    app.run(debug=True)
