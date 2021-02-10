import logging
from logging import Logger, Handler, Filter
from logging.config import fileConfig, dictConfig

url = "http://example.com" # Sensitive
url = "ftp://anonymous@example.com" # Sensitive
url = "telnet://anonymous@example.com" # Sensitive

import telnetlib
cnx = telnetlib.Telnet("towel.blinkenlights.nl") # Sensitive

import ftplib
cnx = ftplib.FTP("ftp.example.com") # Sensitive

import smtplib
smtp = smtplib.SMTP("smtp.example.com", port=587) # Sensitive

class MyClass:
    def __add__(self, other):
        raise NotImplementedError()  # Noncompliant
    def __radd__(self, other):
        raise NotImplementedError()  # Noncompliant

class MyOtherClass:
    def __add__(self, other):
        return 42
    def __radd__(self, other):
        return 42

MyClass() + MyOtherClass()  # This will raise NotImplementedError

url = "http://example.com" # Sensitive
url = "ftp://anonymous@example.com" # Sensitive
url = "telnet://anonymous@example.com" # Sensitive




