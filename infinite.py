# Python3 code to demonstrate 
# generating random strings 
# using secrets.choice() 
import secrets 
import string 

# initializing size of string 
N = 22

# using random.choices() 
# generating random strings 
res = ''.join(secrets.choice(string.ascii_uppercase + string.ascii_lowercase + "-"+ "_"+ string.digits ) 
												for i in range(N)) 


print("https://www.acko.tech/amazon-mobile/download-policy/" + str(res)) 

