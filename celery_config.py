from config import BROKER_URL,CELERY_RESULT_BACKEND

BROKER_URL = BROKER_URL

CELERY_RESULT_BACKEND = CELERY_RESULT_BACKEND
CELERY_TASK_SERIALIZER = "msgpack"
CELERY_RESULT_SERIALIZER = "json"
CELERY_TASK_RESULT_EXPIRES = 60 * 60 * 24
CELERY_ACCEPT_CONTENT = ['json','msgpack']

CELERY_MONGODB_BACKEND_SETTINGS = {
    "taskmeta_collection" : "celery"
}

CELERY_TIMEZONE = "Asia/Shanghai"