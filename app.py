from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    """Homepage for Open Terminal."""
    return render_template('index.html', slogan="Trade Smart, Trade Fast")

@app.route('/about')
def about():
    """About page for Open Terminal."""
    return render_template('about.html', description="Open Terminal is a Trading Terminal for traders built using Python, Flask, and AngelOne Smart API.")

@app.route('/order')
def order():
    return render_template('order.html')

# Example GET request with name and age parameters
@app.route('/api/get_example', methods=['GET'])
def get_example():
    """Accepts only name and age as parameters and returns them in the response."""
    name = request.args.get("name")
    age = request.args.get("age")
    
    if not name or not age:
        return jsonify({"error": "Both name and age parameters are required"}), 400
    
    response = {"message": "Received parameters", "name": name, "age": age}
    return jsonify(response)

# Updated POST request for handling trade orders with Buy/Sell functionality
@app.route('/api/post_example', methods=['POST'])
def post_example():
    """Receives Symbol, Quantity, Exchange, and Order Type (Buy/Sell) and responds back with detailed message."""
    data = request.json
    symbol = data.get("symbol")
    quantity = data.get("quantity")
    exchange = data.get("exchange") 
    order_type = data.get("order_type")
    
    if not symbol or not quantity or not exchange or not order_type:
        return jsonify({"error": "Symbol, Quantity, Exchange, and Order Type are required"}), 400
    
    color = "green" if order_type == "buy" else "red"
    
    return jsonify({
        "message": f"Order received successfully: Symbol - {symbol}, Quantity - {quantity}, Exchange - {exchange}, Order Type - {order_type.capitalize()}",
        "symbol": symbol,
        "quantity": quantity,
        "exchange": exchange,
        "order_type": order_type,
        "color": color
    })

if __name__ == '__main__':
    app.run(debug=True)
