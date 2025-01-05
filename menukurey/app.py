from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Data menu coffee shop
menu = {
    "coffee": {
        "Espresso": 20000,
        "Americano": 25000,
        "Cappuccino": 30000,
        "Latte": 35000
    },
    "tea": {
        "Green Tea": 20000,
        "Black Tea": 18000,
        "Milk Tea": 25000
    },
    "snack": {
        "Brownie": 20000,
        "Croissant": 25000,
        "Muffin": 15000
    }
}

# Variabel global untuk menyimpan pesanan pengguna
order = {}

# Halaman utama untuk menampilkan menu
@app.route('/')
def index():
    return render_template('index.html', menu=menu, order=order)

@app.route('/add_to_order', methods=['POST'])
def add_to_order():
    category = request.form.get('category')  # Ambil kategori dari form
    item = request.form.get('item')  # Ambil item dari form
    quantity = int(request.form.get('quantity', 1))  # Ambil jumlah dari form

    # Validasi apakah item ada di menu kategori yang sesuai
    if category in menu and item in menu[category]:
        order[item] = order.get(item, 0) + quantity  # Tambahkan ke pesanan
    return redirect(url_for('index'))



# Endpoint untuk checkout dan menampilkan struk
@app.route('/checkout')
def checkout():
    total_price = sum(menu[cat][item] * qty for item, qty in order.items() for cat in menu if item in menu[cat])
    return render_template('checkout.html', order=order, menu=menu, total_price=total_price)

# Endpoint untuk menghapus pesanan
@app.route('/remove_item/<item>')
def remove_item(item):
    if item in order:
        del order[item]
    return redirect(url_for('index'))

# Jalankan aplikasi
if __name__ == '__main__':
    app.run(debug=True)