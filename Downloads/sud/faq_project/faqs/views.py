from django.shortcuts import render
from rest_framework import viewsets
from .models import FAQ
from .serializers import FAQSerializer

def home(request):
    lang = request.GET.get('lang', 'en')
    faqs = FAQ.objects.all()
    
    # Transform FAQ data based on language
    faq_data = []
    for faq in faqs:
        if lang == 'hi':
            question = faq.question_hi or faq.question
            answer = faq.answer_hi or faq.answer
        elif lang == 'bn':
            question = faq.question_bn or faq.question
            answer = faq.answer_bn or faq.answer
        else:
            question = faq.question
            answer = faq.answer
            
        faq_data.append({
            'id': faq.id,
            'question': question,
            'answer': answer
        })
    
    return render(request, 'faqs/home.html', {
        'faqs': faq_data,
        'current_lang': lang
    })

class FAQViewSet(viewsets.ModelViewSet):
    queryset = FAQ.objects.all()
    serializer_class = FAQSerializer