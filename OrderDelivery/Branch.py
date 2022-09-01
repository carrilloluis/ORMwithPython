from peewee import *

db = SqliteDatabase('/tmp/OrderDelivery.db')

class Branch (Model):
	id = IntegerField()
	name = StringFields()
	class Meta:
		database = db