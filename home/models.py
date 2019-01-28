from django.db import models
from django.db.models import Q
from django.utils import timezone
from modelcluster.fields import ParentalKey
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.core.blocks import CharBlock

from wagtail.core.models import Page, Orderable
from wagtail.core.fields import RichTextField, StreamField
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, StreamFieldPanel, MultiFieldPanel
from wagtail.images.edit_handlers import ImageChooserPanel


class HomePage(Page):
    about_content = RichTextField(blank=True)
    layout_lab_link = models.URLField()

    # Contact Info
    address = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=100, null=True)

    hours = StreamField([
        ('hour_info', CharBlock())
    ], null=True)

    content_panels = Page.content_panels + [
        InlinePanel('announcements', label='Announcements'),
        FieldPanel('about_content', classname="full"),
        InlinePanel('gallery_images', label="Gallery images"),
        FieldPanel('layout_lab_link'),
        InlinePanel('pricing_sections', label='Pricing Sections'),
        MultiFieldPanel([
            FieldPanel('address'),
            FieldPanel('email'),
            FieldPanel('phone'),
            StreamFieldPanel('hours')
        ], heading='Contact Information')
    ]

    parent_page_types = []

    def get_context(self, request, *args, **kwargs):
        context = super(HomePage, self).get_context(request)
        context['current_announcements'] = Announcement.objects\
            .filter(start_date__lte=timezone.now().date())\
            .filter(Q(end_date__gte=timezone.now().date()) | Q(end_date=None))
        return context


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
    start_date = models.DateField(default=timezone.now(), null=False)
    end_date = models.DateField(null=True, blank=True)

    panels = [
        FieldPanel('announcement'),
        FieldPanel('start_date'),
        FieldPanel('end_date')
    ]


class PricingSection(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='pricing_sections')
    pricing_title = models.CharField(max_length=200)
    caption = models.CharField(max_length=200)
    body = StreamField([
        ('table', TableBlock(), ),
    ], blank=True)

    panels = [
        FieldPanel('pricing_title'),
        FieldPanel('caption'),
        StreamFieldPanel('body'),
    ]
