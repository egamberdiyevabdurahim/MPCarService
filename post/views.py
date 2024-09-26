from django.shortcuts import render

from about.models import (CarouselModel, ServicesAboutModel, AboutModel, TickedModel,
                          ServicesModel, SocialsModel, InfoModel, ExpertTechniciansModel)


def home_page_view(request):
    carousel = CarouselModel.objects.filter(is_active=True)
    about = AboutModel.objects.filter(is_deleted=False).first()
    service = ServicesModel.objects.filter(is_deleted=False)
    info = InfoModel.objects.filter(is_deleted=False).first()
    expert_technicians = ExpertTechniciansModel.objects.filter(is_pinned=True)


    counter = 0
    for ser in about.services.all():
        counter += 1
        setattr(ser, 'number', int(f"0{counter}"))
        # service['number'] = f"0{counter}"

    context = {
        'carousel': carousel,
        'about': about,
        'service': service,
        'info': info,
        'experts': expert_technicians,
    }

    return render(request, 'index.html', context)


def about_page_view(request):
    return render(request, 'about.html')


def contact_page_view(request):
    return render(request, 'contact.html')


def booking_page_view(request):
    return render(request, 'booking.html')


def service_page_view(request):
    return render(request, 'service.html')


def team_page_view(request):
    return render(request, 'team.html')


def testimonial_page_view(request):
    return render(request, 'testimonial.html')