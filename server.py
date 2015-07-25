#my love for poutine has gone too far
import string
import json
import os
import sys
import webapp2

class InstantAPIServer(webapp2.RequestHandler):
    def get(self):


        self.response.headers['Content-Type'] = 'application/json'

        file_arg = "source.json"

        try:
            content = json.loads(open(file_arg).read())

            path = self.request.path[1:]
            components = string.split(path, '/')
            print components

            node = content
            for component in components:
                if len(component) == 0 or component == "favicon.ico":
                    continue

                if type(node) == dict:
                    node = node[component]

                elif type(node) == list:
                    node = node[int(component)]

        except IOError:
            self.response.set_status(404)
            node = json.loads("{\"error\":\"Couldn't find source\"}")


        self.response.write(json.dumps(node,indent=4))

        return

app = webapp2.WSGIApplication([(r'/.*', InstantAPIServer)],
debug=os.environ['SERVER_SOFTWARE'].startswith('Dev'))
