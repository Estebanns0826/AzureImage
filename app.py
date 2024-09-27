from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/enviar_imagen', methods=['POST'])
def recibir_clasificacion():
    file = request.files.get('image')
    endpoint = request.form.get('endpoint')
    key = request.form.get('key')

    if file:
        response = classify_image_with_azure(file.read(), endpoint, key)
        return jsonify(response)
    else:
        return jsonify({'error': 'No se recibió ninguna imagen'}), 400

def classify_image_with_azure(image_file, endpoint, key):
    headers = {
        'Content-Type': 'application/octet-stream',
        'Prediction-Key': key
    }

    response = requests.post(endpoint, headers=headers, data=image_file)
    
    if response.status_code == 200:
        return response.json()
    else:
        print(f"Error {response.status_code}: {response.text}")
        return {'error': 'Error al clasificar la imagen', 'details': response.text}, response.status_code

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3500, debug=True)
