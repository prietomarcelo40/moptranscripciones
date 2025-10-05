from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/servicios')
def servicios():
    return render_template('servicios.html')

@app.route('/desarrollador')
def desarrollador():
    return render_template('desarrollador.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))  # Puerto Render o 5000 local
    debug_mode = os.environ.get('FLASK_DEBUG', '1') == '1'  # Debug solo local
    app.run(host='0.0.0.0', port=port, debug=debug_mode)
