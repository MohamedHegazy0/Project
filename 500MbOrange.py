import requests
import hashlib
import requests
import requests,os,sys,time,pyfiglet
import webbrowser
Z = '\033[1;31m' #احمر
X = '\033[1;33m' #اصفر
F = '\033[2;32m' #اخضر
C = "\033[1;97m" #ابيض
B = '\033[2;36m'#سمائي
Y = '\033[1;34m' #ازرق فاتح.
C = "\033[1;97m" #ابيض
E = '\033[1;31m'
B = '\033[2;36m'
G = '\033[1;32m'
S = '\033[1;33m'
Lo=pyfiglet.figlet_format('Adam and Ramez ')
print(F+Lo)
Jo=pyfiglet.figlet_format('500 Orange')
print(F+Jo)
webbrowser.open('https://t.me/T_e_a_m_Lasheen')
print(B+"by code: Adam&Ramez")
print("")
num=input(B+' Enter a Number : '+Y)
print()
pas=input(B+'Enter a Password : '+Y)
print("")
url = 'https://services.orange.eg/SignIn.svc/SignInUser'
header ={
"net-msg-id": "61f91ede006159d16840827295301013",
"x-microservice-name": "APMS",
"Content-Type": "application/json; charset=UTF-8",
"Content-Length": "166",
"Host": "services.orange.eg",
"Connection": "Keep-Alive",
"Accept-Encoding": "gzip",
"User-Agent": "okhttp/3.14.9",
}
data = '{"appVersion":"7.2.0","channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"dialNumber":"%s","isAndroid":true,"password":"%s"}' % (num,pas)
r=requests.post(url,headers=header,data=data).json()
#print(r)
userid=r["SignInUserResult"]["UserData"]["UserID"]
print("Wait..🔥🔥")
urlo = "https://services.orange.eg/GetToken.svc/GenerateToken"
hdo = {"Content-type":"application/json", 
  "Content-Length":"78", 
  "Host":"services.orange.eg"
   , "Connection":"Keep-Alive" ,
    "User-Agent":"okhttp/3.12.1"}
datao = '{"appVersion":"2.9.8","channel":{"ChannelName":"MobinilAndMe","Password":"ig3yh*mk5l42@oj7QAR8yF"},"dialNumber":"%s","isAndroid":true,"password":"%s"}' %(num,pas)
ctv = requests.post(urlo,headers=hdo,data = datao).json()["GenerateTokenResult"]["Token"]
key = ',{.c][o^uecnlkijh*.iomv:QzCFRcd;drof/zx}w;ls.e85T^#ASwa?=(lk'
htv=(str(hashlib.sha256((ctv+key).encode('utf-8')).hexdigest()).upper())
url2="https://services.orange.eg/APIs/Promotions/api/CAF/Redeem"
data2='{"Language":"ar","OSVersion":"Android7.0","PromoCode":"رمضان كريم","dial":"%s","password":"%s","Channelname":"MobinilAndMe","ChannelPassword":"ig3yh*mk5l42@oj7QAR8yF"}' %(num,pas)
header2={
"_ctv": ctv,
"_htv": htv,
"UserId": userid,
"Content-Type": "application/json; charset=UTF-8",
"Content-Length": "142",
"Host": "services.orange.eg",
"Connection": "Keep-Alive",
"User-Agent": "okhttp/3.14.9",
}
da=data2.encode('utf-8')
response = requests.post(url2, headers=header2, data=da).json()

if 'ErrorDescription' in response:
    if response['ErrorDescription'] == 'Success':
        print(F+"تم إضافة 524 ميجا بنجاح")
    elif response['ErrorDescription'] == 'User is redeemed before':
        print(X+"العرض غير متاح لك حاليا")
    else:
        print(Z+"حدث خطأ، حاول مرة أخرى")
else:
    print(Z+"حدث خطأ غير متوقع، حاول مرة أخرى")