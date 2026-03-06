from api.spectacular.urls import urlpatterns as doc_urls
from accounts.urls import urlpatterns as accounts
from statistic.urls import urlpatterns as statistica

app_name = 'api'

urlpatterns = []

urlpatterns += doc_urls
urlpatterns += accounts
urlpatterns += statistica