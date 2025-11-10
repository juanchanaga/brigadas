from django.db import models

class Familia(models.Model):
    nombre = models.CharField(max_length=200)
    direccion = models.CharField(max_length=255, blank=True, null=True)
    condiciones_socioeconomicas = models.TextField(blank=True, null=True)
    numero_integrantes = models.PositiveIntegerField(blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} ({self.numero_integrantes or 'N/D'} miembros)"

class TipoAyuda(models.Model):
    OPCIONES = [
        ('Alimentaria','Alimentaria'),
        ('Educativa','Educativa'),
        ('Económica','Económica'),
        ('Médica','Médica'),
        ('Otros','Otros'),
    ]
    nombre = models.CharField(max_length=50, choices=OPCIONES)
    descripcion = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.nombre

class Voluntario(models.Model):
    ROLES = [
        ('Administrador','Administrador'),
        ('Coordinador','Coordinador'),
        ('Voluntario','Voluntario'),
    ]
    nombre = models.CharField(max_length=200)
    rol = models.CharField(max_length=20, choices=ROLES)
    contacto = models.CharField(max_length=150, blank=True, null=True)

    def __str__(self):
        return f"{self.nombre} - {self.rol}"

class Entrega(models.Model):
    fecha_entrega = models.DateField()
    familia = models.ForeignKey(Familia, on_delete=models.CASCADE, related_name='entregas')
    tipo_ayuda = models.ForeignKey(TipoAyuda, on_delete=models.PROTECT)
    voluntario = models.ForeignKey(Voluntario, on_delete=models.SET_NULL, null=True, blank=True)
    observaciones = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Entrega {self.id} - {self.familia.nombre} - {self.fecha_entrega}"

class Seguimiento(models.Model):
    familia = models.ForeignKey(Familia, on_delete=models.CASCADE, related_name='seguimientos')
    fecha = models.DateField()
    comentarios = models.TextField(blank=True, null=True)
    evaluacion_impacto = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return f"Seguimiento {self.id} - {self.familia.nombre} - {self.fecha}"
