'''Created on 2012-3-16@author: zongzong'''from mongokit import *import datetimeimport hashlib, hmac, base64, refrom db.mongo import Mongofrom tornado import options  import uuid  @Mongo.db.connection.registerclass Custormer(Document):      structure = {                 '_id':unicode,                 'cname':basestring,                 'yname':basestring,                 'status':int,                 'description':basestring,                 'continue_to':int,                 'ctype':int,                 'begin_at':datetime.datetime,                 'created_at':datetime.datetime,                 'suspended_at':datetime.datetime                 }    use_dot_notation = True    @staticmethod    def lookup(c_id):        return Mongo.db.ui.custormers.custormer.find_one({'_id' : c_id})        @staticmethod    def getProducts(cname):        return [u for u in Mongo.db.ui.custormers.find({'cname' : cname})]        @staticmethod    def getCustormers(name, status, yname):        c = Custormer()        if status:            c.status = status          if name:            c._id = name        if yname:            c.yname = yname        custormers = [w for w in Mongo.db.ui['custormers'].find({'cname':{'$regex':c._id}, 'status':int(c.status), 'yname':yname})]                                                                      return custormers        @staticmethod    def getAllCustormers(yname):          custormers = [c for c in Mongo.db.ui['custormers'].find({'yname':yname})]        return custormers        @staticmethod    def insertCustorm(yname, status, description, cname, begin_at, suspended_at, continue_to, ctype):        c = Custormer.instance(yname, status, description, cname, begin_at, suspended_at, continue_to, ctype)        Mongo.db.ui['custormers'].insert(c)            @staticmethod    def updateCustorm(_cid, status, continue_to, begin_at, suspended_at):        c = Custormer.lookup(_cid)        c.status = status        c.continue_to = continue_to        c.begin_at = begin_at        c.suspended_at = suspended_at          Mongo.db.ui['custormers'].update(c)                 '''    creates a new tool instance. unsaved    '''    @staticmethod    def instance(yname, status, description, name, begin_at, suspended_at, continue_to, ctype):        cname = normalize(name)#custormer's name        c = Custormer()        c['_id'] = uuid.uuid1()        c.cname = cname        c.yname = yname        c.status = status #custormer's name 1 for alive / 0 for died        c.description = description        c.continue_to = continue_to        c.created_at = datetime.datetime.now()        c.begin_at = begin_at        c.suspended_at = suspended_at        c.ctype = ctype        return c     '''normalizes a tool id'''def normalize(name):      if not name :        return None    #allow legal email address    name = name.strip().lower()    name = re.sub(r'[^a-z0-9\\.\\@_\\-~#]+', '', name)    name = re.sub('\\s+', '_', name)    #don't allow $ and . because they screw up the db.    name = name.replace(".", "")    name = name.replace("$", "")    return name;           