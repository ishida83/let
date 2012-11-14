'''Created on 2012-3-16@author: zongzong'''from mongokit import Documentimport datetimeimport refrom db.mongo import Mongoimport uuid @Mongo.db.connection.registerclass Product(Document):      structure = {                 '_id':unicode,                 'cname':basestring,                 'oname':basestring,                 'status':int,                 'address':basestring,                 'phonenum':basestring,#                 'begin_ip':basestring,#                 'suspended_ip':basestring,                 'port':basestring,                 'device':basestring,                 'continue_to':int,                 'ctype':int,                 'price':int,                 'begin_at':datetime.datetime,                 'created_at':datetime.datetime,                 'suspended_at':datetime.datetime                 }    use_dot_notation = True    @staticmethod    def lookup(p_id):        return Mongo.db.ui.products.find_one({'_id' : uuid.UUID(p_id)})        @staticmethod    def getProduct(cname):        return [u for u in Mongo.db.ui.products.find({'cname' : cname})]        @staticmethod    def getProducts(name, status, oname):        c = Product()        if status:            c.status = status          if name:            c._id = name        if oname:            c.oname = oname        products = [w for w in Mongo.db.ui['products'].find({'cname':{'$regex':c._id}, 'status':int(c.status), 'oname':oname})]                                                                return products        @staticmethod    def getAllProducts(name, oname):        c = Product()        if name:            c._id = name        if oname:            c.oname = oname        products = [w for w in Mongo.db.ui['products'].find({'cname':{'$regex':c._id}, 'oname':oname})]                                                                return products            @staticmethod    def getOperatorProducts(oname):          products = [c for c in Mongo.db.ui['products'].find({'oname':oname})]        return products        #    @staticmethod#    def insert(yname, status, cname, begin_at, suspended_at, continue_to, ctype, address, phonenum, price,begin_ip,suspended_ip):#        c = Product.instance(yname, status, cname, begin_at, suspended_at, continue_to, ctype, address, phonenum, price,begin_ip,suspended_ip)#        Mongo.db.ui['products'].insert(c)       @staticmethod    def insert(oname, status, cname, device, port, begin_at, suspended_at, continue_to, ctype, address, phonenum, price):        c = Product.instance(oname, status, cname, device, port, begin_at, suspended_at, continue_to, ctype, address, phonenum, price)        Mongo.db.ui['products'].insert(c)              @staticmethod    def update(_cid, status, continue_to, begin_at, suspended_at):        c = Product.lookup(_cid)        c.status = status          c.continue_to = continue_to        c.begin_at = begin_at        c.suspended_at = suspended_at          Mongo.db.ui['products'].Product.update(c)            @staticmethod    def updateProduct(_cid, status):        Mongo.db.ui['products'].update({"_id":uuid.UUID(_cid)}, {'$set':{'status':status}})                 '''    creates a new tool instance. unsaved    '''    @staticmethod    def instance(oname, status, cname, device, port, begin_at, suspended_at, continue_to, ctype, address, phonenum, price):        cname = normalize(cname)#Operators's name        c = Product()        c['_id'] = uuid.uuid1()        c.cname = cname          c.oname = oname        c.status = status #Operators's name 1 for alive / 0 for died        c.address = address        c.phonenum = phonenum        c.price = price#        c.begin_ip = begin_ip#        c.suspended_ip = suspended_ip        c.port = port        c.device = device        c.continue_to = continue_to        c.created_at = datetime.datetime.now()        c.begin_at = begin_at        c.suspended_at = suspended_at        c.ctype = ctype        return c       '''normalizes a tool id'''def normalize(name):      if not name :        return None    #allow legal email address    name = name.strip().lower()#    name = re.sub(r'[^a-z0-9\\.\\@_\\-~#]+', '', name)    name = re.sub('\\s+', '_', name)    #don't allow $ and . because they screw up the db.    name = name.replace(".", "")    name = name.replace("$", "")    return name;           