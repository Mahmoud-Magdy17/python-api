from flask import Flask, jsonify, request

app = Flask(__name__)

# Example Python function to be called
def my_function():
    return "Hello from Python!"

@app.route('/run-python', methods=['GET'])
def run_python_function():
    result = my_function()  # Call the Python function
    return jsonify({'message': result})

if __name__ == '__main__':
    app.run(debug=True)
