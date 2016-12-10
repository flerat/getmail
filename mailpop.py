import poplib,sys,email,getpass

mimes=["image/jpeg","application/msword","application/pdf","application/rtf","application/zip"]

p=poplib.POP3_SSL('pop.gmail.com',995)
username=raw_input("Gmail user name : ")
p.user(username)
password=getpass.getpass("Password : ")
p.pass_(password)
response,listings,cpt=p.list()
cpt=1
for listing in listings:
	number0,size=listing.split()
	number=int(number0)
	response,lines,octets=p.top(number,0)
	message=email.message_from_string('\n'.join(lines))	# message contains core of the message with line breaks

	mailid="mail-"+str(cpt)+".txt"
	f1=open("output/"+mailid,"w")

	for header in 'From','To','Subject','Date':
		if header in message:				# find line with header info
			f1.write(header+':'+message[header]+'\n')
			if header=='Date':
				print "Fetching : "+message[header]

	response,lines,octets=p.retr(number)			# retrieve core of message(n)
	message=email.message_from_string('\n'.join(lines))
	f1.write('-'*72+'\n')
	for part in message.walk():
		if part.get_content_type()== 'text/plain':
			f1.write(part.get_payload())
			f1.write('\n'+'-'*72+'\n')
		else:
			if part.get_content_type() in mimes:
				name="output/mail-"+str(cpt)+"-"+part.get_filename()
				data=part.get_payload(decode=True)
				f=open(name,"wb")
				f.write(data)
				f.close()
	cpt=cpt+1
	

