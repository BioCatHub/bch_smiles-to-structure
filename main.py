import os

from flask import Flask

app = Flask(__name__)


@app.route("/<smiles>", methods=["GET"])
def map(smiles):
    os.system('obabel -:"{}" -O molecule.svg'.format(smiles))
    return open("molecule.svg", "r").read()


if __name__ == '__main__':
    app.run()
