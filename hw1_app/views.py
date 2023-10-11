from django.http import HttpResponse
import logging

from django.views.generic import TemplateView

logger = logging.getLogger(__name__)

# 📌 Создайте пару представлений в вашем первом приложении: главная и о себе.
# 📌 Внутри каждого представления должна быть переменная html - многострочный текст с HTML вёрсткой и данными о
# вашем первом Django сайте и о вас.
# 📌 *Сохраняйте в логи данные о посещении страниц.
# 📌 Заменила многострочный текст с HTML вёрсткой на шаблоны...


class MainView(TemplateView):
    template_name = 'hw1_app/main.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Главная'
        logger.info(f'{context} => Main page accessed!')
        return context


class AboutView(TemplateView):
    template_name = 'hw1_app/about.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Обо мне'
        logger.info(f'{context} => About page accessed!')
        return context
