from peewee import *
import datetime

DATABASE_NAME = '/tmp/OrderDelivery.db'
# DATABASE_NAME = 'OrderDelivery.db'

def getConnection2DB():
	db = SqliteDatabase(DATABASE_NAME) 
	# db = MySQLDatabase('the_db_name', user='xxxxx', passwd='xxxxx')  host='localhost', port=3306, db='xxxxx'
	db.connect()
	return db

db = getConnection2DB()

class BaseModel(Model):
	class Meta:
		database = db

class Headquarter (BaseModel):
	id = IntegerField(column = 'a_', primary_key = True) # unique = True)
	name = CharField(column = 'b_', max_length = 64, null = False)

	@property
	def serialize(self):
		return {
			'code': self.id,
			'desc': str(self.name).strip(),
		}
		
class Branch (BaseModel):
	id = IntegerField(column_name = 'a_', primary_key = True) # unique = True, 
	name = CharField(column_name = 'b_', max_length = 64, null = False)
	subsidiary = ForeignKeyField(Headquarter, column_name = 'c_', backref='Branchs')

	@property
	def serialize(self):
		return {
			'code': self.id,
			'desc': str(self.name).strip(),
		} # 'owner': str(self.hqID),

class Supplier (BaseModel):
	id = AutoField() # IntegerField(unique=True)
	name = CharField(column_name = 'supplier_name', null = False) # table_name = 'Supplier'

	@property
	def serialize(self):
		tmpSupplier = {
			'code': self.id,
			'name': str(self.name).strip(),
		} # 'owner': str(self.hqID),
		return tmpSupplier

class Order (BaseModel):
	id = IntegerField(unique = True, primary_key = True)
	date = DateTimeField(default = datetime.datetime.now) # created_date =
	branchID = ForeignKeyField(Headquarter, backref = 'OrdersByBranch')

	@property
	def serialize(self):
		tmpSupplier = {
			'code': self.id,
			'name': str(self.name).strip(),
		} # 'owner': str(self.hqID),
		return tmpSupplier

class Product (BaseModel):
	id = IntegerField(unique = True)
	supplierID = ForeignKeyField(Supplier, backref = 'ProductsBySupplier')
	name = CharField(max_length = 64, null = False)

	@property
	def serialize(self):
		tmpSupplier = {
			'code': self.id,
			'name': str(self.name).strip(),
		} # 'owner': str(self.hqID),
		return tmpSupplier

class OrderDetail (BaseModel):
	id = IntegerField(unique = True)
	orderId = ForeignKeyField(Order, backref='OrderDetailsById')

if __name__ == '__main__':
	Headquarter.create_table()
	Branch.create_table()

'''
class Delivery (BaseModel):
	id = AutoField()
	deliveryDate = DateTimeField(default = datetime.datetime.now)
	supplierID = ForeignKeyField(Supplier, backref = 'DeliveryBySupplier')

class DetailsDelivery (BaseModel):
	id = AutoField()
	supplierID = ForeignKeyField(Supplier, backref = 'DetailsByDelivery')	

	def __repr__(self):
		return "{}, {}, {}".format(
			self.id,
			self.name,
			self.subsidiary
		)

	branchsSamples = (
		(1, 'Sede Cusco 01', 1),
		(2, 'Sede Cusco 02', 1),
		(3, 'Sede Cusco 03', 2)
	)
	for item_ in branchsSamples:
		c = Branch(id = item_[0], name=item_[1], hqID=item_[2])
		c.save()
	# with database:
	#	  database.create_tables([Headquarter, Branch]) # BlogPost.create_table()
'''