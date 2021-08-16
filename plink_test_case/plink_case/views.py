from .models import ValidParametres
from .serializer import ValParSerializer
from rest_framework import generics


class CheckPar(generics.CreateAPIView):
    queryset = ValidParametres.objects.all()
    serializer_class = ValParSerializer


class ValParList(generics.ListCreateAPIView):
    queryset = ValidParametres.objects.all()
    serializer_class = ValParSerializer