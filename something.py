###############################    F U N K T I O N S   ##############################
import os
def info():
	print()
	print('Since our Operating System is very new, we can only offer you limited Information, but we will keep you Updatet!')
	print()
	n = int(input('What type of Info are you interested in? \n- - - 1 = IP Address - - -\n- - - 2 = Malware - - -\n- - - 3 = How to keep Safe in the Internet - - -\nYour Input Here : '))
	if n == 1:
		print()
		print('An IP address is nothing more than a numeric identifier. It identifies a PC, smartphone, or any other device in a network, like the')
		print('Internet. You can think of it like a snail mail address. If I know your snail mail address I know where you are, and I can send you')
		print('some letters. With an IP address, I can know (roughly) where your device is, and send you some Internet traffic.')
		print()
		print()
		print('In other words, you are identified by your IP address over the Internet. Typically, your Internet provider assigns a public IP ')
		print('address to your router in your house. When your devices in your home network want to send traffic over the Internet, they will use')
		print('that public IP address (shared among all of them).')
		print()
		print()
		print('The communication over the Internet happens with packets. Each piece of data is put in a packet, you can think of it as a letter.')
		print('On the envelope, you always write source and destination IP addresses. The Internet will take care of delivering the packet to the ')
		print('right destination. Now, as you can see, if you send traffic out you will write your IP as source IP. This is the only way the other')
		print('part can know it, and send some traffic back.')
		print()
		print('That would be all, that we know for now.')
	if n == 2:
		print()
		print("Malware, is a harmful file, like a trojan or a virus. Malware can be downloaded to your PC (usually, unless it's very high quality) and there will not be any harm, \nbut as soon as you open that file, your Computer will be infected. What this means is that Important files\nCould be deleted, your PC might even not work anymore, or other things, that can harm your Computer. \nMalware is usually found in scethy or not so trust worthy websites, messages from unknown Users or other annonymous things. \nAs soon as you get a Virus, or Malware in general, the best thing to do for you, is to first Check your Task manager (if Posible) if any background processes are happening\nthen to taskkill the file, and to uninstall it later. It really depends on the type of virus, but these Steps should be your first action. \n \nThat would be all that we know, for now.")
	if n == 3:
		print('The Internet can be a dangerous Place, people could track your Location EASILY, if you are not protected enough. \nMy personal Recomendations would be, to get a VPN. That would completely hide your location and IP Address. Other things you should Consider is ofcourse an Anti-Virus software, that seems trustworthy. This will protect you (for the most part) against Viruses, if you\nget yourself Infected. Another easily said, but hardly done thing, would be to watch out in general. You would need to Inform yourself about websites you go to,\nor check who is texting you, before you Open any links or files. \nThat would be all the Info we know, for now.')
def game(): 
	print('I will probably finnish this later')
	print('Or maybe not.')
def welcome():
	print('You are now Logged in to your Account.')
	print('Now you are granted access to all of our features! \n \n \n \n')
	print('------------------    M A I N    M E N U      ----------------------- \n')
	n = int(input('~~~~      Press 1 for Information about the Internet       ~~~~ \n \n~~~~      Press 2 for a Calculator                         ~~~~ \n \n~~~~      Press 3 to play a Game                           ~~~~ \n \n~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~\nYour Input here : '))
	if n == 1:
		info()
	if n == 2:
		os.system('calc.py')
	if n == 3:
		game()
def noacc():
	print('Welcome to "Something.py"!')
	n = int(input("Please Enter your Username, or press 1 to create an account : "))
	if n == 1:
		print('--------------- Sign Up ------------------ \n')
		a = input('What would you like this system to call you? : ')
		c = input('What should your password be? : ')
		print()
		print('- - - - - - - - - - - -') 
		print('Ok, now your Username is '+a)
		print('And your Password is '+c)
		print()
		print('- - - - - - - - - - - -') 
		print('Welcome to "Something.py"!')
	d = input("Please Enter your Username, or press 1 to create an account : ")
	if d == a:
		print('--------------- Log In ------------------- \n')
		print('Hello '+a)
		f = input("Please Enter your Password : ")
		if f == c:
			welcome()
			reff1= open("accounts.txt","a+")
			reff1.write(a+c)
noacc()
######################################################################################
