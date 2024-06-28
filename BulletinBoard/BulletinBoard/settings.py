"""
Настройки Django для проекта BulletinBoard.

Создано «django-admin startproject» с использованием Django 5.0.6.

Дополнительную информацию об этом файле см.
https://docs.djangoproject.com/en/5.0/topics/settings/

Полный список настроек и их значений см.
https://docs.djangoproject.com/en/5.0/ref/settings/
"""
import os
from pathlib import Path

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
        'DIRS': [os.path.join(BASE_DIR, 'appAccounts/templates/appAccounts')],
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

# Тип поля первичного ключа по умолчанию
# https://docs.djangoproject.com/en/5.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'appAccounts.User'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
]

ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_UNIQUE_EMAIL = True
ACCOUNT_USERNAME_REQUIRED = False
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_EMAIL_VERIFICATION = 'mandatory'

# Чтобы allauth распознал нашу форму как ту, что должна выполняться вместо
# формы по умолчанию, необходимо добавить.
ACCOUNT_FORMS = {"signup": "accounts.forms.CustomSignupForm"}

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

EMAIL_HOST_USER = "AndreyTestSF"
# логин пользователя почтового сервера
EMAIL_HOST_PASSWORD = "zuqvkobqbkixymje"  # noqa
# пароль пользователя почтового сервера
EMAIL_USE_TLS = False
EMAIL_USE_SSL = True

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

ADMINS = (
    ('ADMIN', 'ADMIN@zhiza.net'),
    ('admin', 'admin@mail.com'),
)

EMAIL_SUBJECT_PREFIX = 'Bulletin Board'
