from flask import Flask, render_template, session, redirect, url_for

app = Flask(__name__)
app.secret_key = 'paste_generated_key_here'  # Replace with the generated key

# Sample sock data
socks = {
    1: {'name': 'Comfort Crew Sock', 'price': 10.99},
    2: {'name': 'Cozy Stripe Sock', 'price': 12.99},
}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/cart')
def cart():
    cart_items = session.get('cart', [])
    total_price = sum(item['price'] for item in cart_items)
    return render_template('cart.html', cart=cart_items, total_price=total_price)

@app.route('/add_to_cart/<int:sock_id>', methods=['POST'])
def add_to_cart(sock_id):
    cart_items = session.get('cart', [])
    sock = socks.get(sock_id)
    if sock:
        cart_items.append({'name': sock['name'], 'price': sock['price']})
        session['cart'] = cart_items
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)


