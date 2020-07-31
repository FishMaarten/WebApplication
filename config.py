import os
directory = os.path.dirname(os.path.abspath(__file__))

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "super-duper-secret"
