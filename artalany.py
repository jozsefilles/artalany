#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


from flask import Flask, request, abort
from tinydb import TinyDB, Query
from dataclasses import dataclass, asdict


@dataclass
class Page:
    url: str
    xpath: str


def create_app(test_config=None):
    import json


    app = Flask(__name__, instance_relative_config=True)

    db = TinyDB('./pages.json')


    @app.route('/pages/<int:page_id>')
    def get_page(page_id):
        page = db.get(doc_id=page_id)
        if page is None:
            abort(404)
        else:
            return json.dumps(page)


    @app.route('/pages/', methods=['POST'])
    def post_page():
        page = Page(request.form['url'], request.form['xpath'])
        page_id = db.insert(asdict(page))
        return str(page_id)


    return app
