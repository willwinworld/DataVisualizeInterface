#! python2
# -*- coding: utf-8 -*-
import os
import json
import subprocess
from flask import Flask, render_template, request, jsonify, session, Response
from flask_bootstrap import Bootstrap
from flask_wtf import Form
from wtforms import StringField, SubmitField, HiddenField
from wtforms.validators import DataRequired
from peewee import RawQuery
from model import Crime
"""python -m SimpleHTTPServer 8000"""
app = Flask(__name__)
app.config['SECRET_KEY'] = 'very hard to guess string'
app.config['BOOTSTRAP_SERVE_LOCAL'] = True
bootstrap = Bootstrap(app)


@app.route('/stream_province', methods=['POST'])
def stream_province():
    def generate():
        log_path = '../sd/log'
        with open('%s/山东省人民检察院.log' % log_path, 'r') as f:
            yield f.read()

    return Response(generate(), mimetype='text/plain')


@app.route('/stream_city/<cityname>', methods=['POST'])
def stream_city(cityname):
    def generate():
        program_path = '../sd'
        with open('%s/log/%s.log' % (program_path, cityname), 'r') as f:
            yield f.read()

    return Response(generate(), mimetype='text/plain')


@app.route('/')
def index():  # index主页面并不渲染，并不需要表单
    program_path = '../sd'
    file_names = [x.replace('.py', '') for x in os.listdir(program_path) if x != 'dialogue' and x != 'log' and x != 'sd_model.py' and len(x) < 10]
    return render_template('index.html', dirs=file_names)


@app.route('/province', methods=['GET', 'POST'])
def province():
    program_path = '../sd'
    file_names = [x.replace('.py', '') for x in os.listdir(program_path) if x != 'dialogue' and x != 'log' and x != 'sd_model.py' and len(x) < 10]
    province_spider_name = u'山东省人民检察院.py'  # debug
    form = PostDataForm(request.values, hidden_field=province_spider_name)
    if form.validate_on_submit():
        subprocess.Popen(['python', province_spider_name.encode('gbk', 'ignore')], cwd='%s' % program_path)
        return render_template('submit_province_success.html', string=province_spider_name, dirs=file_names)
    return render_template('province.html', form=form, dirs=file_names)


@app.route('/city/<cityname>', methods=['GET', 'POST'])
def city(cityname):
    program_path = '../sd'
    city_spider_name = ''
    file_names = [x.replace('.py', '') for x in os.listdir(program_path) if x != 'dialogue' and x != 'log' and x != 'sd_model.py' and len(x) < 10]
    for file_name in file_names:
        city_spider_name = file_name
    form = PostDataForm(request.values, hidden_field=cityname)
    if form.validate_on_submit():
        subprocess.Popen(['python', city_spider_name+'.py'], cwd='%s' % program_path)
        return render_template('submit_city_success.html', cityname=cityname, string=cityname, dirs=file_names)
    return render_template('city.html', cityname=cityname, form=form, dirs=file_names)


@app.route('/chart', methods=['GET', 'POST'])
def chart():
    res = []
    program_path = '../sd'
    file_names = [x.replace('.py', '') for x in os.listdir(program_path) if
                  x != 'dialogue' and x != 'log' and x != 'sd_model.py' and len(x) < 10]
    rq = RawQuery(Crime,
                  'select count(*) as count , date(created_time) as created_time from crime group by date(created_time)')
    rq.execute()
    count = 0
    for obj in rq.execute():
        res.append({'index': count, 'date': obj.created_time.strftime("%Y-%m-%d"), 'number': obj.count})
        count += 1
    """传json data到前端页面"""
    return render_template('chart.html', items=res, dirs=file_names)


class PostDataForm(Form):
    hidden_field = HiddenField('hidden_field', validators=[DataRequired()])
    submit_run = SubmitField(u'运行')


if __name__ == '__main__':
    app.run(debug=True)