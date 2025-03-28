from flask import Blueprint, jsonify, request, Response
import pandas as pd
from flask_cors import CORS

bp = Blueprint('routes', __name__)

df = pd.read_csv('Relatorio_cadop.csv')

@bp.route('/', methods=['GET'])
def index():
    try:
        search = request.args.get('search', '')
        field = request.args.get('field', '')
        page = int(request.args.get('page', 1))
        per_page = 15

        if not search and not field:
            filtered_df = df.copy()
        else:
            filtered_df = df[df[str(field)].str.contains(search, case=False, na=False)]

        filtered_df = filtered_df.fillna('')

        total_records = len(filtered_df)
        start = (page - 1) * per_page
        end = start + per_page
        paginated_results = filtered_df.iloc[start:end].to_dict(orient='records')

        return jsonify({
            "data": paginated_results,
            "total": total_records,
            "per_page": per_page,
            "current_page": page
        })

    except Exception as err:
        return Response("Access denied", status=403)
