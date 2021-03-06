"""
Django settings for csDjango project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://Docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://Docs.djangoproject.com/en/2.1/ref/settings/

项目配置是根据实际开发需求从而对珍格格Web框架编写相关配置信息.配置信息主要由项目的setting.py实现.
主要配置有项目路径,密钥配置,域名访问权限,App列表,配置静态资源,配置模板文件,数据库配置,中间件和缓存配置
"""

import os

# 项目路径
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
from datetime import timedelta

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/
# 密钥配置
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'etg2)8%62c1bz555@71%x$r6@_l^5i0dg+qhe1^aia#k6gg)4x'

# SECURITY WARNING: don't run with debug turned on in production!
# 调试模式
# 当DEBUG为True并且ALLOWED_HOSTS为空时,项目只允许以localhost或127.0.0.1在浏览器上访问
# 当DEBUG为False时,ALLOWED_HOSTS为必填项,否则程序无法启动,如果想允许所有域名ALLOW_HOSTS=['*']
DEBUG = True

# 域名访问权限
ALLOWED_HOSTS = ["*", ]

AUTH_USER_MODEL = 'Users.User'

# App列表
# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'corsheaders',
    'rest_framework',
    'Dishes.apps.DishesConfig',
    'Orders.apps.OrdersConfig',
    'Tables.apps.TablesConfig',
    'Users.apps.UsersConfig',
    'Announcements.apps.AnnouncementsConfig',
    'django_filters',
    # 'drf_writable_nested',
]

MIDDLEWARE = [
    # 配置属性MIDDLEWARE的数据格式为列表类型,每个中间件的设置顺序是固定的,
    # 如果随意变更中间件很容易导致程序异常
    'django.middleware.security.SecurityMiddleware',  # 内置的安全机制,保护用户与网站的通信安全
    'django.contrib.sessions.middleware.SessionMiddleware',  # 会话Session功能
    # 使用中文
    # 'django.middleware.locale.LocaleMiddleware',    # 支持中文语言
    'django.middleware.common.CommonMiddleware',  # 处理请求信息,规范化请求内容
    'corsheaders.middleware.CorsMiddleware',
    # 'django.middleware.csrf.CsrfViewMiddleware',    # 开启CSRF防护功能
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # 开启内置的信息提示功能
    'django.contrib.messages.middleware.MessageMiddleware',  # 开启内置的信息提示功能
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # 防止恶意程序点击劫持
]

ROOT_URLCONF = 'DinDonBackend.urls'
# DRF的一些配置
REST_FRAMEWORK = {
    # 分页器设置
    'DEFAULT_PAGINATION_CLASS': 'DinDonBackend.pagination.StandardResultsSetPagination',
    'PAGE_SIZE': 10,
    # 过滤器设置
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',
                                #                             'rest_framework.filters.SearchFilter',
                                #                             'rest_framework.filters.OrderingFilter'
                                ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}
# 手机号正则表达式
REGEX_PHONE = "1[3|4|5|7|8][0-9]{9}"

# JWT 配置
SIMPLE_JWT = {
    'ACCESS_TOKEN_LIFETIME': timedelta(minutes=15),
}

TEMPLATES = [
    {
        # BACKEND: 定义模板引擎,用于识别模板里面的变量和指令.
        # 内置的模板引擎有Django Template和jinja2.Jinja2
        # 每个模板引擎都有自己的变量和指令语法
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        # DIRS: 设置模板所在路径,告诉Django在哪个地方查找模板的位置,默认为空列表
        'DIRS': [os.path.join(BASE_DIR, 'templates'),
                 os.path.join(BASE_DIR, 'index/templates')],
        # APP_DIRS: 是否在App里查找模板文件
        'APP_DIRS': True,
        # OPTIONS: 用于填充在RequestContext中上下文的调用函数,一般情况下不做任何修改
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'DinDonBackend.wsgi.application'

# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    # 'default': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'Dindon',
    #     'USER': 'root',
    #     'PASSWORD': '321',
    #     'HOST': '127.0.0.1',
    #     'PORT': '3306',
    # }
    # ,
    # # 多个数据库
    # # 第二个数据库
    # 'MyDjango': {
    #     'ENGINE': 'django.db.backends.mysql',
    #     'NAME': 'MyDjango_db',
    #     'USER': 'root',
    #     'PASSWORD': '1234',
    #     'HOST': '127.0.0.1',
    #     'PORT': '3306',
    # }
    # ,
    # 第三个数据库
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]

# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

# 设置时区
LANGUAGE_CODE = 'zh-hans'  # 中文支持，django1.8以后支持；1.8以前是zh-cn
TIME_ZONE = 'Asia/Shanghai'
USE_I18N = True
USE_L10N = True
USE_TZ = False  # 默认是Ture，时间是utc时间，由于我们要用本地时间，所用手动修改为false！！！！

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

# 设置根目录的静态资源文件夹 public_static
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'public_static')]
# 设置App(index)的静态资源文件夹(index_static)
os.path.join(BASE_DIR, 'index/index_static')

# STATIC_ROOT的作用是方便在服务器上部署项目,实现服务器和项目之间的映射
STATIC_ROOT = os.path.join(BASE_DIR, 'all_static')

# 跨域请求配置
CORS_ALLOW_CREDENTIALS = True
CORS_ORIGIN_ALLOW_ALL = True
# CORS_ORIGIN_WHITELIST = [
#     "http://127.0.0.1:9000",
# ]
CORS_ALLOW_METHODS = (
    'DELETE',
    'GET',
    'OPTIONS',
    'PATCH',
    'POST',
    'PUT',
    'VIEW',
)

CORS_ALLOW_HEADERS = (
    'XMLHttpRequest',
    'X_FILENAME',
    'accept-encoding',
    'authorization',
    'content-type',
    'dnt',
    'origin',
    'user-agent',
    'x-csrftoken',
    'x-requested-with',
    'Pragma',
)
