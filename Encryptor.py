from random import shuffle

global characters
characters = ['a','b','c','d','e','f','g','h','i','j','k',\
'l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','A',\
'B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q',\
'R','S','T','U','V','W','X','Y','Z','0','1','2','3','4','5','6',\
'7','8','9','+','-','[',' ','*','&','%','!','@',']','#','$','^',\
'(',')','_','{',',','.','?','/','|','<','}','>','~','=',':',';'\
'"',"'",'\\','`']
rst_characters = characters


def encrypt(message):
	message_length = len(message)
	i=0
	global encrypted_message
	encrypted_message = ''
	shuffle(characters)
	while i < message_length:
		if message[i] in characters:
			char_pos = characters.index(message[i])
			if char_pos < len(characters)-1:
				encrypted_message += characters[char_pos+1]
			else:
				encrypted_message += characters[0]
		else:
			encrypted_message += message[i]	
		i+=1
	print(encrypted_message)


def decrypt():
	message_length = len(encrypted_message)
	i=0
	decrypted_message = ''
	while i < message_length:
		if encrypted_message[i] in characters:
			char_pos = characters.index(encrypted_message[i])
			if char_pos != 0:
				decrypted_message += characters[char_pos-1]
			else:
				decrypted_message += characters[len(characters)-1]
		else:
			decrypted_message += message[i]	
		i+=1
	print(decrypted_message)
	
	
while True:
	message = input("Send a message\n")
	print("Here is your message encrypted:")
	encrypt(message)
	command = input("would you like to decrypt this message?\n")
	if command.lower() == 'yes':
		decrypt()
	end_prompt = input('Continue?\n')
	if end_prompt == 'no':
		break
	characters = rst_characters
