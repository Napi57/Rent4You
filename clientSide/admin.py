from django.contrib import admin
from . import models
# Register your models here.


@admin.register(models.Dépot)
class DépotAdmin(admin.ModelAdmin):
    list_display = ['id', 'adress_dpt','capacité_dpt', 'id_agence']


@admin.register(models.Véhicule)
class VéhiculeAdmin(admin.ModelAdmin):
    list_display = ['id', 'matricule','img_vhl', 'prix_heure', 'prix_jour','marque','model', 'description','etat_véhicule','disponibilité','catégorie_véhicule','id_dépot']
    list_editable = ['etat_véhicule', 'catégorie_véhicule','img_vhl','marque','model', 'id_dépot', 'description','prix_jour']


admin.site.register(models.Locataire)
admin.site.register(models.Réservation)


@admin.register(models.Agence)
class AgenceAdmin(admin.ModelAdmin):
    list_display = ['id', 'nom_agence','siége_agence', 'num_contact', 'email_agence', 'nmbr_succursales', 'nmbr_flotte', 'logo_agence']


admin.site.register(models.Avis)

admin.site.register(models.Contrat_location)
admin.site.register(models.Facture)






