import os
from smtplib import SMTPException

from django.core.mail import EmailMultiAlternatives
from django.db import models
from django.db.models import Q
from django.template.loader import render_to_string
from django.utils import timezone
from django.utils.html import strip_tags
from modelcluster.fields import ParentalKey
from wagtail.admin.edit_handlers import FieldPanel, InlinePanel, StreamFieldPanel, MultiFieldPanel
from wagtail.contrib.table_block.blocks import TableBlock
from wagtail.core.blocks import CharBlock
from wagtail.core.fields import RichTextField, StreamField
from wagtail.core.models import Page, Orderable
from wagtail.images.edit_handlers import ImageChooserPanel
from django.contrib import messages

from home.forms import ContactForm


class ContactPage(Page):
    contact_content = RichTextField(blank=True)

    content_panels = Page.content_panels + [
        FieldPanel('contact_content', classname='full')
    ]

    def get_context(self, request, *args, **kwargs):
        context = super(ContactPage, self).get_context(request)
        if request.method == 'GET':
            context['form'] = ContactForm()
        else:
            context['form'] = ContactForm()
            form = ContactForm(request.POST, request.FILES)
            try:
                if not form.is_valid():
                    raise KeyError('invalid form submitted')
                subject = form.cleaned_data['subject']
                from_email = form.cleaned_data['from_email']
                message = form.cleaned_data['message']
                phone = form.cleaned_data['phone']
                data = {
                    'from_email': from_email,
                    'phone': phone,
                    'message': message
                }

                msg_html = render_to_string('home/email.html', data)
                msg_plain = strip_tags(msg_html)

                email = EmailMultiAlternatives(
                    'CUSTOMER INQUIRY: ' + subject,
                    msg_plain,
                    'alexn1336@gmail.com',
                    [os.getenv('FORM_EMAIL')],
                    reply_to=[from_email],
                )
                email.attach_alternative(msg_html, 'text/html')
                for file in request.FILES.getlist('file_field'):
                    email.attach(file.name, file.read(), file.content_type)
                email.send(fail_silently=False)
                messages.add_message(
                    request, messages.SUCCESS,
                    'Successfully sent Longbeach Graphix a message. We will contact you shortly.')
            except KeyError:
                messages.add_message(
                    request, messages.ERROR,
                    'It seems you didn\'t provide all of the necessary form data. Please fill out the required fields.')
            except (SMTPException, Exception) as _:
                messages.add_message(
                    request, messages.ERROR,
                    'An error happened while sending your email. Please try again or contact us via email.')

        return context


class HomePage(Page):
    about_content = RichTextField(blank=True)
    # layout_lab_link = models.URLField()
    payments_link = models.URLField()

    # Contact Info
    contact = RichTextField(blank=True)
    address = models.CharField(max_length=200, null=True)
    email = models.EmailField(null=True)
    phone = models.CharField(max_length=100, null=True)

    hours = StreamField([
        ('hour_info', CharBlock())
    ], null=True)

    content_panels = Page.content_panels + [
        MultiFieldPanel([
            InlinePanel('announcements', label='Announcements'),
        ], classname="collapsible collapsed", heading='Announcements'),
        MultiFieldPanel([
            FieldPanel('about_content', classname="full"),
        ], classname="collapsible collapsed", heading='About'),
        MultiFieldPanel([
            InlinePanel('gallery_images', label="Gallery images"),
        ], classname="collapsible collapsed", heading='Gallery Images'),
        # FieldPanel('layout_lab_link'),
        MultiFieldPanel([
            InlinePanel('pricing_sections', label='Pricing Sections'),
        ], heading="Pricing Sections"),
        MultiFieldPanel([
            # FieldPanel('address'),
            # FieldPanel('email'),
            # FieldPanel('phone'),
            # StreamFieldPanel('hours')
            FieldPanel('contact')
        ], heading='Contact Information', classname="collapsible collapsed"),
        MultiFieldPanel([
            FieldPanel('payments_link')
        ], heading='Payments Info', classname="collapsible collapsed")
    ]

    parent_page_types = []

    def get_context(self, request, *args, **kwargs):
        context = super(HomePage, self).get_context(request)
        context['current_announcements'] = Announcement.objects \
            .filter(start_date__lte=timezone.now().date()) \
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
    start_date = models.DateField(default=timezone.now, null=False)
    end_date = models.DateField(null=True, blank=True)

    panels = [
        FieldPanel('announcement'),
        FieldPanel('start_date'),
        FieldPanel('end_date')
    ]


class PricingSection(Orderable):
    page = ParentalKey(HomePage, on_delete=models.CASCADE, related_name='pricing_sections')
    pricing_title = models.CharField(max_length=200)
    caption = models.CharField(max_length=200, null=True, blank=True)
    image = models.ForeignKey(
        'wagtailimages.Image', on_delete=models.CASCADE, related_name='+', null=True, blank=True
    )
    body = StreamField([
        ('table', TableBlock(), ),
    ], blank=True)

    panels = [
        FieldPanel('pricing_title'),
        FieldPanel('caption'),
        StreamFieldPanel('body'),
        ImageChooserPanel('image')
    ]
