import httplib2
import urllib
import webapp2
import json

from datetime import datetime


def _send_post(url, data=None):
    http = httplib2.Http(timeout=30)
    if data is None:
        body = urllib.urlencode('')
    else:
        body = urllib.urlencode(data)
    headers = {'Content-type': 'application/x-www-form-urlencoded'}
    resp, content = http.request(url, 'POST', headers=headers, body=body)
    return resp, content

def _send_get(url):
    http = httplib2.Http(timeout=30)
    resp, content = http.request(url, 'GET')
    return resp, content


# Example:
# class GenerateSortingOrder(webapp2.RequestHandler):
#     def get(self):
#         url = "<API-URL>"
#         _send_request(url=url)


class CrawlerHeartbeat(webapp2.RequestHandler):
    def get(self):
        url = "<API-URL>"
        schedule_url = "<SCHEDULE-URL>"
        schedule_data = {}
        resp, content = _send_get(url=url)
        if resp['status'] == "200" and len(json.loads(content)['running']) == 0:
            resp, content = _send_post(schedule_url, schedule_data)
        self.response.write(content)