# minhaapp/api.py
from rest_framework import viewsets, generics
from rest_framework.response import Response
from rest_framework.decorators import action
from myapp.models import Produto
from myapp.serializers import ProdutoSerializer

class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer
    
    @action(detail=False, methods=['get'])
    def disponiveis(self, request):
        produtos = Produto.objects.filter(disponivel=True)
        serializer = self.get_serializer(produtos, many=True)
        return Response(serializer.data)
