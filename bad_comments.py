# (c) Maximilian Schwarzmüller / Academind GmbH
# Created in 2020

# ***************
# GLOBALS
# ***************
sqlDriver: any
mongoDbDriver: any

# ***************
# CLASSES
# ***************
# Acts as an adapter, connecting models to various database engines (SQL, MongoDB)
class Database:
  __dbDriver: any; # the database engine to which we connect

  def __init__(self, dbDriver):
    self.__dbDriver = dbDriver 

  def loadDatabaseDriver(self, driver):
    if (driver == 'sql'): 
      # Connect to the SQL Driver if "driver" is set to SQL
      self.dbDriver = sqlDriver
    else: 
      # Otherwise, connect to MongoDB
      self.dbDriver = mongoDbDriver
    


  def connect(self): 
    self.dbDriver.connect(); # self may fail and throw an error
  

  def insertData(self, data: any): 
    self.dbDriver.insert(data); # updates a user
  

  def findOne(self, id): 
    # Todo: Needs to be implemented
    pass

  # findMany(filter: any) {
  #   self.dbDriver.find(filter);
  # }
