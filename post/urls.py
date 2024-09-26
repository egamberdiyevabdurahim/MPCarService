from django.urls import path

from post.views import (home_page_view, about_page_view, contact_page_view, booking_page_view,
                        service_page_view, team_page_view, testimonial_page_view)


urlpatterns = [
    path('', home_page_view, name="home"),
    path('about/', about_page_view, name="about"),
    path('contact/', contact_page_view, name="contact"),
    path('booking/', booking_page_view, name="booking"),
    path('service/', service_page_view, name="service"),
    path('team/', team_page_view, name="team"),
    path('testimonial/', testimonial_page_view, name="testimonial"),
]