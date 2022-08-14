import random
import string

print('Welcome to your personal password generator.')

available_characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

number_of_passwords = int(input('Enter the amount of passwords you want to generate: '))

length_of_password = int(input('Enter the length of the password you want to generate: '))

print('/nyour result of the generated passwords:')

for pwds in range(number_of_passwords):
	passwords = ''
	for char in range(length_of_password):
		passwords += random.choice(available_characters)
	print(passwords)



