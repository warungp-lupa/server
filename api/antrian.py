from flask import app, jsonify, request
from app import db
from models import Antrian

# Route untuk menambahkan antrian
@app.route('/tambah_antrian', methods=['POST'])
def tambah_antrian():
    data = request.get_json()
    nama_pelanggan = data.get('nama_pelanggan')
    
    # Untuk mendapatkan nomor antrian terakhir
    nomor_terakhir = Antrian.query.order_by(Antrian.nomor_antrian.desc()).first()
    nomor_antrian_baru = 1 if nomor_terakhir is None else nomor_terakhir.nomor_antrian + 1
    
    antrian_baru = Antrian(nama_pelanggan=nama_pelanggan, nomor_antrian=nomor_antrian_baru)
    
    try:
        db.session.add(antrian_baru)
        db.session.commit()
        return jsonify({'message': 'Antrian berhasil ditambahkan'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

# Route untuk melihat daftar antrian
@app.route('/daftar_antrian', methods=['GET'])
def daftar_antrian():
    try:
        daftar_antrian = Antrian.query.all()
        antrian_list = []
        for antrian in daftar_antrian:
            antrian_info = {
                'id': antrian.id,
                'nama_pelanggan': antrian.nama_pelanggan,
                'nomor_antrian': antrian.nomor_antrian
            }
            antrian_list.append(antrian_info)
        
        return jsonify(antrian_list), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500
