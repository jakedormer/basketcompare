from .url_base import *
from basketcompare.settings import development

urlpatterns += static(development.MEDIA_URL, document_root=development.MEDIA_ROOT)

