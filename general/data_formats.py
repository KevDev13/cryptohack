# Privacy enhanced Mail
print("Privacy Enhanced Mail")

from Crypto.PublicKey import RSA

keyfile = open("privacy_enhanced_mail.pem", "r")
print(RSA.importKey(keyfile.read()).d)
