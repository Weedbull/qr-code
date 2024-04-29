import segno
from segno import helpers
def wifi():
    print("WIFI QR_CODE")
    qr_code = segno.helpers.make_wifi(input("ssid:"), input("WIFI Password:"), security="WPA")
    qr_code.show(scale=20)
def qr_code_url():
    print("URL QR_CODE")
    qr_code = segno.make_qr(input("URL for qrcode:"))
    qr_code.show(scale=20)
    return
def email():
    print("EMAIL QR_CODE")
    qr_code = segno.helpers.make_email("EMAIL for sends letter")
    qr_code.show(scale=20)
    return

print("That do you want QR CODE setup ?:")
print("1. Wifi, \n2. Url \n3. Email")

vibor = input("Select: 1, 2, 3\n" )

if vibor == "1":
    wifi()
elif vibor == "2":
    qr_code_url()
elif vibor == "3":
    email()
print("Your request is finished")