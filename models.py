from app import db
from sqlalchemy.orm import Session


class Menu(db.Model):
    id_menu = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    harga = db.Column(db.Integer)
    kuantitas = db.Column(db.Integer)
    deskripsi = db.Column(db.String)

class Pemesanan(db.Model):
    id_pembeli = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(50))
    alamat = db.Column(db.String(50))
    telp = db.Column(db.String(15))
    pesan = db.Column(db.String(50))
    makanditempat = db.Column(db.Boolean())

class User(db.Model):
    id_user = db.Column(db.Integer, primary_key=True)
    password = db.Column(db.String(20))

class Pembayaran(db.Model):
    id_pembayaran = db.Column(db.Integer, primary_key=True)
    id_pembeli = db.Column(db.Integer, db.ForeignKey('pemesanan.id_pembeli'))
    opsi_bayar = db.Column(db.String(20))
    total_harga = db.Column(db.Integer)
