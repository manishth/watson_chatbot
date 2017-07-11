import json
from watson_developer_cloud import ConversationV1


conversation = ConversationV1(
	username='xxxxxxxxxx',
	password='xxxxxxxx',
	version='2016-09-20')

workspace_id = 'xxxxxxxxxxxxxxxxxxxx'


incoming_message = "Hello chatbot"


response = conversation.message(workspace_id=workspace_id, message_input={
	'text': incoming_message})


print(json.dumps(response, indent=2))

print(response["output"]["text"])