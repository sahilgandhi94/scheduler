import httplib2
import urllib
import webapp2

from datetime import datetime


def _send_request(url, data=None):
    http = httplib2.Http(timeout=30)
    if data is None:
        body = urllib.urlencode('')
    else:
        body = urllib.urlencode(data)
    headers = {'Content-type': 'application/x-www-form-urlencoded'}
    resp, content = http.request(url, 'POST', headers=headers, body=body)
    return resp, content


# Example:
# class GenerateSortingOrder(webapp2.RequestHandler):
#     def get(self):
#         url = "http://api2.workindia.in/api/jobs/generate-sort-order/"
#         _send_request(url=url)
