from peewee import *
import datetime

DATABASE_NAME = '/tmp/OrderDelivery.db'
db = SqliteDatabase(DATABASE_NAME)

class BaseModel(Model):
    class Meta:
        database = db

class Headquarter(BaseModel):
    id = IntegerField(unique=True)
    name = CharField(max_length = 64, null = False)

class Branch (BaseModel):
	id = IntegerField(unique = True, primary_key = True)
	name = CharField(max_length = 64, null = False)
	hqID = ForeignKeyField(Headquarter, backref='Branchs')
    
class Supplier (BaseModel):
	id = AutoField() # IntegerField(unique=True)
	name = CharField(column_name = 'supplier_name', null = False) # table_name = 'Supplier'

class Order (BaseModel):
    id = IntegerField(unique = True, primary_key = True)
    date = DateTimeField(default = datetime.datetime.now) # created_date =
    branchID = ForeignKeyField(Headquarter, backref = 'OrdersByBranch')
    
class Product (BaseModel):
    id = IntegerField(unique = True)
    supplierID = ForeignKeyField(Supplier, backref = 'ProductsBySupplier')
    name = CharField(max_length = 64, null = False)

class OrderDetail (BaseModel):
    id = IntegerField(unique = True)
    orderId = ForeignKeyField(Order, backref='OrderDetailsById')
    
class Delivery (BaseModel):
    id = AutoField()
    deliveryDate = DateTimeField(default = datetime.datetime.now)
    supplierID = ForeignKeyField(Supplier, backref = 'DeliveryBySupplier')

class DetailsDelivery (BaseModel):
    id = AutoField()
    supplierID = ForeignKeyField(Supplier, backref = 'DetailsByDelivery')