from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

# Importing pickle files
model = pickle.load(open('classifier.pkl', 'rb'))
ferti = pickle.load(open('fertilizer.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('plantindex.html')

@app.route('/Model1')
def Model1():
    return render_template('Model1.html')

@app.route('/Detail')
def Detail():
    return render_template('Detail.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Fetching input values from the form
        temp = float(request.form.get('temp'))
        humi = float(request.form.get('humid'))
        mois = float(request.form.get('mois'))
        soil = int(request.form.get('soil'))
        crop = int(request.form.get('crop'))
        nitro = int(request.form.get('nitro'))
        pota = int(request.form.get('pota'))
        phosp = int(request.form.get('phos'))

        # Input feature list
        features = [temp, humi, mois, soil, crop, nitro, pota, phosp]

        # Predict using the model
        prediction_index = model.predict([features])[0]  # e.g., 2
        result = ferti.classes_[prediction_index]         # e.g., 'Urea'

        # Return prediction result
        return render_template('Model1.html', x=result)

    except (TypeError, ValueError):
        return render_template('Model1.html', x='Invalid input. Please ensure all fields contain valid numbers.')

if __name__ == "__main__":
    app.run(debug=True)
