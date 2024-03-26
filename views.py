from flask import jsonify, render_template, request
from psycopg2 import IntegrityError
from app import app
from models import *
from controller import *

# Rute untuk halaman utama
@app.route("/")
def home():
    return render_template('dashboard.html')

# Rute untuk halaman login
@app.route("/login")
def login():
    return render_template('login.html')

# Fungsi untuk melakukan login
@app.route('/login', methods=['POST'])
def login_pengguna():
    id_user = request.form['username']
    password = request.form['password']

    # Cek apakah pengguna ada dalam database
    user = User.query.filter_by(id_user=id_user, password=password).first()
    if user:
        return f"Selamat datang, {id_user}!"
    else:
        return "Login gagal. Cek kembali username dan password Anda."
    
# Rute untuk halaman pendaftaran akun
@app.route("/daftar")
def daftar():
    return render_template('daftar.html')

# Fungsi untuk melakukan pendaftaran akun
@app.route('/daftar', methods=['POST'])
def daftar_akun():
    id_user = request.form['id_user']
    password = request.form['password']

    # Tambahkan pengguna baru ke dalam database
    try:
        new_user = User(id_user=id_user, password=password)
        db.session.add(new_user)
        db.session.commit()
        return f"Akun {id_user} berhasil didaftarkan."
    except IntegrityError:
        db.session.rollback()
        return "Username sudah digunakan. Silakan pilih username lain."
    
# Rute untuk mendapatkan daftar menu
@app.route('/menu', methods=['GET'])
def menu():
    session = Session()
    menus = session.query(Menu).all()
    session.close()
    output = []
    for menu in menus:
        menu_data = {}
        menu_data['id_menu'] = menu.id_menu
        menu_data['nama'] = menu.nama
        menu_data['harga'] = menu.harga
        menu_data['kuantitas'] = menu.kuantitas
        output.append(menu_data)
    return jsonify({'menu': output})


# Rute untuk mendapatkan pesanan
@app.route('/pesan', methods=['GET'])
def pesan():
    return jsonify({'pesan': antrian_restoran})

# Rute untuk menambahkan nomor meja ke dalam antrian
@app.route('/pesan', methods=['POST'])
def add_to_antrian():
    data = request.get_json()
    nomor_meja = data.get('nomor_meja')

    if not nomor_meja:
        return jsonify({'error': 'Nomor meja harus disertakan'}), 400

    antrian_restoran.append({'nomor_meja': nomor_meja, 'status': 'menunggu'})
    return jsonify({'message': f'Nomor meja {nomor_meja} telah ditambahkan ke dalam antrian'})

# Rute untuk memperbarui status antrian (misalnya: dipanggil, selesai)
@app.route('/pesan/<int:nomor_meja>', methods=['PUT'])
def update_antrian_status(nomor_meja):
    status = request.args.get('status')
    for antrian in antrian_restoran:
        if antrian['nomor_meja'] == nomor_meja:
            antrian['status'] = status
            return jsonify({'message': f'Status antrian untuk nomor meja {nomor_meja} diperbarui menjadi {status}'})

    return jsonify({'error': f'Nomor meja {nomor_meja} tidak ditemukan'}), 404

# Rute untuk melakukan pembayaran
@app.route('/pembayaran', methods=['POST'])
def pembayaran():
    data = request.get_json()
    pemesanan_id = data['pemesanan_id']
    total_harga = data['total_harga']

    pembayaran = Pembayaran(pemesanan_id=pemesanan_id, total_harga=total_harga)
    db.session.add(pembayaran)
    db.session.commit()

    return jsonify({'message': 'Pembayaran berhasil'}), 201
