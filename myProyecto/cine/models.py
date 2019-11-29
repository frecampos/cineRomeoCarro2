from django.db import models

# Create your models here.
class Categoria(models.Model):
    name=models.CharField(max_length=100,primary_key=True)
    calificacion=models.IntegerField()

    def __str__(self):
        return self.name

class Pelicula(models.Model):
    name=models.CharField(max_length=100,primary_key=True)
    duracion=models.IntegerField()
    precio=models.IntegerField()
    descripcion=models.TextField()
    categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE)
    #creamos un campo de tipo Imagen que se carga en el directorio
    # pelis ubicado en "media"
    imagen=models.ImageField(upload_to="pelis",null=True)

    def __str__(self):
        return self.name

class Ticket(models.Model):
    usuario=models.CharField(max_length=100)
    titulo=models.CharField(max_length=100)
    precio=models.IntegerField()
    cantidad=models.IntegerField()
    total=models.IntegerField()
    fecha=models.DateField()

    def __str__(self):
        return str(self.usuario)+' '+str(self.titulo)