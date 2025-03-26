from flask import Blueprint, jsonify, request
import pandas as pd

bp = Blueprint('routes', __name__)

df = pd.read_csv('Relatorio_cadop.csv')

@bp.route('/', methods=['GET'])
def index():
    print(f'1')
    termo = request.args.get('termo', '')
    print(f'2')
    if termo:
        results = df[df.apply(lambda row: row.astype(str).str.contains(termo, case=False).any(), axis=1)]
    else:
        results = df
    print(f'3')
    results_dict = results.to_dict(orient='records')
    return jsonify(results_dict)