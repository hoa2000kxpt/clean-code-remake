# class Database {
#   private client: any;

#   get connectedClient() {
#     if (!this.client) {
#       throw new Error('Database not connected!');
#     }
#     return this.client;
#   }

#   connect() {
#     // Establishing connection ...
#     this.client = {};
#   }
# }

# const db = new Database();
# db.connectedClient.query();

class Database:
  __client = ""

  @classmethod
  def connectedClient(cls):
    if (cls.client):
      raise Exception('Database not connected!');
    return cls.client

  @classmethod
  def connect(cls):
    # Establishing connection ...
    cls.client = {}

db = Database()
db.connectedClient.query()
