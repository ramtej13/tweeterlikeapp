from demo.models import test,PetsDetails,Pets
from rest_framework import viewsets
from .serializers import testSerializer,petsSerializer,UserDetails
from django.contrib.auth.models import User
from rest_framework import generics
from rest_framework import mixins

class TestViewSet(viewsets.ModelViewSet):
    serializer_class = testSerializer
    queryset = test.objects.all()

class PetsViewSet(viewsets.ModelViewSet):
    serializer_class = petsSerializer
    queryset = PetsDetails.objects.all()

class UserDetails(viewsets.ModelViewSet):
    serializer_class = UserDetails
    queryset = Pets.objects.filter()



class GenericAPIView(generics.GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin,
                     mixins.UpdateModelMixin, mixins.RetrieveModelMixin,
                     mixins.DestroyModelMixin):
    serializer_class = testSerializer
    queryset = test.objects.all()
    lookup_field = 'id'

    def get(self, request, id=None):

        if id:
            return self.retrieve(request)

        else:
            return self.list(request)

    def post(self, request):
        return self.create(request)

    def put(self, request, id=None):
        return self.update(request, id)

    def delete(self, request, id):
        return self.destroy(request, id)


# class ArticleViewSet(viewsets.ModelViewSet):
#     serializer_class = testSerializer
#     queryset = test.objects.all()


# class TestListView(ListAPIView):
#     queryset = test.objects.all()
#     serializer_class = testSerializer

# class TestDetailView(RetrieveAPIView):
#     queryset = test.objects.all()
#     serializer_class = testSerializer