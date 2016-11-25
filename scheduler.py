import webapp2
import dateutil.parser
import httplib2
import urllib
from google.appengine.api import taskqueue


class ScheduleHandler(webapp2.RequestHandler):
    def post(self):
        data = dict(self.request.POST)
        if data['eta'] is None:
            self.response.body('eta is a required field')
            self.response.status = '400 Bad Request'
            return
        if data['callback_url'] is None:
            self.response.body('callback_url is a required field')
            self.response.status = '400 Bad Request'
            return
        eta = dateutil.parser.parse(data['eta'])
        taskqueue.add(url='/worker', eta=eta, params=data)


class ScheduleWorker(webapp2.RequestHandler):
    def post(self):
        data = dict(self.request.POST)
        url = data['callback_url']
        print(url)
        # using httplib2 because GAE doesn't fully support Requests library
        http = httplib2.Http(timeout=30)
        body = urllib.urlencode(data)
        headers = {'Content-type': 'application/x-www-form-urlencoded'}
        resp, content = http.request(url, 'POST', headers=headers, body=body)
        print(resp, content)


