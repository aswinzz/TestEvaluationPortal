
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url,include

app_name="evaluation"

urlpatterns =[
    url(r'^marks',views.uploadMarksView,name='course'),
    url(r'^course',views.uploadCourseView,name='marks'),
    url(r'^attendance',views.uploadAttendanceView,name='attendance'),

]
