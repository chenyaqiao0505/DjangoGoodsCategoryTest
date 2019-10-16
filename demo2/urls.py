from django.contrib import admin
from django.urls import path
from app01.views import Type1View,Type2View,Type3View,Type4View,TypeView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/Type1',Type1View.as_view()),
    path('api/Type2',Type2View.as_view()),
    path('api/Type3',Type3View.as_view()),
    path('api/Type4',Type4View.as_view()),
    path(r'api/Type',TypeView.as_view()),

]
