# BioCatHub Mol Structure

Microservice that converts SMILES codes to structure SVGs.

## Installation

- Install open babel 3: https://openbabel.org/wiki/Category:Installation
- Install pipfile ``pipenv install``

## Running the server

- ``python3 main.py``

## Access a structure SVG

- Call ``/<YOUR SMILES CODE>``
- Examples:
  - ``http://127.0.0.1:5000/C1=CC(=C[N+](=C1)C2C(C(C(O2)COP(=O)([O-])OP(=O)(O)OCC3C(C(C(O3)N4C=NC5=C(N=CN=C54)N)O)O)O)O)C(=O)N``
  - ``http://127.0.0.1:5000/c1ccccc1``