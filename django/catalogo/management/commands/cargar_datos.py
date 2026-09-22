from django.core.management.base import BaseCommand
from catalogo.models import Categoria, Producto

class Command(BaseCommand):
    help = 'Carga datos de ejemplo para el laboratorio de MVT'

    def handle(self, *args, **options):
        Producto.objects.all().delete()
        Categoria.objects.all().delete()

        perifericos = Categoria.objects.create(nombre='Periféricos')
        monitores = Categoria.objects.create(nombre='Monitores')

        Producto.objects.create(
            categoria=perifericos, nombre='Teclado', precio=24990, stock=15)
        Producto.objects.create(
            categoria=perifericos, nombre='Mouse', precio=9990, stock=30)
        Producto.objects.create(
            categoria=monitores, nombre='Monitor 24"', precio=129990, stock=5)
        Producto.objects.create(
            categoria=monitores, nombre='Monitor 27"', precio=189990, stock=0, activo=False)

        self.stdout.write(self.style.SUCCESS('Datos de ejemplo cargados.'))
