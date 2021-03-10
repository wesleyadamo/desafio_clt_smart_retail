# Create your views here.
import sys
from datetime import datetime

from rest_framework import status
from rest_framework.exceptions import APIException
from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response

from hotel.models import CustomerFee


class CheapestHotel(RetrieveAPIView):

    def get(self, request, *args, **kwargs):
        query_params = self.request.query_params

        client_type = list(request.GET.keys())[0]
        # recupera a taxa do cliente de acordo com o seu tipo passado por parametro na requisição
        customer_fee = CustomerFee.objects.filter(client_type__iexact=client_type).all()
        # verifica se foi retornado algum valor na consulta
        if len(customer_fee) == 0:
            raise APIException(detail='Bad request. Client type not found', code=status.HTTP_400_BAD_REQUEST)

        weekday = 0
        weekend = 0
        # percorre todos
        for x in query_params.values():
            try:
                date = datetime.strptime(x, '%d/%m/%Y')
                '''
                   soma mais 1 em weekday se a data for em um dia da semana (<6),
                   caso contrario, soma mais 1 em weekend
                '''
                weekday, weekend = (weekday + 1, weekend) if date.isoweekday() < 6 else (weekday, weekend + 1)
            except:
                continue

        if weekend == 0 and weekday == 0:
            raise APIException(detail='Nothing date found', code=status.HTTP_400_BAD_REQUEST)

        min_value = sys.float_info.max

        hotel = ''

        for ce in customer_fee:
            fee = ce.weekday_rate * weekday + ce.weekend_rate * weekend

            if fee < min_value:
                min_value = fee
                hotel = ce.hotel
            elif fee == min_value:
                hotel = hotel if hotel.classification > ce.hotel.classification else ce.hotel

        return Response(status=status.HTTP_200_OK, data={'cheapest': hotel.name})
