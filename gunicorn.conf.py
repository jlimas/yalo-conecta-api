import multiprocessing

wsgi_app = "yalo.wsgi"
bind = "127.0.0.1:8080"
workers = multiprocessing.cpu_count() * 2 + 1
