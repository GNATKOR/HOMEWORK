from flask import Flask, request, render_template, jsonify

app = Flask(__name__)

products = []


@app.route('/products', methods=['POST'])
def create_product():
    data = request.form
    products.append(data)
    message = f"Product {request.form['name']} created successfully!", 201
    return render_template('index3.html', message=message)


@app.route('/products/getname', methods=['GET'])
def get_name():
    product_names = []
    for i in products:
        product_names.append(i['name'])
    return jsonify(product_names)


@app.route('/products/getcalories', methods=['GET'])
def get_calories():
    product_calories = []
    for i in products:
        product_calories.append(i['calories'])
    return jsonify(product_calories)


@app.route('/products', methods=['GET'])
def get_products():
    return render_template('index2.html')


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
