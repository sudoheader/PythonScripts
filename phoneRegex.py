phoneNumberOldWay = re.compile(r'''
\d\d\d 	# area code (without parens)
(\(\d\d\d\) )	# -or- area code with parens and no dash
\d\d\d 		# first 3 digits
-		# second dash
\d\d\d\		# last 4 digits
\sx\d{2,4}	# extension, like x1234''', re.IGNORECASE | re.DOTALL | re.VERBOSE)

newPhoneNumber = re.compile(r'''
\d\d\d 	# area code (without parens)
(\(\d\d\d\) )	# -or- area code with parens and no dash
\d\d\d 		# first 3 digits
-		# second dash
\d\d\d\		# last 4 digits
\sx\d{2,4}	# extension, like x1234''', re.VERBOSE)

# old-fashioned | bit-wise or operator to pass arguments to compile (only used for that function.
# just pass VERBOSE instead
