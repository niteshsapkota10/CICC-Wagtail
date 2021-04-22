from django.db import models

from wagtail.core.models import Page
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    def get_context(self, request):
        context = super(HomePage, self).get_context(request)
        context['images'] = CarouselPage.objects.all()[1:]
        context['first_image'] = CarouselPage.objects.all()[:1].get()
        context['services_three'] = Services.objects.all()[:3].filter()
        context['about'] = AboutPage.objects.all()[:1].get()
        context['projects'] = ProjectPage.objects.all()[:1].get()
        return context
        

class CarouselPage(Page):
    banner_title = models.CharField(max_length=100, blank=False, null=True)
    banner_subtitle = RichTextField(features=["bold", "italic"], blank=False, null=True)
    banner_image = models.ForeignKey("wagtailimages.Image", null=True, blank=False, on_delete=models.SET_NULL, related_name="+")


    content_panels = Page.content_panels + [
        FieldPanel("banner_title"),
        FieldPanel("banner_subtitle"),
        ImageChooserPanel("banner_image"),
    ]


class Services(Page):
    service_title = models.CharField(max_length=100, blank=False, null=False)
    service_subtitle = models.TextField(blank=False, null=False)
    service_body = models.TextField(blank=False, null=False)
    service_image = models.ForeignKey("wagtailimages.Image", null=True, blank=False, on_delete=models.SET_NULL, related_name="+")

    content_panels = Page.content_panels + [
        FieldPanel("service_title"),
        FieldPanel("service_subtitle"),
        FieldPanel("service_body"),
        ImageChooserPanel("service_image"),
    ]
    

class AboutPage(Page):
    about_heading = models.CharField(max_length=100, blank=False, null=False)
    about_subheading = models.CharField(max_length=100,blank=True, null=True)
    about_description = models.TextField(blank=False, null=False)
    about_image = models.ForeignKey("wagtailimages.Image", null=True, blank=False, on_delete=models.SET_NULL, related_name="+")

    content_panels = Page.content_panels + [
        FieldPanel("about_heading"),
        FieldPanel("about_subheading"),
        FieldPanel("about_description"),
        ImageChooserPanel("about_image"),
    ]


class ServicePage(Page):
    def get_context(self, request):
        context = super(ServicePage, self).get_context(request)
        context['services'] = Services.objects.all()
        return context



class Projects(Page):
    project_title = models.CharField(max_length=100, blank=False, null=False)
    project_subtitle = models.TextField(blank=False, null=False)
    project_body = models.TextField(blank=False, null=False)
    project_image = models.ForeignKey("wagtailimages.Image", null=True, blank=False, on_delete=models.SET_NULL, related_name="+")

    content_panels = Page.content_panels + [
        FieldPanel("project_title"),
        FieldPanel("project_subtitle"),
        FieldPanel("project_body"),
        ImageChooserPanel("project_image"),
    ]



class ProjectPage(Page):
    project_heading = models.CharField(max_length=100, blank=False, null=False)
    project_subheading = models.CharField(max_length=100,blank=True, null=True)
    project_description = models.TextField(blank=False, null=False)
    project_image = models.ForeignKey("wagtailimages.Image", null=True, blank=False, on_delete=models.SET_NULL, related_name="+")
    def get_context(self, request):
        context = super(ProjectPage, self).get_context(request)
        context['projects'] = Projects.objects.all()
        return context
    
    content_panels = Page.content_panels + [
        FieldPanel("project_heading"),
        FieldPanel("project_subheading"),
        FieldPanel("project_description"),
        ImageChooserPanel("project_image"),
    ]
