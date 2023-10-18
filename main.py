import pywhatkit as whats
import random
import constants
import notion_connection

notion_client = notion_connection.connection()

notion_response = notion_connection.read_database(notion_client, constants.notion_page_id)

message = random.choice(constants.messages_templates)

for entry in notion_response:
  chat_id = entry['properties']['id']['rich_text'][0]['text']['content']
  status = entry['properties']['Status']['status']['name']

  if status == 'In Progress':
    whats.sendwhatmsg_to_group_instantly(chat_id, message, 15, True, 3)