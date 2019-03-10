
from flask import Response
from .views import *
from halo_current_account_service.api.swagger.__init__ import load_app

def load_urls(app):
	stage = '/' + settings.ENV_NAME
	app.add_url_rule(stage+'/robots.txt', view_func= lambda r: Response("User-agent: *\nDisallow: /", content_type="text/plain"))
	app.add_url_rule(stage+'/perf/', view_func= PerfLink.as_view('Perf'))
	#app.add_url_rule('/static/(?P<path>.*)$', DocRootLink.as_view('document_root'))
	load_app(app,stage)
	if settings.SERVER_LOCAL == True:
		app.add_url_rule(stage+'/__event__/', view_func= EventLink__.as_view('_Event'))

	            






