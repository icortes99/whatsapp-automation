from notion_client import Client
import constants

def connection():
  client = Client(auth = constants.notion_token)
  return client

def read_database(client, db_id):
  result = client.databases.query(database_id = db_id)
  return result['results']