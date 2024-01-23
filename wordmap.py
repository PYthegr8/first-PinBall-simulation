''' Papa Yaw Owusu Nti
    CS 152B
    Project 8
    November 7th 2023
    This program tests the use of dictionaries by taking user input for each prompt and
    prints out each key-value pair in the dictionary, 
    displaying the prompt as the key and the corresponding user response as the value.
'''
dictionary = { "Key" : "Value" } ##Empty dictionary

words = [ "Favorite color?" , "Favorite food?" , "Is today Friday?" ] ##Fill this in ]
##For loop over prompts
for word in words:

	##Get user input and assign to a variable
	user_response = input( word )
	#print( user_response )

	##assign user_response as the value for the key "Prompt"
	dictionary[ word ] = user_response ##Put user_response in the spot with "Prompt as they ey"
	##Prompt is the key and user_response is the value

for key in dictionary.keys():
	print( "Key: " , key )
	print( "Value: " , dictionary[ key ] )