# -*- coding: utf-8 -*-
from __future__ import absolute_import


from .sd_current_account_v1.__init__ import bp,load_resource

def load_app(app,stage):
    load_resource(app)
    app.register_blueprint(
        bp,
        url_prefix=stage+'/sd-current-account/v1')