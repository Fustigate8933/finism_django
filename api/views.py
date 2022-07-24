from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from datetime import timezone
import datetime as dt
import pandas_datareader.data as web
import json
import sys
sys.path.append('api')
from backend import Finism

finism = Finism()
stocks = finism.stock_history()
crypto = finism.crypto_live()
stocks = json.loads(stocks)
crypto = json.loads(crypto)

class GetStock(APIView):
    def get(self, request, format=None):
        return Response(stocks, status=status.HTTP_200_OK)

class GetCrypto(APIView):
    def get(self, request, format=None):
        return Response(crypto, status=status.HTTP_200_OK)
