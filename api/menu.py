from tkinter import Menu
from flask import app, jsonify
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from menu import *

Base = declarative_base()

engine = create_engine('postgresql://postgres:11111@localhost/palupi')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)

# Endpoint untuk mendapatkan seluruh menu
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