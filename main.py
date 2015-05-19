import os

import webapp2
import jinja2

template_directory = os.path.join(os.path.dirname(__file__), "templates")
jinja_environment = jinja2.Environment(loader = jinja2.FileSystemLoader(template_directory),
                                      autoescape = True)

class Handler(webapp2.RequestHandler):
    def write(self, *a, **kw):
      self.response.out.write(*a, **kw)

    def render_string(self, template, **params):
      t = jinja_environment.get_template(template)
      return t.render(params)

    def render(self, template, **kw):
      self.write(self.render_string(template, **kw))

class MainPage(Handler):
    def get(self):
      self.render("main_page.html")

class Lesson1(Handler):
	def get(self):
	  self.render("lesson1.html")

class Lesson2(Handler):
	def get(self):
	  self.render("lesson2.html")

class Lesson3(Handler):
	def get(self):
	  self.render("lesson3.html")

class Lesson4(Handler):
    def get(self):
      items = self.request.get_all("food") #gets all items with name 'food' from the url storing them in the list 'items'
      self.render("lesson4.html", items=items)
		






app = webapp2.WSGIApplication([
    ('/', MainPage),
    ('/lesson1', Lesson1),
    ('/lesson2', Lesson2),
    ('/lesson3', Lesson3),
    ('/lesson4', Lesson4)
], debug=True)
