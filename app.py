from flask import Flask, render_template, request, redirect

app = Flask(__name__)

# Sample data (replace with a database in a real-world scenario)
menu_items = {
    1: {'name': 'Hibachi Chicken', 'price': 15.99},
    2: {'name': 'Hibachi Steak', 'price': 18.99},
    # Add more menu items as needed
}

orders = []

@app.route('/')
def home():
    return render_template('menu.html', menu_items=menu_items)

@app.route('/order', methods=['POST'])
def order():
    item_id = int(request.form.get('item_id'))
    quantity = int(request.form.get('quantity'))

    item = menu_items.get(item_id)

    if item:
        total_price = item['price'] * quantity
        orders.append({'item': item['name'], 'quantity': quantity, 'total_price': total_price})
        return redirect('/')
    else:
        return "Invalid item ID"

@app.route('/cart')
def cart():
    return render_template('cart.html', orders=orders)

if __name__ == '__main__':
    app.run(debug=True)
