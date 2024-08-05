from flask import Flask, request, render_template, render_template_string
import sqlite3
app = Flask(__name__)

@app.route('/index.html')
def home():
    return render_template('index.html')

@app.route('/products')
def products():
    query = request.args.get('query', '')
    # Safely embedding user input using Jinja2's autoescaping
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
      <title>Supermart Products</title>
      <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">
    </head>
    <body>
    <header>
    <h1>Our Products</h1> 
        <nav>
          <ul>
            <li><a href="index.html">Home</a></li>
            <li><a href="products">Products</a></li>
            <li><a href="login">Login</a></li>
            <li><a href="contact">Contact</a></li>
          </ul>
        </nav>
      </header>

      <form method="GET">
          <label for="query">Search:</label>
          <input type="text" id="query" name="query" value="{{ query }}">
          <input type="submit" value="Search">
      </form>
      <p>You searched for: {{ query }}</p>
      <div id="searchResults"></div>

      <div class="filter-options">
        <button onclick="sortProducts()">Sort by Price</button>
      </div>

      <div class="product-gallery">
        <div class="product-item">
          <p>Apple Watch Series 9 GPS 41mm Silver Aluminum Case with Storm Blue Sport Band - S/M</p>
          <img src="{{ url_for('static', filename='iphone.jpeg') }}" alt="Product 1" style="width:450px; height:250px;">
          <p>Price: $450 <span class="discount">Discount: 20%</span></p>
          <button onclick="addToCart(this)">Add to Cart</button>
          <button onclick="buyNow(this)">Buy Now</button>
        </div>
        <div class="product-item">
          <p>Samsung Galaxy S23 Ultra 5G Dual S918B 256GB 8GB RAM GSM Unlocked – Black</p>
          <img src="{{ url_for('static', filename='samsung.jpeg') }}" alt="Product 2" style="width:300px; height:200px;"> 
          <p>Price: $150 <span class="discount">Discount: 15%</span></p>
          <button onclick="addToCart(this)">Add to Cart</button>
          <button onclick="buyNow(this)">Buy Now</button>
        </div>
      </div>
    </body>
    </html>
    ''')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact')
def contact():
    query = request.args.get('query', '')
    # Safely passing user input as a variable to the template
    return render_template_string('''
    <!DOCTYPE html>
    <html>
    <head>
      <title>Walmart Products</title>
      <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">
    </head>
    <body>
    <header>
        <h1>Contact Us!</h1>
        <nav>
          <ul>
            <li><a href="index.html">Home</a></li>
            <li><a href="products">Products</a></li>
            <li><a href="login">Login</a></li>
            <li><a href="contact">Contact</a></li>
          </ul>
        </nav>
      </header>
    <form>
        <div class="form-group">
            <label for="email">Email address:</label>
            <input type="email" class="form-control" id="email" placeholder="email@example.com">
        </div>
        <div class="form-group">
            <label for="phone">Phone:</label>
            <input type="tel" class="form-control" id="phone" placeholder="+1 234 567 890">
        </div>
    </form>
    <form method="GET">
        <label for="query">Feedback:</label>
        <input type="text" id="query" name="query" value="{{ query }}">
        <input type="submit" value="Submit">
    </form>
    <div id="searchResults"></div>
    </body>
    </html>
    ''', query=query)

@app.route('/login', methods=['GET', 'POST'])
def login():
    message = ''
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        connection = sqlite3.connect('database.db')
        cursor = connection.cursor()
        
        # Secure SQL query using parameterized statements
        query = "SELECT * FROM users WHERE username=? AND password=?"
        cursor.execute(query, (username, password))
        result = cursor.fetchone()
        
        if result:
            message = 'Logged in successfully'
        else:
            message = 'Invalid credentials'
        connection.close()
    return render_template('login.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
