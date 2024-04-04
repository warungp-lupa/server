from flask import app, jsonify, request
import psycopg2

def create_connection():
    conn = psycopg2.connect(
        dbname="palupi",
        user="postgresql",
        password="11111"
    )
    return conn

@app.route('/tambah_pembayaran', methods=['POST'])
def tambah_pembayaran():
    conn = create_connection()
    cur = conn.cursor()
    
    # Mendapatkan data pembayaran dari request
    data = request.get_json()
    nama_pelanggan = data['nama_pelanggan']
    jumlah_pembayaran = data['jumlah_pembayaran']

    try:
        # Menambahkan pembayaran ke database
        cur.execute("INSERT INTO pembayaran (nama_pelanggan, jumlah_pembayaran) VALUES (%s, %s)", (nama_pelanggan, jumlah_pembayaran))
        conn.commit()
        return jsonify({'status': 'sukses', 'pesan': 'Pembayaran berhasil ditambahkan'})
    except Exception as e:
        conn.rollback()
        return jsonify({'status': 'gagal', 'pesan': str(e)})
    finally:
        cur.close()
        conn.close()