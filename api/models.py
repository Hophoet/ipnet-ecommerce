from django.db import models

#Item models
class Categorie(models.Model):
	"""docstring for Category"""
	nom = models.CharField(max_length=100, verbose_name="Nom de la catégorie ")
	description = models.TextField()

	class Meta(object):
		"""docstring for Meta"""
		unique_together = ['nom']

	def __str__(self):
		return "{}".format(self.nom)
			

class Produit(models.Model):
    nom = models.CharField(max_length=100, verbose_name="Nom du produit ")
    prix = models.FloatField()
    caracteristique = models.TextField(verbose_name="Caractéristique ")
    quantite = models.IntegerField(verbose_name="Quantité ")
    image = models.ImageField(upload_to='images/produits', null=True, blank=True)
    category = models.ForeignKey(Categorie, on_delete = models.CASCADE)


    def __str__(self):
    	return "{}".format(self.nom)
		