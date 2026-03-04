from django.db import models

class Videojoc(models.Model):
    titol = models.CharField(max_length=100)
    plataforma = models.CharField(max_length=50)
    preu = models.DecimalField(max_digits=8, decimal_places=2)
    stock = models.PositiveIntegerField(default=0)
    venudes = models.PositiveIntegerField(default=0)

    @property
    def a_reabastir(self):
        """Calcula si cal reabastir (si stock < 5)"""
        return self.stock < 5

    def __str__(self):
        return f"{self.titol} ({self.plataforma})"

class Client(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.nom

class Comanda(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    videojocs = models.ManyToManyField(Videojoc)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Comanda #{self.id} - {self.client.nom}"
