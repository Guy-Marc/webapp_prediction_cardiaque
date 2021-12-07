from flask import Flask, render_template, request, flash
import numpy as np
import pickle

app = Flask(__name__)
model = pickle.load(open('modele.pkl', 'rb'))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/post-predict', methods=['POST'])
def predict():
    for x in request.form.values():
        if not x:
            erreur = "tous les champs sont necessaires"
            return render_template('index.html', erreur=erreur)
    input_valeur = [float(x) for x in request.form.values()]
    tab_np = np.array(input_valeur)
    tab_np = np.reshape(tab_np, (1, -1))

    pred = model.predict(tab_np)
    return render_template('index.html', predict=pred)


if __name__ == "__main__":
    app.run(debug=True)
