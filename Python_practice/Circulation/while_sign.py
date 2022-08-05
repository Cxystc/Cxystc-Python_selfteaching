#while2
prompt = "\n Tell me something ,and I will repeat it back to you"
prompt += "\n Enter 'quit' to end the progame"
active = True
while active:
	message = input(prompt)

	if message == "quit":
		active = False
	else:
		print(message)
	
#sign 退出	