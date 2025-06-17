"""
Настройки Django для проекта BulletinBoard.

Создано «django-admin startproject» с использованием Django 5.0.6.

Дополнительную информацию об этом файле см.
https://docs.djangoproject.com/en/5.0/topics/settings/

Полный список настроек и их значений см.
https://docs.djangoproject.com/en/5.0/ref/settings/
"""

from pathlib import Path
import os

# Создайте пути внутри проекта следующим образом: BASE_DIR/'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Настройки быстрого запуска разработки - непригодны для производства
# См. https://docs.djangoproject.com/en/5.0/howto/deployment/checklist/.


SECRET_KEY = 'django-insecure-mkg#tly^fzk!$#ci0^q9=n^)jgkhv3l&+qxa%i!@jv#(q#67d%' # noqa


DEBUG = True
ALLOWED_HOSTS = []
# DEBUG = False
# ALLOWED_HOSTS = ['127.0.0.1']

SITE_ID = 1

# Определение приложения

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'allauth',
    'allauth.account',
    'allauth.socialaccount',

    'django_extensions',
    'ckeditor',

    'appAccounts.apps.AppaccountsConfig',
    'appBoard.apps.AppboardConfig',
    'appSubscriptions.apps.AppsubscriptionsConfig',

]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'allauth.account.middleware.AccountMiddleware',
]

ROOT_URLCONF = 'BulletinBoard.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',

                'django.template.context_processors.request',
            ],
        },
    },
]

WSGI_APPLICATION = 'BulletinBoard.wsgi.application'


# База данных
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Проверка пароля
# https://docs.djangoproject.com/en/5.0/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator', # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator', # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator', # noqa
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Интернационализация
# https://docs.djangoproject.com/en/5.0/topics/i18n/

LANGUAGE_CODE = 'ru'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Статические файлы (CSS, JavaScript, изображения)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = 'static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Тип поля первичного ключа по умолчанию
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'appAccounts.User'
#  После входа, пользователя перенаправляем на страницу с новостями.
LOGIN_REDIRECT_URL = "/board."

# Этого раздела может не быть, добавьте его в указанном виде.
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

'''
Первые два параметра указывают на то, что поле email является обязательным
и уникальным.
Третий, наоборот, — говорит, что username необязательный.
Следующий параметр указывает, что аутентификация будет происходить
посредством электронной почты.
Напоследок мы указываем, что верификация почты отсутствует.

Обычно на почту отправляется подтверждение аккаунта,
после подтверждения которого восстанавливается полная функциональность
учётной записи.
'''

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True
# 'None' - проверка email — отсутствует;
# 'mandatory' — не пускать пользователя на сайт до момента подтверждения почты;
# 'optional' — сообщение о подтверждении почты будет отправлено, но
# пользователь может залогиниться на сайте без подтверждения почты.
# Чтобы allauth распознал нашу форму как ту, что должна выполняться вместо
# формы по умолчанию, необходимо добавить.
ACCOUNT_FORMS = {
    'signup': 'appAccounts.forms.CustomSignupForm',
}

# Блок кода настроек нашего проекта работы с почтой (Yandex-почтой)
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
# 'django.core.mail.backends.console.EmailBackend' - для писем в терминал
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# класс отправителя сообщений (у нас установлено значение по умолчанию,
# а значит, эта строчка не обязательна)
EMAIL_HOST = 'smtp.yandex.ru'
# Хост почтового сервера — это адрес или доменное имя сервера, который
# обрабатывает и отправляет электронную почту.
# Хост почтового сервера может быть использован как для отправки, так и для
# получения почты.
EMAIL_PORT = 465
"""
Порт, на который почтовый сервер принимает письма, называется почтовым портом.
Один из самых распространенных почтовых портов - это порт 25, который
используется для передачи электронной почты
по протоколу SMTP (Simple Mail Transfer Protocol).
Однако, существуют и другие почтовые порты, такие как порт 587,
который используется для SMTP с шифрованием TLS (Transport Layer Security),
и порт 465,
который используется для SMTP с шифрованием SSL (Secure Sockets Layer).
Использование конкретного почтового порта зависит от настроек и требований
почтового сервера.
"""
EMAIL_HOST_USER = "AndreyTestSF"
# логин пользователя почтового сервера
EMAIL_HOST_PASSWORD = "zuqvkobqbkixymje"  # noqa
# пароль пользователя почтового сервера
EMAIL_USE_TLS = False
# необходимость использования TLS
# (зависит от почтового сервера,
# смотрите документацию по настройке работы с сервером по SMTP)
EMAIL_USE_SSL = True
# необходимость использования SSL
# (зависит от почтового сервера,
# смотрите документацию по настройке работы с сервером по SMTP)

DEFAULT_FROM_EMAIL = "AndreyTestSF@yandex.ru"
# Почтовый адрес отправителя по умолчанию
# Последняя строчка будет использоваться как значение по умолчанию
# для поля from в письме.
# То есть будет отображаться в поле «отправитель» у получателя письма.

SERVER_EMAIL = "AndreyTestSF@yandex.ru"
# SERVER_EMAIL содержит адрес почты, от имени которой будет отправляться письмо
# при вызове mail_admins и mail_manager.
# А переменная MANAGERS будет хранить список имён менеджеров и адресов
# их почтовых ящиков.


EMAIL_SUBJECT_PREFIX = 'Bulletin Board'

# Настройки Celery
CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = 'redis://localhost:6379/0'
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TIMEZONE = TIME_ZONE

# Добавляем django-celery-beat в установленные приложения
INSTALLED_APPS += ['django_celery_beat']

# URL сайта для использования в рассылках
SITE_URL = 'http://localhost:8000'  # Измените на реальный URL в продакшене

# Настройки для отправки email
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # Для разработки
# EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  # Для продакшена

# Настройки для allauth
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
ACCOUNT_LOGOUT_ON_GET = True

# Настройки для allauth форм
ACCOUNT_FORMS = {
    'signup': 'appAccounts.forms.CustomSignupForm',
}

# Медиа файлы
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Maximum upload file size (10MB)
DATA_UPLOAD_MAX_MEMORY_SIZE = 10485760
FILE_UPLOAD_MAX_MEMORY_SIZE = 10485760

# Allowed file types
ALLOWED_IMAGE_TYPES = ['image/jpeg', 'image/png', 'image/gif']
ALLOWED_VIDEO_TYPES = ['video/mp4', 'video/webm']