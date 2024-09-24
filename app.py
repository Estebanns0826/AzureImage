from flask import Flask, jsonify, render_template, request
import requests

app = Flask(__name__)

# URL del endpoint de Azure para el modelo de ML
azure_endpoint = "https://maincraxd-prediction.cognitiveservices.azure.com/customvision/v3.0/Prediction/853c5ffe-9de8-4f03-ac03-5586ac847252/classify/iterations/pruebaproyecto/image"
subscription_key = "46136165095e4925b2ea68a1b5496e18"

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/enviar_imagen', methods=['POST'])
def recibir_clasificacion():
    file = request.files.get('image')
    if file:
        response = classify_image_with_azure(file.read())
        return jsonify(response)
    else:
        return jsonify({'error': 'No se recibió ninguna imagen'}), 400

def classify_image_with_azure(image_file):
    headers = {
        'Content-Type': 'application/octet-stream',
        'Prediction-Key': subscription_key
    }

    response = requests.post(azure_endpoint, headers=headers, data=image_file)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {'error': 'Error al clasificar la imagen'}, response.status_code

if __name__ == '__main__':
    app.run(debug=True)
