# Create your views here.
from django.views import View
from django.http import JsonResponse
from werkzeug.exceptions import HTTPException
import json
from django.shortcuts import redirect

class GetSite(View):
    
    def get(self, request):
        try:
            req = json.loads(request.body)
            # store_code = req["store_code"]
            # client_id = req["client_id"]
            # client_secret = req["client_secret"]
            # provider_name = req["provider_name"]
            return JsonResponse({"url": "url"}, status=200)
        except Exception as ex:
            print(ex)
            return JsonResponse({"msg": "error"}, status="400")
