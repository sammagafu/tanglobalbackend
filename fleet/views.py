from rest_framework import viewsets,generics
from rest_framework.parsers import MultiPartParser, FormParser
from .models import Vehicle,VehicleImage,VehicleType
from rest_framework.permissions import IsAuthenticated
from .serializers import VehicleSerializer,VehicleImageSerializer,VehicleTypeSerializer
from rest_framework.response import Response

class VehicleCreateList(generics.ListCreateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class VehicleDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    parser_classes = (MultiPartParser, FormParser)
    permission_classes = [IsAuthenticated]


class VehicleTypeView(generics.ListCreateAPIView):
    queryset = VehicleType.objects.all()
    serializer_class = VehicleTypeSerializer


class ApproveVehicleView(generics.UpdateAPIView):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.isApproved = True
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)