from ..media.models import Categoria

def inject_categoria(request):
    return {
        'categoria': Categoria.objects.all(),
    }
