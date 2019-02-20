from django.db import models
from modelcluster.fields import ParentalKey

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel
from wagtail.images.edit_handlers import ImageChooserPanel

import datetime


class HomePage(Page):
    about_content = RichTextField(blank=True)
    layout_lab_link = models.URLField()

    content_panels = Page.content_panels + [
        InlinePanel('announcements', label='Announcements'),
        FieldPanel('about_content', classname="full"),
        InlinePanel('gallery_images', label="Gallery images"),
        FieldPanel('layout_lab_link')
    ]

class GalleryImage(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='gallery_images')
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+'
    )
    caption = models.CharField(blank=True, max_length=250)

    panels = [
        ImageChooserPanel('image'),
        FieldPanel('caption'),
    ]

class Announcement(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='announcements')
    announcement = models.CharField(blank=True, max_length=200)
    start_date = models.DateField(default=datetime.date.today(), null=False)
    end_date = models.DateField(null=True)

    panels = [
        FieldPanel('announcement'),
        FieldPanel('start_date'),
        FieldPanel('end_date')
    ]