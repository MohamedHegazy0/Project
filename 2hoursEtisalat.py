import os
try:
 import requests
 import base64
 import xml.etree.ElementTree as ET
 from colorama import Fore
 from pyfiglet import Figlet
 import webbrowser
	
except:
 os.system('pip install requests')
 os.system('pip install base64')
 os.system('pip install pyfiglet')
 os.system('pip install colorama')


G = Fore.GREEN
R = Fore.RED

def flag():
    ramadan_kareem = "❤️‍🔥2 HOURS ETISALAT❤️‍🔥"
    titanic_text = "Adam and Ramez"

    f = Figlet(font='small',width=50)


    print("\033[1;33m" + f.renderText(ramadan_kareem) + "\033[0m")


    print("\033[1;31m" + "-" * 50 + "\033[0m")

    print("\033[1;32m" + f.renderText(titanic_text) + "\033[0m")
    telegram_channel_link = "https://t.me/T_e_a_m_Lasheen"
    


    print("\033[1;31m" + "-"*50 + "\033[0m")


    text1 = "BY:Adam&Ramez"
    text2 = "Our channel : https://t.me/T_e_a_m_Lasheen"
    text3 = "❤️‍🔥Team Lasheen FOR FREE INTERNET❤️‍🔥"

    print("\033[1;33m" + text1.center(50) + "\033[0m")
    print("\033[1;31m" + "-" * 50 + "\033[0m")
    print("\033[1;33m" + text2.center(50) + "\033[0m")
    print("\033[1;31m" + "-" * 50 + "\033[0m")
    print("\033[1;33m" + text3.center(50) + "\033[0m")


    print("\033[1;31m" + "-" * 50 + "\033[0m")


    number = input("\033[1;33mEnter Your Number : \033[0m")

    print("\033[1;33m" + "-"*50 + "\033[0m")


    password = input("\033[1;33mENTER Your Password : \033[0m")

    print("\033[1;33m" + "-"*50 + "\033[0m")
    
    email = input("\033[1;33mENTER Your Email : \033[0m")

    print("\033[1;33m" + "-"*50 + "\033[0m")
    
    if "011" in number:
        num = number[+1:]
    else:
        num = number
    
    code = email + ":" + password
    ccode = code.encode("ascii")
    base64_bytes = base64.b64encode(ccode)
    auth = base64_bytes.decode("ascii")
    xauth = "Basic" + " " + auth

    urllog = "https://mab.etisalat.com.eg:11003/Saytar/rest/authentication/loginWithPlan"

    headerslog = {
        "applicationVersion": "2",
        "applicationName": "MAB",
        "Accept": "text/xml",
        "Authorization": xauth,
        "APP-BuildNumber": "964",
        "APP-Version": "27.0.0",
        "OS-Type": "Android",
        "OS-Version": "12",
        "APP-STORE": "GOOGLE",
        "Is-Corporate": "false",
        "Content-Type": "text/xml; charset=UTF-8",
        "Content-Length": "1375",
        "Host": "mab.etisalat.com.eg:11003",
        "Connection": "Keep-Alive",
        "Accept-Encoding": "gzip",
        "User-Agent": "okhttp/5.0.0-alpha.11",
        "ADRUM_1": "isMobile:true",
        "ADRUM": "isAjax:true"
    }

    datalog = "<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><loginRequest><deviceId></deviceId><firstLoginAttempt>true</firstLoginAttempt><modelType></modelType><osVersion></osVersion><platform>Android</platform><udid></udid></loginRequest>"
    log = requests.post(urllog, headers=headerslog, data=datalog)

    if "true" in log.text:
        st = log.headers["Set-Cookie"]
        ck = st.split(";")[0] 
        br = log.headers["auth"]

        url = "https://mab.etisalat.com.eg:11003/Saytar/rest/zero11/offersV3?req=<dialAndLanguageRequest><subscriberNumber>%s</subscriberNumber><language>1</language></dialAndLanguageRequest>"%(num)




        headers = {
        'applicationVersion': "2",
        'Content-Type': "text/xml",
        'applicationName': "MAB",
        'Accept': "text/xml",
        'Language': "ar",
        'APP-BuildNumber': "10459",
        'APP-Version': "29.9.0",
        'OS-Type': "Android",
        'OS-Version': "11",
        'APP-STORE': "GOOGLE",
        'auth': "Bearer " + br,
        'Host': "mab.etisalat.com.eg:11003",
        'Is-Corporate': "false",
        'Connection': "Keep-Alive",
        'Accept-Encoding': "gzip",
        'User-Agent': "okhttp/5.0.0-alpha.11",
        'Cookie': ck
    }


        response = requests.get(url, headers=headers)

        if response.status_code == 200:
            root = ET.fromstring(response.text)
            offer_id = None
            for category in root.findall('.//mabCategory'):
                for product in category.findall('.//mabProduct'):
                    for parameter in product.findall('.//fulfilmentParameter'):
                        if parameter.find('name').text == 'Offer_ID':
                            offer_id = parameter.find('value').text
                            break
                    if offer_id:
                        break
                    
                if offer_id:
                    break
        else:
            print(R+"هذا العرض غير متاح حاليا ليك حاول بكره تاني")
    else:
        print("الرقم او كلمة السر غلط")

    if "true" in log.text:
        st = log.headers["Set-Cookie"]
        ck = st.split(";")[0] 
        br = log.headers["auth"]

        urlsub = "https://mab.etisalat.com.eg:11003/Saytar/rest/zero11/submitOrder"

        headerssub = {
            "applicationVersion": "2",
            "applicationName": "MAB",
            "Accept": "text/xml",
            "Cookie": ck,
            "Language": "ar",
            "APP-BuildNumber": "964",
            "APP-Version": "27.0.0",
            "OS-Type": "Android",
            "OS-Version": "12",
            "APP-STORE": "GOOGLE",
            "auth": "Bearer " + br + "",
            "Is-Corporate": "false",
            "Content-Type": "text/xml; charset=UTF-8",
            "Content-Length": "1375",
            "Host": "mab.etisalat.com.eg:11003",
            "Connection": "Keep-Alive",
            "User-Agent": "okhttp/5.0.0-alpha.11"
        }

        datasub = "<?xml version='1.0' encoding='UTF-8' standalone='yes' ?><submitOrderRequest><mabOperation></mabOperation><msisdn>%s</msisdn><operation>ACTIVATE</operation><parameters><parameter><name>GIFT_FULLFILMENT_PARAMETERS</name><value>Offer_ID:%s;ACTIVATE:True;isRTIM:Y</value></parameter></parameters><productName>FAN_ZONE_HOURLY_BUNDLE</productName></submitOrderRequest>" % (num, offer_id)
        
        subs = requests.post(urlsub, headers=headerssub, data=datasub).text


        if "true" in subs:
            text4 =G+ "❤️‍🔥معاك دلوقتي ساعتين سوشيال❤️‍🔥"
            print("\033[1;31m" + text4.center(50) + "\033[0m")
        else:
            print(R + "Check Your Data")
    else:
        print(R + "Check Your Input")


flag()