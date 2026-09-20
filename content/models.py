# content/models.py
from django.db import models


def default_hero_stats():
    return [
        {"num": "100%", "label": "Naturel"},
        {"num": "12+", "label": "Formules"},
        {"num": "Vegan", "label": "Certifié"},
    ]


def default_marquee_items():
    return ["Hydratation profonde", "Boucles définies", "Sans sulfate", "Vegan", "Naturel", "Afro Cure", "Karité & Ricin"]


def default_feature_cards():
    return [
        {"icon": "sparkles", "title": "Hydrater profondément", "body": "Des formules riches en acide hyaluronique et céramides pour une hydratation durable et intense qui transforme chaque fibre."},
        {"icon": "heart", "title": "Réparer et renforcer", "body": "Des actifs réparateurs et protéines soigneusement sélectionnés pour redonner force et élasticité à vos cheveux."},
        {"icon": "leaf", "title": "Stimuler la croissance", "body": "Des sérums enrichis en MSM et niacinamide pour une pousse visible, un cuir chevelu sain et revitalisé."},
    ]


def default_cta_pills():
    return [
        {"icon": "leaf", "title": "Ingrédients naturels", "body": "Karité, ricin, aloe vera et extraits africains"},
        {"icon": "sparkles", "title": "Formules scientifiques", "body": "Acide hyaluronique, céramides, MSM et niacinamide"},
        {"icon": "heart", "title": "100% Vegan", "body": "Certifié cruelty-free, sans sulfate ni silicone"},
    ]


class HomeContent(models.Model):
    # Hero
    hero_eyebrow = models.CharField(max_length=200, default="Afro Cure — Maison de soins")
    hero_title_line1 = models.CharField(max_length=200, default="L'élégance")
    hero_title_emphasis = models.CharField(max_length=200, default="naturelle")
    hero_title_line2 = models.CharField(max_length=200, default="des cheveux")
    hero_subtitle = models.TextField(
        default="Des soins luxueux pour cheveux texturés. Combinant science cosmétique et plantes africaines."
    )
    hero_cta_primary_label = models.CharField(max_length=100, default="Découvrir nos soins")
    hero_cta_secondary_label = models.CharField(max_length=100, default="Notre histoire")
    hero_stats = models.JSONField(default=default_hero_stats)  # [{num, label}]
    hero_image = models.ImageField(upload_to='content/', blank=True, null=True)

    # Marquee
    marquee_items = models.JSONField(default=default_marquee_items)  # [str]

    # "Pourquoi Afro Cure" features
    features_eyebrow = models.CharField(max_length=200, default="Notre Philosophie")
    features_title_plain = models.CharField(max_length=200, default="Pourquoi")
    features_title_emphasis = models.CharField(max_length=200, default="Afro Cure ?")
    features_description = models.TextField(
        default="Une gamme développée pour répondre aux besoins majeurs des cheveux texturés."
    )
    feature_cards = models.JSONField(default=default_feature_cards)  # [{icon, title, body}]

    # Products section header
    products_eyebrow = models.CharField(max_length=200, default="Sélection")
    products_title_plain = models.CharField(max_length=200, default="Produits")
    products_title_emphasis = models.CharField(max_length=200, default="Vedettes")
    products_description = models.TextField(
        default="Découvrez nos soins les plus populaires, plébiscités par notre communauté."
    )
    products_footer_label = models.CharField(max_length=100, default="Voir tous les produits")

    # Bottom CTA
    cta_eyebrow = models.CharField(max_length=200, default="Routine Personnalisée")
    cta_title_plain = models.CharField(max_length=200, default="Révélez la beauté")
    cta_title_emphasis = models.CharField(max_length=200, default="de vos cheveux")
    cta_body = models.TextField(
        default="Une routine personnalisée pour des résultats visibles et durables. "
                "Chaque formule est pensée pour célébrer la beauté naturelle des cheveux texturés."
    )
    cta_button_label = models.CharField(max_length=100, default="En savoir plus")
    cta_pills = models.JSONField(default=default_cta_pills)  # [{icon, title, body}]
    cta_image = models.ImageField(upload_to='content/', blank=True, null=True)

    # Avis clients
    testimonials_eyebrow = models.CharField(max_length=200, default="Témoignages")
    testimonials_title_plain = models.CharField(max_length=200, default="Ce que disent")
    testimonials_title_emphasis = models.CharField(max_length=200, default="nos clientes")
    testimonials_description = models.TextField(
        default="Des retours authentiques de celles qui ont adopté nos soins au quotidien."
    )
    testimonials_form_label = models.CharField(max_length=200, default="Laisser un avis")

    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj

    def __str__(self):
        return "Contenu de la page d'accueil"


