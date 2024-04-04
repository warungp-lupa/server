from flask import app, jsonify, request

# Rute untuk mendapatkan pesanan
@app.route('/pesan', methods=['GET'])
def pesan():
    return jsonify({'pesan': update_antrian_status})

# Rute untuk menambahkan nomor meja ke dalam antrian
@app.route('/pesan', methods=['POST'])
def add_to_antrian():
    data = request.get_json()
    nomor_meja = data.get('nomor_meja')

    if not nomor_meja:
        return jsonify({'error': 'Nomor meja harus disertakan'}), 400

    update_antrian_status.append({'nomor_meja': nomor_meja, 'status': 'menunggu'})
    return jsonify({'message': f'Nomor meja {nomor_meja} telah ditambahkan ke dalam antrian'})

# Rute untuk memperbarui status antrian (misalnya: dipanggil, selesai)
@app.route('/pesan/<int:nomor_meja>', methods=['PUT'])
def update_antrian_status(nomor_meja):
    status = request.args.get('status')
    for antrian in update_antrian_status:
        if antrian['nomor_meja'] == nomor_meja:
            antrian['status'] = status
            return jsonify({'message': f'Status antrian untuk nomor meja {nomor_meja} diperbarui menjadi {status}'})

    return jsonify({'error': f'Nomor meja {nomor_meja} tidak ditemukan'}), 404