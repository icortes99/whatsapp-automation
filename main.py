import pywhatkit as whats
import constants
import notion_connection

notion_client = notion_connection.connection()

#Open and read whats_info.txt
with open("whats_info.txt", "r") as file:
  lines = file.readlines()

for line in lines:
  lineSplit = line.strip().split(": ")

  if len(lineSplit) == 2:
    key, value = lineSplit[0], lineSplit[1]

    if key == constants.keys[0]:
      group_id = value
    elif key == constants.keys[1]:
      message_type = value
    elif key == constants.keys[2] and value == constants.possible_values[0]:
      is_active = True

      #If channel is active, send the proper message template via whatsapp
      if is_active:
        if message_type == constants.possible_values[1]:
          whats.sendwhatmsg_to_group_instantly(group_id, constants.message_new_student, 15, True, 3)
        elif message_type == constants.possible_values[2]:
          whats.sendwhatmsg_to_group_instantly(group_id, constants.message_couple_students, 15, True, 3)

#whats.sendwhatmsg_to_group_instantly(group_id, constants.message_new_student, 15, True, 3)
#whats.sendwhatmsg_to_group_instantly(group_id, constants.message_couple_students, 15, True, 3)