def default_about_cards():
    return [
        {"icon": "leaf", "title": "Naturel & Vegan", "body": "Tous nos ingrédients sont d'origine naturelle, vegan et certifiés cruelty-free. Nous refusons tout compromis sur la qualité."},
        {"icon": "sparkles", "title": "Science Avancée", "body": "Nos formules intègrent les dernières innovations cosmétiques : acide hyaluronique, céramides, MSM pour des résultats visibles."},
        {"icon": "heart", "title": "Pour Tous", "body": "Qu'il s'agisse de boucles serrées, de tresses ou de cheveux frisés, nos soins s'adaptent à chaque texture."},
    ]


class AboutContent(models.Model):
    eyebrow = models.CharField(max_length=200, default="Notre Histoire")
    title_plain = models.CharField(max_length=200, default="Afro")
    title_emphasis = models.CharField(max_length=200, default="Cure")
    body = models.TextField(
        default="Afro Cure est née d'une conviction simple : les cheveux texturés méritent des soins à la hauteur "
                "de leur beauté. Nous combinons la richesse des plantes africaines avec la rigueur de la science "
                "cosmétique pour créer des formules qui transforment véritablement vos cheveux."
    )
    cards = models.JSONField(default=default_about_cards)  # [{icon, title, body}]
    cta_label = models.CharField(max_length=100, default="Découvrir nos soins")

    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj

    def __str__(self):
        return "Contenu de la page À propos"


def default_products_marquee():
    return ["Hydratation profonde", "Boucles définies", "Sans sulfate", "Vegan", "Naturel", "Afro Cure"]


class ProductsPageContent(models.Model):
    eyebrow = models.CharField(max_length=200, default="Afro Cure — Collection")
    title_plain = models.CharField(max_length=200, default="Nos")
    title_emphasis = models.CharField(max_length=200, default="Soins")
    description = models.TextField(
        default="Chaque formule est pensée pour nourrir, définir et célébrer la beauté naturelle des cheveux texturés."
    )
    marquee_items = models.JSONField(default=default_products_marquee)  # [str]

    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj

    def __str__(self):
        return "Contenu de la page Produits"


def default_footer_marquee():
    return ["Cheveux Texturés", "Beurre de Karité", "Huile de Ricin", "Vegan & Naturel", "Sans Sulfate", "Aloe Vera", "Coiffant Doux"]


def default_footer_soins_items():
    return ["Hydratation", "Définition", "Nourrissants", "Styling"]


class FooterContent(models.Model):
    brand_description = models.TextField(
        default="Des soins efficaces, équilibrés et adaptés aux besoins réels des cheveux texturés. "
                "Science cosmétique et plantes africaines."
    )
    social_eyebrow = models.CharField(max_length=200, default="Suivez-nous")
    facebook_url = models.CharField(max_length=300, blank=True, default="#")
    instagram_url = models.CharField(max_length=300, blank=True, default="#")
    twitter_url = models.CharField(max_length=300, blank=True, default="#")

    marquee_items = models.JSONField(default=default_footer_marquee)  # [str]

    soins_label = models.CharField(max_length=200, default="Nos Soins")
    soins_items = models.JSONField(default=default_footer_soins_items)  # [str], all link to /products

    contact_email = models.CharField(max_length=200, default="contact@afrocure.fr")

    copyright_text = models.CharField(max_length=200, default="© 2026 Afro Cure. Tous droits réservés.")
    tagline = models.CharField(max_length=200, default="Célébrer la beauté naturelle")

    updated_at = models.DateTimeField(auto_now=True)

    def save(self, *args, **kwargs):
        self.pk = 1
        super().save(*args, **kwargs)

    @classmethod
    def load(cls):
        obj, _ = cls.objects.get_or_create(pk=1)
        return obj

    def __str__(self):
        return "Contenu du pied de page"
