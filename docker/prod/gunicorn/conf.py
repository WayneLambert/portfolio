import multiprocessing

name = 'ab_back_end'
loglevel = 'debug'
errorlog = '-'
accesslog = '%(h)s %(l)s %(u)s %(t)s "%(r)s" %(s)s %(b)s "%(f)s" "%(a)s"'
bind = '0.0.0.0:8000'
workers = multiprocessing.cpu_count() * 2 + 1
