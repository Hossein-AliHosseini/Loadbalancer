from flask import Flask
import subprocess
import requests

app = Flask(__name__)

curr = 0

@app.route('/')
def main_function():
    list_ports = subprocess.run(['docker ps --format \'{{ .Ports }}\''], shell=True, capture_output=True).stdout.decode('utf-8').split()
    # global ports
    ports = []
    for i in range(0, len(list_ports), 4):
        ports.append(list_ports[i][8:12])
    global curr
    print(curr)
    response = requests.get('http://localhost:' + ports[curr])
    if curr == len(ports)-1:
        curr = 0
    else:
        curr += 1
    return response.text

if __name__ == '__main__':
    app.run(debug=True)
