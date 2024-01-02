from django.db import models
from django.urls import reverse
from tinymce.models import HTMLField


MEDIA_CHOICES = (
    ("fab fa-facebook-f", "facebook"),
    ("fab fa-twitter", "twitter"),
    ("fab fa-behance", "behance"),
    ("fab fa-pinterest-p", "pinterest"),
    ("fab fa-instagram", "instagram"),
    ("fab fa-dribbble", "dribbble"),
    ("fab fa-linkedin-in", "linkedin"),
    ("fab fa-youtube", "youtube"),
    ("fab fa-vimeo-v", "vimeo"),
    ("fab fa-google-plus-g", "google"),
    ("fab fa-skype", "skype"),
    ("fab fa-tumblr", "tumblr"),
    ("fab fa-github", "github"),
)

class Slider(models.Model):
    topline = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField(upload_to="sliders")
    button_text = models.CharField(max_length=100)
    button_url = models.URLField()

    def __str__(self):
        return self.title


class Service(models.Model):
    CHOICES = (
        ("HOME_AUTOMATION", "Home & Office Automation"),
        ("SECURITY_SURVEILLANCE", "Security & Surveillance")
    )
    category = models.CharField(max_length=50, choices=CHOICES)
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    order = models.PositiveIntegerField(default=0)
    description = models.TextField()
    image = models.ImageField(upload_to='service_image',blank=True,null=True)

    class Meta:
        ordering = ("order",)

    def get_absolute_url(self):
        return reverse("web:service_quote", kwargs={"slug": self.slug})

    def __str__(self):
        return self.name

class PortfolioCategory(models.Model):
    category = models.CharField(max_length=50)
    
    def __str__(self):
        return self.category
    

class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    image = models.ImageField(upload_to="projects")
    description = models.TextField()
    date = models.DateField()
    portfolio_category = models.ForeignKey(PortfolioCategory, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        ordering = (("-date"),)
        verbose_name_plural = "Portfolios"

    def get_absolute_url(self):
        return reverse("web:portfolio_detail", kwargs={"slug": self.slug})

    def get_images(self):
        return PortfolioImage.objects.filter(project=self)

    def __str__(self):
        return self.name


class PortfolioImage(models.Model):
    portfolio = models.ForeignKey(Portfolio, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="project_images")

    def __str__(self):
        return self.project.name


class News(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    date = models.DateField()
    image = models.ImageField(upload_to="news")
    summary = models.TextField()
    content = HTMLField()

    class Meta:
        ordering = (("-date"),)
        verbose_name_plural = "Newses"

    def get_absolute_url(self):
        return reverse("web:news_detail", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title


class Team(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=100)
    image = models.ImageField(upload_to="team")

    def __str__(self):
        return self.name


class Client(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="clients")

    def __str__(self):
        return self.name


class Vacancy(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    location = models.CharField(max_length=100)
    description = models.TextField()
    date = models.DateField()
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ("-date",)
        verbose_name_plural = "Vacancies"

    def get_absolute_url(self):
        return reverse("web:career_apply", kwargs={"slug": self.slug})

    def __str__(self):
        return self.title


class JobApplication(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=100)
    cv = models.FileField(upload_to="job_applications")
    vacancy = models.ForeignKey(Vacancy, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=100, blank=True, null=True)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class SocialMedia(models.Model):
    media = models.CharField(max_length=100, choices=MEDIA_CHOICES)
    url = models.URLField()

    def __str__(self):
        return self.media


class About(models.Model):
    title = models.CharField(max_length=100)
    meta_title = models.CharField(max_length=100)
    short_description = models.TextField()
    description = models.TextField()
    image = models.ImageField(upload_to="about")

    def __str__(self):
        return self.title


class Testimonail(models.Model):
    content = models.CharField(max_length=150)
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name
    
    
class Enquiry(models.Model):
    name = models.CharField(max_length=100)
    contact = models.IntegerField()
    email = models.EmailField()
    details = models.TextField()
    
    def __str__(self):
        return self.name