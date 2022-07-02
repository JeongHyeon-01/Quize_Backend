from rest_framework import generics
from cores.decorator import login_authorization
from cores.permissions import CustomReadOnly
from supports.models import Support
from supports.serializers import SupportSerializers, SupprotDetailSerializers
from rest_framework.response         import Response

from users.models import User


class SupportPublicUser(generics.ListCreateAPIView):
    queryset = Support.objects.all()
    serializer_class = SupportSerializers

    @login_authorization
    def create(self, request):
        serializer = SupportSerializers(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data, status=201)
        return Response(serializer.errors)


class SupportCustomUser(generics.RetrieveUpdateDestroyAPIView):
    queryset = Support.objects.all()
    serializer_class = SupprotDetailSerializers
    permission_classes = [CustomReadOnly,]

    
        

