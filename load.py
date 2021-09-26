from flask import Flask, jsonify
from transform import get_order_numbers

app = Flask(__name__)

# retorna os números ordenados salvos
@app.route('/get_order_numbers')
def order():
    data=get_order_numbers(False)
    return jsonify(data)

# extrai e ordena os fundos novamente e retorna
@app.route('/update_numbers')
def update():
    data=get_order_numbers(True)
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
    

