"""
HALAL CONSULTANT MANAGEMENT SYSTEM - Web Version
Flask Application Entry Point
"""
import os
from flask import Flask, render_template, request, jsonify, session, redirect, url_for
from functools import wraps
from datetime import datetime
import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from app.database.database import Database
from app.models.user_model import UserModel
from app.models.client_model import ClientModel
from config.config import APP_NAME, APP_VERSION

# Initialize Flask app
app = Flask(__name__, template_folder='templates', static_folder='static')
app.secret_key = os.environ.get('SECRET_KEY', 'halal-consultant-system-2024-secret-key')

# Initialize database
db = Database()
db.initialize()

# Models
user_model = UserModel()
client_model = ClientModel()

# ========== MIDDLEWARE & DECORATORS ==========
def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if 'user_id' not in session:
            return redirect(url_for('login'))
        return f(*args, **kwargs)
    return decorated_function

# ========== AUTHENTICATION ROUTES ==========
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        username = data.get('username')
        password = data.get('password')
        
        user = user_model.authenticate(username, password)
        if user:
            session['user_id'] = user['id']
            session['username'] = user['username']
            session['full_name'] = user['full_name']
            session['role'] = user['role']
            return jsonify({'success': True, 'redirect': url_for('dashboard')})
        else:
            return jsonify({'success': False, 'message': 'Username atau password salah'}), 401
    
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        data = request.get_json()
        try:
            user_model.create(
                username=data.get('username'),
                email=data.get('email'),
                password=data.get('password'),
                full_name=data.get('full_name')
            )
            return jsonify({'success': True, 'message': 'Akun berhasil dibuat'})
        except Exception as e:
            return jsonify({'success': False, 'message': str(e)}), 400
    
    return render_template('register.html')

# ========== DASHBOARD & MAIN PAGES ==========
@app.route('/')
def index():
    if 'user_id' in session:
        return redirect(url_for('dashboard'))
    return redirect(url_for('login'))

@app.route('/dashboard')
@login_required
def dashboard():
    stats = {
        'total_clients': client_model.count(),
        'pending_submissions': 0,
        'completed_submissions': 0,
        'total_revenue': 0
    }
    return render_template('dashboard.html', stats=stats, user=session)

@app.route('/clients')
@login_required
def clients():
    clients_data = client_model.get_all()
    return render_template('clients.html', clients=clients_data, user=session)

@app.route('/clients/<int:client_id>')
@login_required
def client_detail(client_id):
    client = client_model.get_by_id(client_id)
    if not client:
        return redirect(url_for('clients'))
    return render_template('client_detail.html', client=client, user=session)

# ========== API ENDPOINTS ==========
@app.route('/api/clients', methods=['GET', 'POST'])
@login_required
def api_clients():
    if request.method == 'GET':
        clients = client_model.get_all()
        return jsonify([dict(c) for c in clients])
    
    elif request.method == 'POST':
        data = request.get_json()
        try:
            result = client_model.create(
                name=data.get('name'),
                phone=data.get('phone'),
                email=data.get('email'),
                address=data.get('address'),
                company=data.get('company')
            )
            return jsonify({'success': True, 'id': result})
        except Exception as e:
            return jsonify({'success': False, 'message': str(e)}), 400

@app.route('/api/clients/<int:client_id>', methods=['GET', 'PUT', 'DELETE'])
@login_required
def api_client(client_id):
    if request.method == 'GET':
        client = client_model.get_by_id(client_id)
        return jsonify(dict(client)) if client else ('', 404)
    
    elif request.method == 'PUT':
        data = request.get_json()
        try:
            client_model.update(client_id, **data)
            return jsonify({'success': True})
        except Exception as e:
            return jsonify({'success': False, 'message': str(e)}), 400
    
    elif request.method == 'DELETE':
        try:
            client_model.delete(client_id)
            return jsonify({'success': True})
        except Exception as e:
            return jsonify({'success': False, 'message': str(e)}), 400

# ========== ERROR HANDLERS ==========
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.errorhandler(500)
def server_error(error):
    return render_template('500.html'), 500

# ========== CONTEXT PROCESSORS ==========
@app.context_processor
def inject_config():
    return {
        'app_name': APP_NAME,
        'app_version': APP_VERSION,
        'current_year': datetime.now().year
    }

# ========== STARTUP ==========
if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    debug = os.environ.get('FLASK_ENV') != 'production'
    app.run(host='0.0.0.0', port=port, debug=debug)
