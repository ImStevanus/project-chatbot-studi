import json

def muat_data():
    """Membuka file matakuliah.json dan mengembalikan isinya sebagai dictionary"""
    try:
        with open('matakuliah.json', 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return None