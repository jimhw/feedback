"""
Copyright (C) 2015 James Wong <jameshsw@gmail.com>
All Rights Reserved.

URL file
"""

from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
	# Examples:
	# url(r'^$', 'mysite.views.home', name='home'),
	# url(r'^blog/', include('blog.urls')),

	url(r'^admin/', include(admin.site.urls)),
	# url(r'^polls/', include('polls.urls')),
	url(r'^polls/', include('polls.urls', namespace="polls")),
)
