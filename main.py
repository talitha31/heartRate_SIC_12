from flask import Flask, request

app = Flask(__name__)

# Rute untuk menerima data melalui metode GET
Data = []
@app.route('/get_data', methods=['GET'])
def get_data():
    # data = request.args.get('data')
    # Lakukan pemrosesan data sesuai kebutuhan
    print(f'Data received via GET: ')
    return Data

# Rute untuk menerima data melalui metode POST
@app.route('/post_data', methods=['POST'])
def post_data():
    data = request.form.get('data')
    # Lakukan pemrosesan data sesuai kebutuhan
    print(f'Data received via POST: {data}')
    Data.append(data)
    return ('Data post')
    
# Rute untuk menerima data melalui metode PUT

if __name__ == '__main__':
    app.run(host='0.0.0.0')