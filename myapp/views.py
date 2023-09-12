from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from datetime import date,datetime,timezone
# from .serializer import Serializer
# Create your views here.
datetime.utcnow()
@api_view()
def api(request):
     curent_day = datetime.today().strftime('%A')

     context = [
           {
          "slack_name":"Nurudeen",
          "current_day":curent_day,
          # "utc_time":datetime.now(),
          # "utc_tim":datetime.utcnow(),
          "utc_time": datetime.now(timezone.utc),
          "track": "backend",
          "github_file_url": "https://github.com/NurudeenNajeem/zur",
          "github_file_repo":"github.com/NurudeenNajeem",
          "status_code":status.HTTP_200_OK

     }

     ]
    
     return Response(context)


