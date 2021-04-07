from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

# user model
Utilisateur = settings.AUTH_USER_MODEL


class Fournisseur(models.Model):
    """docstring for Fournisseur"""
    nom = models.CharField(max_length=100, verbose_name="Nom du fournisseur ")
    telephone = models.IntegerField(verbose_name="Téléphone du fournisseur ")
    adresse = models.TextField()
    email = models.EmailField()
    estPerson = models.BooleanField(default=False)

    class Meta:
        """docstring for Meta"""
        unique_together = ['nom']

    def __str__(self):
        return "{}".format(self.nom)


class Categorie(models.Model):
	"""docstring for Category"""
	nom = models.CharField(max_length=100, verbose_name="Nom de la catégorie")
	description = models.TextField()
	categorieMere = models.ForeignKey('Categorie', on_delete=models.CASCADE, related_name='categorie_mere', null=True, blank=True)
	
	class Meta:
		"""docstring for Meta"""
		unique_together = ['nom']
		
		def __str__(self):
			return "{}".format(self.nom)


class Produit(models.Model):
    nom = models.CharField(max_length=100, verbose_name="Nom du produit")
    prix = models.FloatField()
    diminu_price = models.FloatField(null=True, blank=True)
    caracteristique = models.TextField(verbose_name="Caractéristique")
    quantite = models.IntegerField(verbose_name="Quantité")
    categories = models.ManyToManyField(Categorie, related_name='Categories')
    fournisseur = models.ForeignKey(
        'Fournisseur', on_delete=models.CASCADE, verbose_name="fournisseur_id")

    def __str__(self):
        return "{}".format(self.nom)

    def get_images(self):
        """ retour un type queryset des images associées au produit"""
        return self.image_set.get_queryset()

    def get_bonus_price(self):
        if self.diminu_price:
            return self.price - self.diminu_price
        return self.price

    def get_bonus_price_pourcentage(self):
        if self.diminu_price:
            return int( ( self.get_bonus_price() * 100 )/self.price )
        return int( ( self.get_bonus_price() * 100 )/self.price )



def envoi_image_nom(instance, filename):
    title = instance.produit.nom
    slug = slugify(title)
    return "post_images/%s-%s" % (slug, filename)


class Image(models.Model):
    produit = models.ForeignKey(
        'Produit', on_delete=models.CASCADE, default=None)
    url = models.ImageField(upload_to=envoi_image_nom, null=True, blank=True)

    def __str__(self):
        return "{}".format(self.url)


class Panier(models.Model):
    utilisateur = models.ForeignKey(Utilisateur, on_delete=models.CASCADE)
    estCommander = models.BooleanField(default=False)

    def get_prix_total(self):
        produits_a_commander = self.produitacommander_set.get_queryset()
        prix_total = 0
        for produit_a_commander in produits_a_commander:
            prix_total += produit_a_commander.quantite * produit_a_commander.produit.prix
        return prix_total


class ProduitACommander(models.Model):
    #utilisateur = models.ForeignKey(
    #    Utilisateur, on_delete=models.CASCADE)
    produit = models.ForeignKey('Produit', on_delete=models.CASCADE)
    panier = models.ForeignKey(
        'Panier', on_delete=models.CASCADE)
    quantite = models.IntegerField(verbose_name="Quantité")
    estCommander = models.BooleanField(default=False)
    #estCommander = models.BooleanField(default=False)

    def get_prix_total(self):
        return self.produit.prix * self.quantite

    #total disount produit price getter
    def get_total_diminu_produit_price(self):
        """Total diminu produit price getter """
        return self.produit.diminu_price * self.quantity

    #total saved ammount getter
    def get_bonus_total(self):
        return self.get_prix_total() - self.get_total_diminu_produit_price()

    #finale price getter
    def get_final_price(self):
        """finale price getter """
        if self.produit.diminu_price:
            return self.get_total_diminu_produit_price()
        return self.get_prix_total()


class Livraison(models.Model):
    date = models.DateTimeField()
    lieu = models.CharField(max_length=100)
    estLivrer = models.BooleanField(default=False)


class Commande(models.Model):
    date = models.DateTimeField()
    panier = models.OneToOneField(
        'Panier', on_delete=models.SET_NULL, null=True, blank=True)
    livraison = models.ForeignKey('Livraison', on_delete=models.CASCADE)
