import webbrowser

# Graphics

HelpBar = '--------------------------------'

# Graphics

# WhiteList/Commands

WhiteList = [
	"https://google.com",
	"https://irssi.org/",
	]

Commands = [
	"pyb.help",
	"pyb.whitelist",
	"pyb.info",
	]

# WhiteList/Commands

# Main

print('\x1b[1;35;49m')
print" _____     _                     _ _ _"
print"|  _  |_ _| |_ ___ ___ _ _ _ ___| | | |"
print"|   __| | | . |  _| . | | | |_ -| | | |"
print"|__|  |_  |___|_| |___|_____|___|_____|"
print"      |___| Written by Rory W."
print('\x1b[0m')
print('Please enter a full url, example: ' + '\033[0;32;49m' + 'https' + '\x1b[0m' + '://' + '\x1b[0;36;49m' + 'google' + '\x1b[0m' + '.' + '\x1b[0;35;49m' + 'com' + '\x1b[0m')
print('You can also enter a ' + '\x1b[3;37;43m' + 'COMMAND'  + '\x1b[0m' + ',' + ' example: ' + '\x1b[0;35;49m' + 'pyb' + '.' + '\x1b[0;32;49m' + 'help' + '\x1b[0m')

while True:	
	x = raw_input('Enter ' + '\x1b[6;30;42m' +  'URL' + '\x1b[0m' + '/' + '\x1b[3;37;43m' + 'COMMAND' + '\x1b[0m' + ': ')
	
	#whitelist
	if x == WhiteList[0]:
		print('You are at ' + '\x1b[0;30;42m' + x + '\x1b[0m')
		webbrowser.open(x, new=2)
	elif x == WhiteList[1]:
		print('You are at ' + '\x1b[0;30;42m' + x + '\x1b[0m')
		webbrowser.open(x, new=2)
	# Commands
	elif x == Commands[0]:
		print(HelpBar)
		print('*' + 'HELP/COMMANDS MENU' + '*' + '\n\npyb.<COMMAND>\n')
		print('\t.whitelist\n\t.info')
	elif x == Commands[1]:
		print(WhiteList[0:2])
	elif x == Commands[2]:
		print('\x1b[1;35;49m' + 'Pybrows' + '\x1b[0m' + '2018')
	else:
		print('This url was ether entered incorrectely or was blocked')
		print('Your input: ' + '\x1b[0;37;41m' + x + '\x1b[0m')

# Main

                                                     
# _____     _                     
#|  _  |_ _| |_ ___ ___ _ _ _ ___ 
#|   __| | | . |  _| . | | | |_ -|
#|__|  |_  |___|_| |___|_____|___|
#      |___|      
