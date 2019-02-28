#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


from flask import Flask, request
from tinydb import TinyDB, Query


def create_app(test_config=None):
    import json


    app = Flask(__name__, instance_relative_config=True)

    db = TinyDB('./pages.json')


    @app.route('/pages/<int:page_id>')
    def get_page(page_id):
        Page = Query()
        result = db.search(Page.id == page_id)
        return f'Hello: {result}'


    @app.route('/pages/', methods=['POST'])
    def post_page():
        return json.dumps(request.form)


    return app
