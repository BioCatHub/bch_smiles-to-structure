import os

from flask import Flask, send_file
from cairosvg import svg2png
from flask_cors import CORS

app = Flask(__name__)
CORS(app, resources={r'/*':{'origins':'*'}})


@app.route("/smiles/<smiles>", methods=["GET"])
def convert_smiles_to_molecule_image(smiles):
    os.system('obabel -:"{}" -O molecule.svg'.format(smiles))
    svg = open("molecule.svg", "rb")
    svg2png(file_obj=svg, write_to='molecule.png')
    return send_file('molecule.png', mimetype='image/png')


if __name__ == '__main__':
    #app.run(debug=True, host='0.0.0.0', port=8000)
    app.run(debug=True, port=5000)