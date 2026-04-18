import os
from pathlib import Path

# 1. ตั้งค่า Path หลักของโปรเจกต์
BASE_DIR = Path(__file__).resolve().parent.parent

# 2. Security Settings
SECRET_KEY = 'django-insecure-+o7iz13%q=4@^8@b0mmlen&s7kfj%x8s=m%0sng+ah!4lt$ktx'

# ปรับให้ยืดหยุ่นสำหรับการ Deploy
DEBUG = True 

# เพิ่ม '*' เพื่อให้เข้าใช้งานผ่าน URL ของ Cloud ได้
ALLOWED_HOSTS = ['*'] 

# 3. Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'shop', 
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    # เพิ่มบรรทัดนี้เพื่อจัดการไฟล์ Static ตอนออนไลน์ (ต้อง pip install whitenoise)
    'whitenoise.middleware.WhiteNoiseMiddleware', 
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'pang_organic.urls'

# 4. การตั้งค่า Templates
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')], 
        'APP_DIRS': True, 
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                # บรรทัดนี้สำคัญสำหรับการดึงรูปภาพมาโชว์ในหน้าเว็บ
                'django.template.context_processors.media', 
            ],
        },
    },
]

WSGI_APPLICATION = 'pang_organic.wsgi.application'

# 5. Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# 6. Password validation
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# 7. Internationalization
LANGUAGE_CODE = 'th' 
TIME_ZONE = 'Asia/Bangkok' 
USE_I18N = True
USE_TZ = True

# 8. Static & Media files
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static'),
]
# สำคัญสำหรับการรวมไฟล์ Static ไปที่โฟลเดอร์เดียวตอน Deploy
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# การตั้งค่ารูปภาพ (Media)
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# ตั้งค่า Storage สำหรับไฟล์ Static (แนะนำสำหรับมือใหม่ที่ Deploy)
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'