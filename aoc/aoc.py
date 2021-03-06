import os
import wsgiref.handlers

from google.appengine.ext.webapp import template
from google.appengine.ext import webapp
from google.appengine.ext import db

class Maps(db.Model):
	name = db.StringProperty(required=True)
	img = db.BlobProperty(required=True)
	x = db.IntegerProperty(required=True)
	y = db.IntegerProperty(required=True)
	
class ResType(db.Model):
	name = db.StringProperty(required=True)
	
class Resources(db.Model):
	name = db.StringProperty(required=True, choices=set(['ash', 
																		  'sandstone', 
																		  'copper', 
																		  'silver', 
																		  'cotton', 
																		  'oak', 
																		  'granite', 
																		  'iron', 
																		  'electrum', 
																		  'yew', 
																		  'basalt', 
																		  'orichalcum', 
																		  'gold']))
	map = db.ReferenceProperty(Maps, collection_name='resources', required=True)
	x = db.IntegerProperty(required=True)
	y = db.IntegerProperty(required=True)
	
	def __init__():
		pass

class MainPage(webapp.RequestHandler):
	def get(self):
	
		template_values = {
			'url': "Adresse",
		}

		path = os.path.join(os.path.dirname(__file__), 'base.htm')
		self.response.out.write(template.render(path, template_values))

class AddRes(webapp.RequestHandler):
	def get(self):
		
		template_values = {
			'url': "Adresse",
		}

		path = os.path.join(os.path.dirname(__file__), 'baseAdd.htm')
		self.response.out.write(template.render(path, template_values))

def main():
	application = webapp.WSGIApplication([('/', MainPage), 
													  ('/add', AddRes)], debug=True)
	wsgiref.handlers.CGIHandler().run(application)

if __name__ == "__main__":
	main()