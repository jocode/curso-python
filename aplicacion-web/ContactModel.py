from google.appengine.ext import ndb

class ContactModel(ndb.Model):
    name = ndb.StringProperty()
    phone = ndb.StringProperty()
    email = ndb.StringProperty()

