#!/bin/env python

from views.views import app

class BaseConfig(object):
    DEBUG = True
    SECRET_KEY = ""
    HOST ="localhost"
    PORT = 5000

class Develop(BaseConfig):
	pass

if __name__ == '__main__':
	dev = Develop()
	app.run(host=dev.HOST, port=dev.PORT, debug=dev.DEBUG)