from .models import ValidParametres
from .serializer import ValParSerializer
from rest_framework import generics


class CheckPar(generics.CreateAPIView):
    queryset = ValidParametres.objects.all()
    serializer_class = ValParSerializer

    def perform_create(self, serializer):
        serializer.save()


class ValParList(generics.ListCreateAPIView):
    serializer_class = ValParSerializer

    def get_queryset(self):
        queryset = ValidParametres.objects.all()
        ipaddress = self.request.query_params.get('ipaddress')
        if ipaddress is not None:
            queryset = queryset.filter(ipaddress=ipaddress)
        return queryset