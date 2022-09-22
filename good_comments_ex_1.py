# (c) Maximilian Schwarzmüller / Academind GmbH
# Created in 2020

sqlDriver: any
mongoDbDriver: any

class DatabaseAdapter:
  __dbEngine: any

  def __init__(self, dbDriver):
    self.__dbDriver = dbDriver 

  def loadDatabaseDriver(self, engine):
    if (engine == 'sql'): 
      self.dbEngine = sqlDriver
    else: 
      self.dbEngine = mongoDbDriver
    
  def connect(self):
    self.dbEngine.tryConnect()


  def insertData(self, data: any):
    self.dbEngine.insert(data)
  

  def findOne(self, id):
    # Todo: Needs to be implemented
    pass  
