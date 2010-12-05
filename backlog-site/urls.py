from django.conf.urls.defaults import *
from django.conf import settings
import views


from django.views.generic.simple import direct_to_template

from django.contrib import admin
admin.autodiscover()

from account.openid_consumer import PinaxConsumer


if settings.ACCOUNT_OPEN_SIGNUP:
    signup_view = "account.views.signup"
else:
    signup_view = "signup_codes.views.signup"


urlpatterns = patterns('',
    url(r'^$', "projects.views.home" , name="home"),
    
    url(r'^robots.txt$', direct_to_template, {'template': 'robots.txt'}),    
    
    url(r'^stats$', direct_to_template, {'template': 'site_stats.html'}),    
    url(r'^stats_data$', views.stats_data ),
    
    url(r'^admin/invite_user/$', 'signup_codes.views.admin_invite_user', name="admin_invite_user"),
    url(r'^account/signup/$', signup_view, name="acct_signup"),
    (r'^forum/', include('forum.urls')),
    (r'^about/', include('about.urls')),
    (r'^account/', include('account.urls')),
    (r'^openid/(.*)', PinaxConsumer()),
    (r'^profiles/', include('basic_profiles.urls')),
    (r'^avatar/', include('avatar.urls')),
    (r'^comments/', include('threadedcomments.urls')),
    (r'^announcements/', include('announcements.urls')),
    (r'^tagging_utils/', include('tagging_utils.urls')),
    (r'^attachments/', include('attachments.urls')),
    (r'^projects/', include('projects.urls')),    
    (r'^organization/', include('organizations.urls')),    
    (r'^admin/(.*)', admin.site.root),
)

if settings.SERVE_MEDIA:
    urlpatterns += patterns('',
        (r'^site_media/', include('staticfiles.urls')),
    )