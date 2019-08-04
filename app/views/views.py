import json
from static.context.context import CONTEXT
from static.cdn.cdn import CDN
from flask import Flask, jsonify
from jinja2 import Environment, FileSystemLoader, select_autoescape

env = Environment(loader=FileSystemLoader('./templates'),
                    autoescape=select_autoescape(['html', 'htm','xml',]))

app = Flask(__name__)


def jsonDumps(f):
	def dumps(args):
		return jsonify(f(args))
	return dumps


@app.route('/')
def index():
    context = CONTEXT
    template = env.get_template('index.html')
    return template.render(context)
    