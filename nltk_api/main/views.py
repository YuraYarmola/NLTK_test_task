from nltk import pos_tag, ne_chunk
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from nltk.tokenize import word_tokenize, sent_tokenize
import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')


class TokenizeView(APIView):
    def post(self, request, *args, **kwargs):
        text = request.data['text']
        mode = request.data.get("mode", "word")
        if mode == "word":
            return Response(word_tokenize(text), status=status.HTTP_200_OK)
        elif mode == "sentence":
            return Response(sent_tokenize(text), status=status.HTTP_200_OK)
        else:
            return Response({"error": "Invalid mode"}, status=status.HTTP_400_BAD_REQUEST)


class PartialLanguageMarkupView(APIView):
    def post(self, request, *args, **kwargs):
        text = request.data['text']
        language = request.data.get('language', "eng")
        words = word_tokenize(text)
        pos_tags = nltk.pos_tag(words, lang=language)
        return Response(pos_tags, status=status.HTTP_200_OK)


class RecognitionNamedEntitiesView(APIView):
    def post(self, request, *args, **kwargs):
        text = request.data['text']
        words = word_tokenize(text)
        tags = pos_tag(words)
        named_entities = ne_chunk(tags)
        entities = []
        for entity in named_entities:
            if hasattr(entity, 'label'):
                entities.append((entity.label(), ' '.join(c[0] for c in entity)))

        return Response(entities, status=status.HTTP_200_OK)

