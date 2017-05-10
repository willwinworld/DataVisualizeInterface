#! python2
# -*- coding: utf-8 -*-
import os
import subprocess
from flask import Flask, render_template, request, jsonify, session, Response
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired
"""python -m SimpleHTTPServer 8000"""
app = Flask(__name__)
app.config['SECRET_KEY'] = 'very hard to guess string'
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
bootstrap = Bootstrap(app)


@app.route('/stream_province', methods=['POST'])
def stream_province():
    def generate():
        province_log_path = '../procuratorate/province/log'
        with open('%s/douban250.log' % province_log_path, 'r') as f:
            yield f.read()

    return Response(generate(), mimetype='text/plain')


@app.route('/stream_city/<cityname>', methods=['POST'])
def stream_city(cityname):
    def generate():
        city_relative_path = '../procuratorate/cities'
        # print '%s/%s/log/test.log' % (city_relative_path, cityname)
        with open('%s/%s/log/test.log' % (city_relative_path, cityname), 'r') as f:
            yield f.read()

    return Response(generate(), mimetype='text/plain')


@app.route('/')
def index():  # index主页面并不渲染，并不需要表单
    relative_path = '../procuratorate/cities'
    file_names = os.listdir(relative_path)
    return render_template('index.html', dirs=file_names)


@app.route('/province', methods=['GET', 'POST'])
def province():
    city_relative_path = '../procuratorate/cities'
    file_names = os.listdir(city_relative_path)
    province_relative_path = '../procuratorate/province'
    # province_spider_name = 'sdjcy.py'
    province_spider_name = 'douban250.py'  # debug
    form = PostDataForm(request.values, hidden_field=province_spider_name)
    if form.validate_on_submit():
        subprocess.call('cd %s && python %s' % (province_relative_path, province_spider_name), shell=True)
        return render_template('submit_province_success.html', string=province_spider_name, dirs=file_names)
    return render_template('province.html', form=form, dirs=file_names)


@app.route('/city/<cityname>', methods=['GET', 'POST'])
def city(cityname):
    relative_path = '../procuratorate/cities'
    all_file_names = os.listdir(relative_path)
    city_spider_name = ''
    file_names = os.listdir('%s/%s' % (relative_path, cityname))
    for file_name in file_names:
        if file_name.endswith('.py') and 'model' not in file_name and file_name != 'test.py':
            city_spider_name = file_name
    form = PostDataForm(request.values, hidden_field=cityname)
    if form.validate_on_submit():
        # subprocess.call('cd %s/%s && python %s' % (relative_path, cityname, city_spider_name), shell=True)
        # return render_template('submit_success.html', string=city_spider_name, dirs=all_file_names)
        subprocess.call('cd %s/%s && python %s' % (relative_path, cityname, 'test.py'), shell=True)
        return render_template('submit_city_success.html', cityname=cityname, string=city_spider_name, dirs=all_file_names)
    return render_template('city.html', cityname=cityname, form=form, dirs=all_file_names)


class PostDataForm(Form):
    hidden_field = HiddenField('hidden_field', validators=[DataRequired()])
    submit_run = SubmitField(u'运行')


if __name__ == '__main__':
    app.run(debug=True)
    # app.run(host='127.0.0.1', port=8080)
    # app.run(host='0.0.0.0', port=8888)
