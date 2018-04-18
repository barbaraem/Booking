"""Booking URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from booking_app.views import BookingView, PriceListView, AddClientView, AddTreatmentView, ClientLoginView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^home$', PriceListView.as_view(), name="home"),
    url(r'^booking/(?P<treatment_id>(\d)+)', BookingView.as_view(), name="booking"),
    url(r'^add_client$', AddClientView.as_view(), name="add_client"),
    url(r'^user_login$', ClientLoginView.as_view(), name="user_login"),
    url(r'^add_treatment$', AddTreatmentView.as_view(), name="add_treatment"),
]
