from rest_framework import generics
from .models import User
from .serializers import UserSerializer
from django.db.models import Q

# GET /users + POST /users
class UserListCreateView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.all()

        # search
        search = self.request.query_params.get('search')
        if search:
            queryset = queryset.filter(
                Q(name__icontains=search) |
                Q(email__icontains=search)
            )

        # sorting
        sort = self.request.query_params.get('sort')
        order = self.request.query_params.get('order', 'asc')

        if sort:
            if order == 'desc':
                sort = f'-{sort}'
            queryset = queryset.order_by(sort)

        return queryset


# GET /users/:id, PUT, DELETE
class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer