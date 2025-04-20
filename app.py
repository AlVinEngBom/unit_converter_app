from flask import Flask, request, render_template

app = Flask(__name__)

# Define conversion factors (temperature units are now just identifiers)
conversion_rates = {
    'length': {
        'meter': 1.0,
        'kilometer': 1000.0,
        'mile': 1609.34,
        'foot': 0.3048,
        'inch': 0.0254
    },
    'weight': {
        'kilogram': 1.0,
        'gram': 0.001,
        'pound': 0.453592,
        'ounce': 0.0283495
    },
    'temperature': {
        'celsius': 'celsius',
        'fahrenheit': 'fahrenheit',
        'kelvin': 'kelvin'
    }
    # Add more categories as needed
}

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html', categories=conversion_rates.keys(), conversion_rates=conversion_rates)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')