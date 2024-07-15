from django.db import models

class Bicicleta(models.Model):
    id_bicicleta = models.AutoField(db_column='idBicicleta', primary_key=True)
    tipo_bicicleta = models.CharField(max_length=20, blank=False, null=False)

    def python__str__(self):
        return self.tipo_bicicleta

class Cliente(models.Model):
    rut = models.CharField(primary_key=True, max_length=10)
    nombre = models.CharField(max_length=20)
    fecha_nacimiento = models.DateField(blank=False, null=False)
    id_bicicleta = models.ForeignKey('Bicicleta', on_delete=models.CASCADE, db_column='idBicicleta')
    telefono = models.CharField(max_length=45)
    email = models.EmailField(unique=True, max_length=100, blank=True, null=True)
    direccion = models.CharField(max_length=50, blank=True, null=True)
    activo = models.IntegerField()

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['rut']

