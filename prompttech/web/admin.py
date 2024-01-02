from django.contrib import admin
from import_export.admin import ImportExportActionModelAdmin

from .models import About
from .models import Contact ,Enquiry
from .models import JobApplication
from .models import News
from .models import Portfolio
from .models import Service
from .models import SocialMedia
from .models import Team, Slider
from .models import Vacancy, PortfolioImage
from .models import PortfolioCategory ,Testimonail



class PortfolioImageInline(admin.TabularInline):
    model = PortfolioImage
    extra = 1


@admin.register(Service)
class ServiceAdmin(ImportExportActionModelAdmin):
    list_display = ("name", "description")
    prepopulated_fields = {"slug": ("name",)}


@admin.register(Portfolio)
class PortfolioAdmin(ImportExportActionModelAdmin):
    list_display = ("name", "image")
    prepopulated_fields = {"slug": ("name",)}
    inlines = [PortfolioImageInline]


@admin.register(News)
class NewsAdmin(ImportExportActionModelAdmin):
    list_display = ("title", "date")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(Team)
class TeamAdmin(ImportExportActionModelAdmin):
    list_display = ("name", "position")


@admin.register(Vacancy)
class VacancyAdmin(ImportExportActionModelAdmin):
    list_display = ("title", "location")
    prepopulated_fields = {"slug": ("title",)}


@admin.register(JobApplication)
class JobApplicationAdmin(ImportExportActionModelAdmin):
    list_display = ("name", "vacancy")


@admin.register(Contact)
class ContactAdmin(ImportExportActionModelAdmin):
    list_display = ("name", "email", "subject")


@admin.register(SocialMedia)
class SocialMediaAdmin(ImportExportActionModelAdmin):
    list_display = ("media", "url")


@admin.register(About)
class AboutAdmin(ImportExportActionModelAdmin):
    list_display = ("title", "description")

    # hide new button if one already exists
    def has_add_permission(self, request):
        num_objects = self.model.objects.count()
        if num_objects >= 1:
            return False
        else:
            return True


@admin.register(Slider)
class SliderAdmin(ImportExportActionModelAdmin):
    list_display = ("title", "description", "image")
 
 
@admin.register(PortfolioCategory)
class Portfolio_CategoryAdmin(ImportExportActionModelAdmin):
    list_display = ("category",)
    

@admin.register(Testimonail)
class TestimonailAdmin(ImportExportActionModelAdmin):
    list_display = ("name",)

       
@admin.register(Enquiry)
class EnquiryAdmin(ImportExportActionModelAdmin):
    list_display = ("name", "contact", "email",)