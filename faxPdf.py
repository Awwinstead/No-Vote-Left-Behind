from interfax import InterFAX
import sys

fax = interfax.deliver(fax_number="+11111111112", files=["folder/fax.pdf"])
fax = fax.reload() #sync with the api to get the latest status
while(fax.status != 0):
    if(fax.status < 0):
        #still pending
        fax = fax.reload
    elif(fax.status > 0):
        #error
        print("Error while sending fax")
        sys.exit()

if(fax.status == 0):
    #success
    print("Fax Success")

