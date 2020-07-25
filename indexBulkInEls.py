import json
from tornado import ioloop, httpclient

elasticsearch_index_to_insert = 'crm_fac'
id_field = 'id'
body = ''

request_url = 'http://localhost:9200/' + elasticsearch_index_to_insert + '/_bulk'

with open('els.json') as json_file:
    data = json.load(json_file)
    hits = data['hits']['hits']
    count = 0
    hits_size = len(hits)
    for hit in hits:
        count = count + 1
        print(str(count) + "/" + str(hits_size))
        obj = hit["_source"]
        id = obj[id_field]
        temp = '{ "index" : {  "_id" : "'+ id +'" } }\n' + json.dumps(obj) + '\n'
        body = body + temp

i = 0
def handle_request(response):
    print '%d %s' % (response.code, response.body)
    global i
    i -= 1
    if i == 0:
        ioloop.IOLoop.instance().stop()

http_client = httpclient.AsyncHTTPClient()

postHeaders = {
    "Content-Type": "application/json"
}

#for future implementation
for iterator in range(1):
    i += 1
    print("sending request")
    http_client.fetch(request_url, handle_request, method='POST', headers=postHeaders, body=body)

ioloop.IOLoop.instance().start()