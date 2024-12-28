from django.urls import path
from .views import index, about,  contact,  team, testimonial, service, menu, aboutdetail, factsdetail, offerdetail, productsdetail, teamdetail, servicedetail, testimonialdetail, AboutUpdateView, AboutDeleteView, AboutCreateView
urlpatterns = [
    path('', index, name='index'),
    path('about/', about, name='about'),
    path('contact/', contact, name='contact'),
    path('team/', team, name='team'),
    path('testimonial/',  testimonial, name='testimonial'),
    path('service/', service, name='service'),
    path('menu/', menu, name='menu'),
    path('teamdetail/<int:id>/', teamdetail, name='teamdetail'),
    path('testimonialdetail/<int:id>/', testimonialdetail, name='testimonialdetail'),
    path('aboutdetail/<slug:courses>/', aboutdetail, name='aboutdetail'),
    path('factsdetail/<int:id>/', factsdetail, name='factsdetail'),
    path('offerdetail/<int:id>/', offerdetail, name='offerdetail'),
    path('productsdetail/<int:id>/', productsdetail, name='productsdetail'),
    path('servicedetail/<int:id>/', servicedetail, name='servicedetail'),
    path('about/edit/<slug>/', AboutUpdateView.as_view(), name='aboutUpdate'),
    path('about/delete/<slug>/', AboutDeleteView.as_view(), name='aboutDelete'),
    path('about/create', AboutCreateView.as_view(), name='aboutCreate'),
]
