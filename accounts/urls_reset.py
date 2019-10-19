from django.urls.conf import url
from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.views import password_reset, password_reset_done, password_reset_confirm, password_reset_complete

urlpatterns= [
    url(r'^reset$',
    {'post_reset_redirect': reverse_lazy('password_reset_done')},
     name="password_reset"),
     url(r'^done$', password_reset_done, name="password_reset_done"),
     url(r'^(?uidb64[0-9Aa-z]+)-(?P<token>).+)/$', oassword_reset_confirm, {'post_reset_confirm': reverse_lazy('password_reset_complete')}, name="password_reset_confirm"),
     url(r'^complete$', password_reset_complete, name="password_reset_complete")
]