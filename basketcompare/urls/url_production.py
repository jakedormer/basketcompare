from .url_base import *
from basketcompare.settings import production

urlpatterns += static(production.MEDIA_URL, document_root=production.MEDIA_ROOT)