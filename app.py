from flask import Flask, render_template, request
import json
from Classes.Engine import Engine
from Classes.Config import Config

options = {
    "leet_min": False,
    "leet_maj": False,
    "leet_all": False,
    "to_capitalize": True,
    "to_upper": True,
    "to_lower": True,
    "remove_accents": True,
    "common_characteres": True,
    "all_characteres": False,
    "n_characteres": False,
    "get_day_number": False,
    "get_month_number": False,
    "get_year_number": False,
    "get_day_text": False,
    "get_month_text": False,
    "get_year_number_two_digits": False
}

langs = [
    Config.get_default_language()
]

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/donnees', methods=['POST'])
def donnees():
    data = request.get_json()
    # Accès aux valeurs
    word_values = data['word']
    date_values = data['date']
    engine = Engine(word_values, date_values, options, langs)
    return json.dumps(engine.listeFinal)

if __name__ == "__main__":
    app.run(debug=False, host="localhost", port=5000)