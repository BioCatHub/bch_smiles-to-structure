import os

from flask import Flask, send_file
from cairosvg import svg2png

app = Flask(__name__)


@app.route("/<smiles>", methods=["GET"])
def convert_smiles_to_molecule_image(smiles):
    os.system('obabel -:"{}" -O molecule.svg'.format(smiles))
    svg = open("molecule.svg", "rb")
    svg2png(file_obj=svg, write_to='molecule.png')
    return send_file('molecule.png', mimetype='image/png')


if __name__ == '__main__':
    app.run()
