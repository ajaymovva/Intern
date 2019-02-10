from django.urls import path
from analytics.views import *

app_name = "analytics"

urlpatterns = [
    path('', base_page, name="fileadd"),
    path("add/", upload_file, name="fileupload"),
    path('select/', select_fields, name='select_field'),
    path('preprocess/', process_selectfield, name='preprocess'),
]
