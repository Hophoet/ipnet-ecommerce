from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class Fournisseur(models.Model):
	"""docstring for Fournisseur"""
	nom = models.CharField(max_length=100, verbose_name="Nom du fournisseur ")
	telephone = models.IntegerField(verbose_name="Téléphone du fournisseur ")

	class Meta:
		"""docstring for Meta"""
		unique_together = ['nom']

	def __str__(self):
		return "{}".format(self.nom)


class Categorie(models.Model):
	"""docstring for Category"""
	nom = models.CharField(max_length=100, verbose_name="Nom de la catégorie ")
	description = models.TextField()
	categorieParent = models.ForeignKey('self', on_delete = models.SET_NULL, null=True, blank=True, verbose_name="Catégorie parent ")
	
	class Meta:
		"""docstring for Meta"""
		unique_together = ['nom']

	def __str__(self):
		return "{}".format(self.nom)
			

class Produit(models.Model):
    nom = models.CharField(max_length=100, verbose_name="Nom du produit ")
    prix = models.FloatField()
    caracteristique = models.TextField(verbose_name="Caractéristique ")
    quantite = models.IntegerField(verbose_name="Quantité ")
    categorie = models.ForeignKey('Categorie', on_delete = models.CASCADE, verbose_name="Catégorie ")
    fournisseur = models.ForeignKey('Fournisseur', on_delete = models.CASCADE, verbose_name="Fournisseur ")


    def __str__(self):
    	return "{}".format(self.nom)

def envoi_image_nom(instance, filename):
    title = instance.produit.nom
    slug = slugify(title)
    return "post_images/%s-%s" % (slug, filename)


class Images(models.Model):
    produit = models.ForeignKey('Produit', on_delete = models.CASCADE, default=None)
    image = models.ImageField(upload_to=envoi_image_nom, null=True, blank=True, verbose_name='Image')

    def __str__(self):
    	return "{}".format(self.image)
