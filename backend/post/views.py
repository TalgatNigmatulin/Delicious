from rest_framework import generics, permissions
from post.models import Products, Comment
from post.serializers import PostSerializer, CommentSerializers
from rest_framework import filters
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets

class ProductsListPagination(PageNumberPagination):
    page_size = 15
    page_size_query_param = 'page_size'
    max_page_size = 10000




class ProductsList(generics.ListAPIView):
    queryset = Products.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['name', 'price']
    pagination_class = ProductsListPagination 


class ProductDetail(generics.RetrieveAPIView):
    queryset = Products.objects.all()
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAdminUser,]


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializers







