import poplib,sys,email

mimes=["image/jpeg","application/msword"]

p=poplib.POP3_SSL('pop.gmail.com',995)
p.user('fmantis77')
p.pass_('mantis777')
response,listings,cpt=p.list()
for listing in listings:
	number0,size=listing.split()
	number=int(number0)
	response,lines,octets=p.top(number,0)
	message=email.message_from_string('\n'.join(lines))	# message contains core of the message with line breaks
	for header in 'From','To','Subject','Date':
		if header in message:				# find line with header info
			print header+':'+message[header]	# try with file with n lines
	print
	response,lines,octets=p.retr(number)			# retrieve core of message(n)
	message=email.message_from_string('\n'.join(lines))
	print '-'*72
	for part in message.walk():
		print 'content type : ',part.get_content_type()
		if part.get_content_type()== 'text/plain':
			print part.get_payload()
			print '-'*72
		else:
			if part.get_content_type() in mimes:
				name=part.get_filename()
				data=part.get_payload(decode=True)
				f=open(name,"wb")
				f.write(data)
				f.close()
	
#		if part.get_content_type() == 'application/msword':
#			name = part.get_param('name') or 'MyDoc.doc'
#			f = open(name, 'wb')
#			f.write(part.get_payload(None, True)) # You need None as the first param because part.is_multipart() is False
#        		f.close(


#            if part.get_content_type() in allowed_mimetypes:
#                name = part.get_filename()
#                data = part.get_payload(decode=True)
#                f = file(name,'wb')
#                f.write(data)
#                f.close()



#def WriteAttachment(msg):
#    for part in msg.walk():
#        if part.get_type() in mimes:
#            name = part.get_filename()
#            data = part.get_payload(decode=True)
#            f = file(name,'wb')
#            f.write(data)
#            f.close()

