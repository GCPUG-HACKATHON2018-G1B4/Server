from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
from flask import render_template
from google.cloud import bigquery
import re

app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

@app.route('/demo/')
def hello():
    return render_template('demo.html')


def query_result_parse(results):
    result_arr = []

    for row in results:
       cleanr =re.compile('<.*?>')
       cleantext = re.sub(cleanr, '', row.body)
       result_arr.append(
           {
               'id': row.id,
               'tags': row.tags,
               'score': row.score,
               'title': row.title,
               'body': cleantext[:80]
           }
       )
    
    return result_arr


def make_query(tag_list):
    main_query = """
    SELECT
        q.id,
        q.tags,
        q.score,
        q.title,
        a.body
    FROM
        `bigquery-public-data.stackoverflow.posts_questions` q
    ,
        `bigquery-public-data.stackoverflow.posts_answers` a
    WHERE
        q.id=a.parent_id
    AND
    """
    if len(tag_list) == 4:
        main_query += """
        q.tags LIKE '%{}%' and q.tags LIKE '%{}%' and a.body LIKE '%{}%' and a.body LIKE '%{}%'
        """.format(tag_list[0], tag_list[1], tag_list[2], tag_list[3])
    else:
        main_query += """
        q.tags LIKE '%{}%' and a.body LIKE '%{}%'
        """.format(tag_list[0], tag_list[1])
    
    main_query += """
    ORDER BY
        a.score DESC
    LIMIT
        5
    """
    return main_query
def query_process(request):
    tag_list = dict(request.args)['tag']
    client = bigquery.Client()
    query_job = client.query(make_query(tag_list))
    results = query_job.result()  # Waits for job to complete.
    return jsonify(query_result_parse(results))

@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

@app.route('/setting')
def tag():
    return query_process(request) 


@app.route('/realtime')
def real_time():
    print('realtime api!!')
    return query_process(request) 


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
