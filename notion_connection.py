from notion_client import Client
import constants

def connection():
  client = Client(auth = constants.notion_token)
  #page_response = client.pages.retrieve(constants.notion_page_id)
  return client

"""
def read_text(client, page_id):
  response = client.blocks.children.list(block_id = page_id)
  return response['results']

def create_objects_from_content(content):
  objects = []

  for obj in content:
    group_id = obj[constants.keys[0]]
    message_type = obj[constants.keys[1]]
    is_active = obj[constants.keys[2]]

    my_object = {
      'group_id': group_id,
      'message_type': message_type,
      'is_active': is_active
    }

    objects.append(my_object)
  
  return objects
"""

def read_database(client, db_id):
  result = client.databases.query(database_id = db_id)
  return result['results']