from django.conf.urls import url
from . import views
app_name = 'accounts'
urlpatterns=[
    url(r'^register/$', views.register, name='register'),
    url(r'^logout/$',views.user_logout,name='logout'),
    url(r'^recommendation/$', views.predict_recomm, name='recommendation'),
    url(r'^profile/(?P<pk>\d+)/$', views.ProfileDetailView.as_view(), name='profile'),
    # url(r'^recommendation/(?P<pk>\d+)/$', views.RecommendationDetailView.as_view(), name='recommendation'),
#url(r'^profile/(?P<pk>\d+)/edit/$', views.profile_update, name='edit_profile'),
]
