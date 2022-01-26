from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls'))

]

handler404 = 'app.views.error_404'
handler500 = 'app.views.error_500'
handler403 = 'app.views.error_403'
handler400 = 'app.views.error_400'

