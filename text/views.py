from .scraper import quque
from django.shortcuts import render

import json


def index(request):
    if 'query' in request.GET.keys():
        query_text = request.GET.get('query')
        final_bobot = quque(query_text)
        chart_data = []
        for key in final_bobot:
            chart_data.append({'y': final_bobot[key], 'label': key})
        chart_data = json.dumps(chart_data)
        response = {'chart_data': chart_data, 'text': query_text}
        return render(request, 'search.html', response)
    else:
        return render(request, 'search.html', {'chart_data': []})
