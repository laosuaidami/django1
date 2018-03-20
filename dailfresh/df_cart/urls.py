from django.conf.urls import url

import views
urlpatterns=[
    url(r'^$',views.cart),
    url(r'^add(\d+)_(\d+)',views.add),
    url(r'carts_count',views.carts_count),
]