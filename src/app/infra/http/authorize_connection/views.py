# Create your views here.
from django.views import View
from django.http import JsonResponse, HttpResponse
from werkzeug.exceptions import HTTPException
import json
from django.shortcuts import redirect, render
from app.infra.trading_api.trading_api import TradingOperations
from pprint import pprint

class GetSite(View):
    
    def get(self, request):
        try:
            # req = json.loads(request.body)
            # store_code = req["store_code"]
            # client_id = req["client_id"]
            # client_secret = req["client_secret"]
            # provider_name = req["provider_name"]
            # return JsonResponse({"url": "url"}, status=200)
            resp = TradingOperations().get_info()
            pprint(resp.json())
            # ctx = {}
            ctx = {
                'labels': ["eua", "mexico", "brazil"],
                'data': ["1","2", "3"],
            }
            return render(request, 'service/pie_chart.html', ctx)
        except Exception as ex:
            raise(ex)
            return JsonResponse({"msg": "error"}, status=400)
