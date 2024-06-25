from django.urls import path
from .views import *
urlpatterns = [
    path("tokenize/", TokenizeView.as_view(), name="tokenize"),
    path("pos_tag/", PartialLanguageMarkupView.as_view(), name="partial_language_markup"),
    path("ner/", RecognitionNamedEntitiesView.as_view(), name="recognition_named_entities"),
]