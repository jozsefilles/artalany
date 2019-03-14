#!/usr/local/bin/python3
# -*- coding: utf-8 -*-


from flask import Flask, request, abort, render_template
from tinydb import TinyDB, Query
from dataclasses import dataclass, asdict


@dataclass
class Page:
    name: str
    url: str
    xpath: str


def create_app(test_config=None):
    import json


    app = Flask(__name__, instance_relative_config=True)

    db = TinyDB('./pages.json')


    # API

    @app.route('/pages/<int:page_id>')
    def get_page(page_id):
        page = db.get(doc_id=page_id)
        if page is None:
            abort(404)
        else:
            return json.dumps(page)


    @app.route('/pages/', methods=['POST'])
    def post_page():
        page = Page(request.form['name'],
                    request.form['url'],
                    request.form['xpath'])
        page_id = db.insert(asdict(page))
        return str(page_id)


    # view methods

    @app.route('/')
    def index():
        return render_template('index.html')


    @app.route('/list_pages')
    def view_list_pages():
        pages = db.all()
        return render_template('list_pages.html', pages=pages)


    @app.route('/add_page', methods=['GET', 'POST'])
    def view_add_page():
        if request.method == 'GET':
            return render_template('add_page.html')
        elif request.method == 'POST':
            name = request.form['name']
            url = request.form['url']
            xpath = request.form['xpath']
            # TODO validate (not empty, etc.)

            page = Page(name, url, xpath)
            page_id = db.insert(asdict(page))
            return render_template('add_page.html',
                                   message=f'Page added with ID: {page_id}')


    return app
