# Data Protection Application Programming Interface (DPAPI)

DPAPI is a simple cryptology programming interface that comes bundled with operating systems in later versions starting with Windows 2000. In theory the Data Protection API can enable symmetric encryption of any kind of data; in practice, its primary use in the Windows operating system is to perform symmetric encryption of asymmetric private keys, using a user or system secret as a significant contribution of entropy.

What does DPAPI protect?
---
<dl>
  <dt>DPAPI is utilized to protect the following personal data:
  <dd>
  <dd>-Passwords and form auto-completion data in Internet Explorer, Yandex, Google "Chrome", etc.
  <dd>-E-mail account passwords in Outlook, Windows Mail, etc.
  <dd>-Shared folders and resources access password
  <dd>-Internal FTP manager account passwords
  <dd>-Outlook for S/MIME
  <dd>-Wireless network account keys and passwords
  <dd>-Private keys for Encrypting File System (EFS), SSL/TLS in Internet Information Services 
  <dd>-Network passwords in Credential Manager
  <dd>-Personal data in any application protected with the API function.
</dl>

Why is DPAPI important for cybersecurity?
---
Information stored in applications is decrypted using DPAPI. In this way, attacker passwords may be captured. For use in attack scenarios, two applications written in Python language have been developed that steal the information stored in internet browsers.
<dl>
  <dd>-Browser Stealer
  <dd>-Browser Stealer Report
  <dd>
</dl>

**Browser Stealer:**
Finds Internet browsers and applications that use those browsers. It detects files that hold personal information such as username and password, and credit card information. It decrypts these files using DPAPI. It transmits this information to the attacker via email.

![3](https://user-images.githubusercontent.com/71177413/166140991-14285215-a949-41fd-8a80-b7f15f762f57.JPG)


**Browser Stealer Report:**
Finds internet browsers and applications that use those browsers. It detects files containing personal information such as username and password, credit card information and cookies. It decrypts these files using DPAPI. It saves this information in an excel file named "Report.xls".

![8](https://user-images.githubusercontent.com/71177413/166141005-add888ec-49e3-45ef-b157-47055d9cb1d1.JPG)


