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

        client_type = list(request.GET.keys())[0]
        dates = self.request.query_params.getlist('date')

        if len(dates) == 0:
            raise APIException(detail='Nothing date found', code=status.HTTP_400_BAD_REQUEST)

        customer_fee = CustomerFee.objects.filter(client_type__iexact=client_type).all()
        if len(customer_fee) == 0:
            raise APIException(detail='Bad request. Client type not found',
                               code=status.HTTP_400_BAD_REQUEST)

        weekday = 0
        weekend = 0
        for date in dates:
            try:
                date = datetime.strptime(date, '%d/%m/%Y')

                weekday, weekend = (weekday + 1, weekend) if date.isoweekday() < 6 else (weekday, weekend + 1)
            except:
                raise APIException(detail='Invalid date', code=status.HTTP_400_BAD_REQUEST)

        min_value = sys.float_info.max

        hotel = ''

        for cf in customer_fee:

            fee = cf.weekday_rate * weekday + cf.weekend_rate * weekend

            if fee < min_value:
                min_value = fee
                hotel = cf.hotel
            elif fee == min_value:
                hotel = hotel if hotel.classification > cf.hotel.classification else cf.hotel

        return Response(status=status.HTTP_200_OK, data={'cheapest': hotel.name})


