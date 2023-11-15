from flask import Flask, render_template, request, redirect
import hashlib

app = Flask(__name__)

# In-memory database for simplicity. In a real application, use a proper database.
url_database = {}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten():
    long_url = request.form['long_url']
    short_url = generate_short_url(long_url)
    url_database[short_url] = long_url
    return render_template('index.html', short_url=short_url)

@app.route('/<short_url>')
def redirect_to_original(short_url):
    long_url = url_database.get(short_url)
    if long_url:
        return redirect(long_url)
    else:
        return render_template('index.html', error='URL not found.')

def generate_short_url(long_url):
    # Simple hashing for demonstration purposes. Use a more secure method in production.
    hashed = hashlib.sha256(long_url.encode()).hexdigest()[:8]
    return hashed

if __name__ == '__main__':
    app.run(debug=False)
