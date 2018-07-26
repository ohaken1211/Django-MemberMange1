"""scelts_manager URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from manager import views

import manager.views as manager_view

app_name = 'Scelts Member'
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login/', manager_view.CustomLoginView.as_view()),
    #url(r'^logout/', manager_view.logout_view),
    url(r'^member_list/', manager_view.PersonListView.as_view()),
    #url(r'^hijack/', include('hijack.urls')),
    # URLとViewを組み合わせる！
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [
        url(r'^__debug__/', include(debug_toolbar.urls)),
    ]
