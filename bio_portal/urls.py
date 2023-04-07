from django.urls import path
from globus_portal_framework.urls import register_custom_index
from bio_portal.views import BIOSearchView, example_view

app_name = "sdl-bio-index"

register_custom_index("sdl_bio_index", ["sdl-bio"])

urlpatterns = [
#    path("<sdl_bio_index:index>/", BIOSearchView.as_view(), name="search"),
]
