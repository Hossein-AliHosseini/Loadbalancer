import os
from threading import Thread
from flask import Flask
from redis import Redis

app1 = Flask('app1')
app2 = Flask('app2')
redis = Redis(host='redis', port=6379)


@app1.route("/")
def hello_world():
    name = os.environ.get('NAME')
    redis.incr(name+'hits')
    return "<p>Hello from {}</p>".format(name)

@app2.route("/")
def metrics():
    name = os.environ.get('NAME')
    reqs = redis.get(name+'hits')
    if not reqs:
        reqs = "0"
    else:
        reqs = str(reqs, 'utf-8')
    return "all_requests: {}".format(reqs)

def start1():
    app1.run(host='0.0.0.0', port=5000)

def start2():
    app2.run(host='0.0.0.0', port=9090)

if __name__ == "__main__":
    Thread(target=start2).start()
    app1.run(host='0.0.0.0', port=5000)
    # app2.run(host='0.0.0.0', port=9090)
