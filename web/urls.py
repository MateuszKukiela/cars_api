from django.conf.urls import include, url
from django.contrib import admin
from django.urls import path
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view

API_TITLE = "Cars API"
API_DESCRIPTION = "A Web API for adding and rating cars."
schema_view = get_schema_view(title=API_TITLE)

urlpatterns = [
    url(r"^", include("api.urls")),
    url(r"^api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    url(r"^schema/$", schema_view),
    url(r"^docs/", include_docs_urls(title=API_TITLE, description=API_DESCRIPTION)),
    path("admin/", admin.site.urls),
]
