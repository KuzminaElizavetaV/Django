from django.http import HttpResponse
import logging
logger = logging.getLogger(__name__)

# 📌 Создайте пару представлений в вашем первом приложении: главная и о себе.
# 📌 Внутри каждого представления должна быть переменная html - многострочный текст с HTML вёрсткой и данными о
# вашем первом Django сайте и о вас.
# 📌 *Сохраняйте в логи данные о посещении страниц


def index(request):
    html = '''
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport"
              content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, minimum-scale=1.0">
        <meta http-equiv="X-UA-Compatible" content="ie=edge">
        <title>Главная</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css"
              rel="stylesheet"
              integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC"
              crossorigin="anonymous"
        />
        <script
          src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.min.js"
          integrity="sha384-Rx+T1VzGupg4BHQYs2gCW9It+akI2MM/mndMCy36UVfodzcJcF0GGLxZIzObiEfa"
          crossorigin="anonymous"
        ></script>
    </head>
    <body>
        <div class="container-fluid">
            <ul class="nav nav-pills justify-content-end align-items-end">
                <li class="nav-item"><a href="/" class="nav-link">Главная</a></li>
                <li class="nav-item"><a href="/about/" class="nav-link">Обо мне</a></li>
            </ul>
            <div class="container text-center my-5">
              <div class="row">
                <div class="col-lg-6 col-md-8 mx-auto">
                  <h1 class="fw-light">Это мой первый Django сайт!</h1>
                  <p class="lead text-muted">Мой первый проект с использованием фреймворка Django</p>
                  <p class="lead text-muted">Мое первое домашнее задание</p>
                  <a href="https://github.com/KuzminaElizavetaV/Django" target="_blank" class="btn btn-primary">
                    GitHub
                  </a>
                  <a href="/about/" class="btn btn-primary">Обо мне</a>
                </div>
              </div>
            </div>
    <div class="row fixed-bottom modal-footer">
        <hr>
        <p>Все права защищены &copy;</p>
    </div>
    </div>
    </body>
    </html>'''
    logger.info('Index page accessed')
    return HttpResponse(html)


def about(request):
    html = '''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport"
                  content="width=device-width, user-scalable=no, initial-scale=1.0, maximum-scale=1.0, 
                  minimum-scale=1.0">
            <meta http-equiv="X-UA-Compatible" content="ie=edge">
            <title>Обо мне</title>
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.2/dist/css/bootstrap.min.css"
                  rel="stylesheet"
                  integrity="sha384-EVSTQN3/azprG1Anm3QDgpJLIm9Nao0Yz1ztcQTwFspd3yD65VohhpuuCOmLASjC"
                  crossorigin="anonymous"
            />
            <script
              src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.min.js"
              integrity="sha384-Rx+T1VzGupg4BHQYs2gCW9It+akI2MM/mndMCy36UVfodzcJcF0GGLxZIzObiEfa"
              crossorigin="anonymous"
            ></script>
        <style>
          .rounded-img {
            width: 60%;
            border-radius: 50%;
            box-shadow: 0 0 10px rgba(26, 9, 9, 0.4);
            padding: 0.6em;
            margin-bottom: 1em;
          }
        </style>
        </head>
        <body>
            <div class="container-fluid">
                <ul class="nav nav-pills justify-content-end align-items-end">
                    <li class="nav-item"><a href="/" class="nav-link">Главная</a></li>
                    <li class="nav-item"><a href="/about/" class="nav-link">Обо мне</a></li>
                </ul>
                <div class="container text-center my-5">
                  <div class="row">
                    <div class="col-lg-6 col-md-8 mx-auto">
                      <img class="rounded-img" src="../img/me.jpg" alt="Тут должно быть мое фото"/>
                      <h1 class="fw-light">Меня зовут Елизавета</h1>
                      <p class="lead text-muted">Я - начинающий разработчик на языке Python</p>
                      <a href="/" class="btn btn-primary">Назад</a>
                    </div>
                  </div>
                </div>
        <div class="row fixed-bottom modal-footer">
            <hr>
            <p>Все права защищены &copy;</p>
        </div>
        </div>
        </body>
        </html>'''
    logger.info('About page accessed')
    return HttpResponse(html)
