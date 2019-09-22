from flask import Flask, jsonify, request
import MySQLdb

db = MySQLdb.connect(host="db4free.net",
                     user="atendemesa",    
                     passwd="atendemesa", 
                     db="dbmesa")

app = Flask(__name__)

mesas = [
    {
        'id': 1,
        'Nome': 'Mesa 1',
        'Status': 'Livre',
        'Lugares': '5',
        'Garcom':'',
        'CodigoComanda':''
    },
    {
        'id': 2,
        'Nome': 'Mesa 2',
        'Status': 'Livre',
        'Lugares': '2',
        'Garcom':'',
        'CodigoComanda':''
    }
]

def CarregaMesas():
    cur = db.cursor() 
    cur.execute(""" SELECT * FROM Mesa; """)
    mesas.clear()
    for linha in cur.fetchall():
        mesa = {
            'id':linha[0],
            'Nome':linha[1],
            'Status':linha[2],
            'Lugares':linha[3],
            'Garcom':linha[4],
            'CodigoComanda':linha[5]
        }
        mesas.append(mesa)

def AlteraMesa(mesa):  
    cur = db.cursor() 
    query = "UPDATE Mesa SET Nome=%s, Status=%s, Lugares=%s, Garcom=%s, CodigoComanda=%s WHERE idMesa=%s"
    cur.execute(query, (mesa['Nome'], mesa['Status'], int(mesa['Lugares']), mesa['Garcom'], int(mesa['CodigoComanda']), int(mesa['id']) ))
    db.commit()
    CarregaMesas()

def RemoveMesa(id):
    cur = db.cursor() 
    query = "DELETE FROM Mesa WHERE idMesa = %s"
    cur.execute(query, (int(id),))
    db.commit()
    CarregaMesas()

@app.route('/mesa', methods=['GET'])
def home():
    CarregaMesas()
    return jsonify(mesas), 200


@app.route('/mesa/<string:status>', methods=['GET'])
def mesas_por_status(status):
    mesas_por_status = [mesa for mesa in mesas if mesa['Status'] == status]
    return jsonify(mesas_por_status), 200


@app.route('/mesa/<int:id>', methods=['PUT'])
def mudarStatus(id):
    for mesa in mesas:
        if mesa['id'] == id:
            mesa['Nome'] = request.get_json().get('Nome')
            mesa['Status'] = request.get_json().get('Status')
            mesa['Lugares'] = request.get_json().get('Lugares')
            mesa['Garcom'] = request.get_json().get('Garcom')
            mesa['CodigoComanda'] = request.get_json().get('CodigoComanda')
            AlteraMesa(mesa)
            return jsonify(mesa), 200

    return jsonify({'Erro': 'Mesa nao encontrada'}), 404


@app.route('/mesa/<int:id>', methods=['GET'])
def mesa_por_id(id):
    for mesa in mesas:
        if mesa['id'] == id:
            return jsonify(mesa), 200

    return jsonify({'Erro': 'Mesa nao encontrada'}), 404


@app.route('/mesa', methods=['POST'])
def adicionar_mesa():
    data = request.get_json()
      
    cur = db.cursor() 
    query = "INSERT INTO Mesa (Nome, Status, Lugares, Garcom, CodigoComanda)" \
        "VALUES (%s,%s,%s,%s,%s)"
    cur.execute(query, (data['Nome'], data['Status'], int(data['Lugares']), data['Garcom'], int(data['CodigoComanda']) ))
    db.commit()
    CarregaMesas()

    return jsonify(data), 201


@app.route('/mesa/<int:id>', methods=['DELETE'])
def remove_mesa(id):
    print("id a ser deletado: ",id)
    index = id - 1
    del mesas[index]
    RemoveMesa(id)

    return jsonify({'Sucesso': 'Mesa removida'}), 200


if __name__ == '__main__':
    CarregaMesas()
    app.run(debug=True)