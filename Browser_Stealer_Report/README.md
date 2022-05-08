
# Browser Stealer Report
Finds internet browsers and applications that use those browsers. It detects files containing personal information such as username and password, credit card information and cookies. It decrypts these files using DPAPI. It saves this information in an excel file named "Report.xls".

**1) The algorithm used by the program for saved passwords is shown in the graphic below.**
![key1](https://user-images.githubusercontent.com/71177413/166139625-fd15d6ea-6355-4a80-ae83-15b6437b54e5.JPG)

**2) The algorithm used by the program for saved credit cards is shown in the graphic below.**
![key2](https://user-images.githubusercontent.com/71177413/166139633-a23d31a5-d098-440d-ba6b-ae36995777b7.JPG)

**3) The algorithm used by the program for cookies is shown in the graphic below.**
![key](https://user-images.githubusercontent.com/71177413/166139637-b07e629a-f7b4-41e4-b8d1-5c4f893e0e83.JPG)


Supported Browsers
---
This python program gets all the saved passwords, credit cards and cookies from chromium based browsers supports chromium 80 and above!
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
  <dt> Browser Stealer Report
  <dd>
  <dd> Browser_Stealer_Report.rar --> zip password: "BroWSerSteaLErRePOrt2022"
  <dd> Link = https://drive.google.com/file/d/13ZrjFqpua_BijbaE52RQ2gfCPX65Mubh/view?usp=sharing
</dl>


Requirements
---
Required libraries:  pywin32, pycryptodome, xlwt, pyinstaller

```
pip install pywin32
pip install pycryptodome
pip install xlwt
pip install pyinstaller
```


"pyinstaller" will be used to make the code one piece executable


Compilation
---

```
pyinstaller --onefile --icon=Browser_Stealer_Report.ico Browser_Stealer_Report.py
```

Some Screenshot of the Working of the Program
---

**Screenshot [1] (Screenshot taken while the program is running)**
![8](https://user-images.githubusercontent.com/71177413/166138985-cb48fcaf-d89c-4fa2-9f46-54609f54e5b0.JPG)


**Screenshot [2] (The sheet showing the browsers on the computer in the report produced by the program)**
![9](https://user-images.githubusercontent.com/71177413/166139105-d420cdad-12be-4426-84ea-ff3021501be0.JPG)


**Screenshot [3] (The sheet showing the saved passwords in the report produced by the program)**
![10](https://user-images.githubusercontent.com/71177413/166139197-93fe17b8-eed2-473a-8f51-d2ce4d8d18e4.JPG)


**Screenshot [4] (The sheet showing the saved credit cards in the report produced by the program)**
![11](https://user-images.githubusercontent.com/71177413/166139251-5e006a71-d077-4de5-a4af-d29a0a2a0c19.JPG)


**Screenshot [5] (The sheet showing the (current) cookies saved in the report produced by the program)**
![12](https://user-images.githubusercontent.com/71177413/166139280-01179ffd-fb96-4db8-bfc2-f72532f8c22c.JPG)


**Screenshot [6] (The sheet showing the (expired) cookies saved in the report produced by the program)**
![13](https://user-images.githubusercontent.com/71177413/166139310-fe79c485-25ee-4fbc-b626-2fcbc4d222a6.JPG)


Legal Warning
---
Run your tests on virtual machines. The responsibility for illegal use belongs to the user. Shared for educational purposes.
