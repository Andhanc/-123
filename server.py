from flask import Flask, jsonify
from db.db_factory import get_db
app = Flask(__name__)

@app.route('/shops')
def get_shops():
    db = get_db()
    _shops = db.shops.find()
    shops = [{"id": shop["id"], "name": shop["name"]} for shop in _shops]
    return jsonify({"shops": shops})

@app.route('/api')
def get_data():
    return {'message': 'Hello from Flask!'}

if __name__ == '__main__':
    app.run(debug=True)
