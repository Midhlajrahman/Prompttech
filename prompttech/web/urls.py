from django.urls import path
from django.views.generic import TemplateView
from . import views


app_name = "web"

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about_us, name="about_us"),
    path("services/", views.services, name="services"),
    path("projects/", views.projects, name="projects"),
    path("contact-us/", views.contact_us, name="contact_us"),
    path("privacy-policy/", views.privacy_policy, name="privacy_policy"),
    path("terms-of-use/", views.terms_of_use, name="terms_of_use"),
    path("service/<str:slug>/quote/", views.service_quote, name="service_quote"),
    path("service_details<slug:slug>",views.service_details ,name="service_details"),


    path("blog-details.html", TemplateView.as_view(template_name="web/blog-details.html")),
    path("blog.html", TemplateView.as_view(template_name="web/blog.html")),
    path("coming-soon.html", TemplateView.as_view(template_name="web/coming-soon.html")),
    path("contact.html", TemplateView.as_view(template_name="web/contact.html")),
    path("index.html", TemplateView.as_view(template_name="web/index.html")),
    path("project-1.html", TemplateView.as_view(template_name="web/project-1.html")),
    path("project-2.html", TemplateView.as_view(template_name="web/project-2.html")),
    path("project-3.html", TemplateView.as_view(template_name="web/project-3.html")),
    path("project-details-2.html", TemplateView.as_view(template_name="web/project-details-2.html")),
    path("project-details.html", TemplateView.as_view(template_name="web/project-details.html")),
    path("service-1.html", TemplateView.as_view(template_name="web/service-1.html")),
    path("service-2.html", TemplateView.as_view(template_name="web/service-2.html")),
    path("service-details.html", TemplateView.as_view(template_name="web/service-details.html")),
    path("shop-1.html", TemplateView.as_view(template_name="web/shop-1.html")),
    path("shop-2.html", TemplateView.as_view(template_name="web/shop-2.html")),
    path("shop-3.html", TemplateView.as_view(template_name="web/shop-3.html")),
    path("shop-cart.html", TemplateView.as_view(template_name="web/shop-cart.html")),
    path("shop-checkout.html", TemplateView.as_view(template_name="web/shop-checkout.html")),
    path("shop-product.html", TemplateView.as_view(template_name="web/shop-product.html")),
    path("team-details.html", TemplateView.as_view(template_name="web/team-details.html")),
    path("team.html", TemplateView.as_view(template_name="web/team.html")),

]
