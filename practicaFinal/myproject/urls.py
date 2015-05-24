from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'myproject.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', "cms_content_app.views.PaginaPrincipal"),
    url(r'^css/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_URL2}),
    url(r'^todas/css/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_URL2}),
    url(r'^login/css/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_URL2}),
    url(r'^logout/css/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_URL2}),
    url(r'^usuario/css/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_URL2}),
    url(r'^noRegistrado/css/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_URL2}),
    url(r'^noRegistrado/$', "cms_content_app.views.NoRegistrado"),
    url(r'^login/$', "cms_content_app.views.login_view"),
    url(r'^logout/$', "cms_content_app.views.logout_view"),
    url(r'^todas/$', "cms_content_app.views.Todas"),
    url(r'^actualizar/$', "cms_content_app.views.Actualizar"),
    url(r'^usuario/$', "cms_content_app.views.user"),
    url(r'^usuario/rss$', "cms_content_app.views.rss"),
    url(r'^guardar/(.*)$', "cms_content_app.views.GuardarActividad"),
    url(r'^(.*)/rss$', "cms_content_app.views.rssUsuario"),
    url(r'^(.*)$', "cms_content_app.views.paginaUsuario"),
    
)
