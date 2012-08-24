from django.conf.urls import patterns, url
from . import views

urlpatterns = patterns('sa_api',
    url(r'^$',
        views.index_view,
        name='manager_index'),
    url(r'^datasets/$',
        views.datasets_view,
        name='manager_dataset_list'),
    url(r'^datasets/new/$',
        views.NewDataSetView.as_view(),
        name='manager_dataset_create'),
    url(r'^datasets/(?P<pk>[^/]+)/$',
        views.ExistingDataSetView.as_view(),
        name='manager_dataset_detail'),
    url(r'^datasets/(?P<dataset_slug>[^/]+)/places/$',
        views.places_view,
        name='manager_place_list'),
    url(r'^datasets/(?P<dataset_slug>[^/]+)/places/new/$',
        views.NewPlaceView.as_view(),
        name='manager_place_create'),
    url(r'^datasets/(?P<dataset_slug>[^/]+)/places/(?P<pk>\d+)/$',
        views.ExistingPlaceView.as_view(),
        name='manager_place_detail'),
    url(r'^datasets/(?P<dataset_slug>[^/]+)/places/(?P<place_id>\d+)/(?P<submission_type>[^/]+)/$',
        views.SubmissionListView.as_view(),
        name='manager_place_submission_list'),
    url(r'^datasets/(?P<dataset_slug>[^/]+)/places/(?P<place_id>\d+)/(?P<submission_type>[^/]+)/new/$',
        views.NewSubmissionView.as_view(),
        name='manager_place_submission_create'),
    url(r'^datasets/(?P<dataset_slug>[^/]+)/places/(?P<place_id>\d+)/(?P<submission_type>[^/]+)/(?P<pk>\d+)/$',
        views.ExistingSubmissionView.as_view(),
        name='manager_place_submission_detail'),
)
