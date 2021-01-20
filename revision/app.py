from flask import Flask, render_template, request, redirect, url_for
import os

# Create new flask application(ie; the server)
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.template.html')

@app.route('/products')
def show_products():
    all_products = [
        "ACME Hammer", "ACME Nails", "ACME Screwdriver"
    ]
    return render_template('products.template.html')



# "magic code" -- boilerplate
if __name__ == '__main__':
    app.run(host=os.environ.get('IP'),
            port=int(os.environ.get('PORT')),
            debug=True)