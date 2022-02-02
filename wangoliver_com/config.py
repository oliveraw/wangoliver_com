"""Insta485 development configuration."""

import pathlib

# Root of this application, useful if it doesn't occupy an entire domain
APPLICATION_ROOT = '/home/wangambk/www/wangoliver_com'

# Secret key for encrypting cookies
# SECRET_KEY = b'\xf6\x0ch=\xc2\xb5\xd2\x81\xad'
# '\x9c<j\x94\xd5\x889M\x17\x15j_\xe3\\?'
# SESSION_COOKIE_NAME = 'login'

# # File Upload to var/uploads/
APP_ROOT = pathlib.Path(__file__).resolve().parent.parent
UPLOAD_FOLDER = APP_ROOT/'uploads'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
# MAX_CONTENT_LENGTH = 16 * 1024 * 1024

# # Database file is var/insta485.sqlite3
# DATABASE_FILENAME = INSTA485_ROOT/'var'/'insta485.sqlite3'
