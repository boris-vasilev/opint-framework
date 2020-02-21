from rest_framework import viewsets
from rest_framework.response import Response

from opint_framework.apps.example_app.models import SampleModel
from opint_framework.apps.example_app.api.serializers import SampleSerializer


class SampleViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows SampleModel to be viewed or edited.
    """
    queryset = SampleModel.objects.all()
    serializer_class = SampleSerializer

    def index(request):
        return Response({"Result":"OK"})

