import telebot
from newsapi import NewsApiClient
import geocoder
import pyowm
import lorem
import random
from lorem.text import TextLorem
api = NewsApiClient(api_key='4451c6f2d9444bbc8a993b2bbc3a58bb')
owm = pyowm.OWM('046bcec9a61e130bf1547ff172d00751', language="ro")  # You MUST provide a valid API key
bot = telebot.TeleBot("1096584234:AAEoSZRqtWWE5VJTfsZPTZB0NC3-1HfOf6g")
def com_pizza():
	com_pizza.h=False
	com_pizza.n=0
	com_pizza.li=[]
	com_pizza.d=False
com_pizza()

@bot.message_handler(commands=['start']) #Salutul la \start
def send_welcome(message):
	foto=open('hello.tgs', 'rb')
	bot.send_message(message.chat.id,"Salut, {0.first_name}!".format(message.from_user,bot.get_me()))
	bot.send_sticker(message.chat.id,foto)
	bot.send_message(message.chat.id,"Pentru informatii la cea ce poate JackyBot le poti primi prin cuvintul chee help")
@bot.message_handler(regexp="Salut") #Salutul 
def echo_all(message):
	foto=open('hello.tgs', 'rb')
	bot.send_message(message.chat.id,"Salut, {0.first_name}!".format(message.from_user,bot.get_me()))
	bot.send_sticker(message.chat.id,foto)
	bot.send_message(message.chat.id,"Pentru informatii la cea ce poate JackyBot le poti primi prin cuvintul chee help")

@bot.message_handler(regexp="Temperatura in")	# intrebarea temperatura de afara
def echo_temp(message):
	loc=message.text.replace("Temperatura in ", "",1)
	if loc==message.text:
		loc=message.text.replace("temperatura in ", "",1)
	observation = owm.weather_at_place(loc)
	w = observation.get_weather()
	tem=round(w.get_temperature('celsius')["temp"])
	atmo=w.get_detailed_status()
	rasp='La moment in '+loc+' sunt '+str(tem)+chr(176)+'C si este ' +atmo
	if tem>=20:
		foto1=open('cald.tgs','rb')
		bot.send_sticker(message.chat.id,foto1)
	elif tem<20 and tem>5:
		foto1=open('caldut.tgs','rb')
		bot.send_sticker(message.chat.id,foto1)	
	else:
		foto1=open('frig.webp','rb')
		bot.send_sticker(message.chat.id,foto1)		
	bot.send_message(message.chat.id,rasp)


@bot.message_handler(regexp="Temperatura")#temperatura dupa GPS
def temp_gps(message):
	g = geocoder.ip('me')
	observation = owm.weather_at_place(g.city)
	w = observation.get_weather()
	tem=round(w.get_temperature('celsius')["temp"])
	atmo=w.get_detailed_status()
	rasp='La moment in '+g.city+' sunt '+str(tem)+chr(176)+'C si este ' +atmo
	if tem>=20:
		foto1=open('cald.tgs','rb')
		bot.send_sticker(message.chat.id,foto1)
	elif tem<20 and tem>5:
		foto1=open('caldut.tgs','rb')
		bot.send_sticker(message.chat.id,foto1)	
	else:
		foto1=open('frig.webp','rb')
		bot.send_sticker(message.chat.id,foto1)		
	bot.send_message(message.chat.id,rasp)

@bot.message_handler(regexp="inca")	# alte 5 cele mai noi stiri
def echo_a(message):
	local=api.get_top_headlines(country='ro')
	n=local['totalResults']
	for i in range(5,10):
		bot.send_message(message.chat.id,'Stirea numarul '+str(i+1)+':')
		bot.send_message(message.chat.id,'Pe site-ul '+local['articles'][i]['url']+' a fost gasit articolul:\n')


@bot.message_handler(regexp="arata stiri")	# alte 5 cele mai noi stiri
def echo_aa(message):
	echo_a(message)
@bot.message_handler(regexp="alte")	# alte 5 cele mai noi stiri
def echo_aa(message):
	echo_a(message)

@bot.message_handler(regexp="Stiri")	#5 cele mai noi stiri
def echo_all(message):
	local=api.get_top_headlines(country='ro')
	n=local['totalResults']
	for i in range(5):
		bot.send_message(message.chat.id,'Stirea numarul '+str(i+1)+':')
		bot.send_message(message.chat.id,'Pe site-ul '+local['articles'][i]['url']+' a fost gasit articolul:\n')
		#bot.send_message(message.chat.id,local['articles'][0]['title']+' scris de '+local['articles'][0]['author']+'\n')
		#bot.send_message(message.chat.id,local['articles'][0]['description']+'\n\n\n')

@bot.message_handler(regexp="Help") #help
def send_welcome(message):
	ast=open('help.tgs','rb')
	bot.send_message(message.chat.id,"Salut, {0.first_name}!\nDaca doresti sa afli date meteorologice despre orice localitate scrie[Temperatura in [Locul unde doresti sa afli datele meteorologice]](fara paranteze)\nTemperatura in localitatea ta o afli doar la cuvintul chee [Temperatura]\nDaca doresti sa vezi 5 stiri ale momentului scrie[o fraza ce contine cuvantul chee stiri]\nDaca doresti sa vezi inca 5 stiri scrie[ o fraza cu cuvintul chee alte]\nLa solicitarea [alune] veti primi web-site-ul https://deceneu.netlify.com/\nDaca vei trimite un sticker vei primi un text random\nDeasemenea botul raspunde si incerca sa interactioneze cu tine pentru ati crea ziua\nMersi de atentie!!!".format(message.from_user,bot.get_me()))
	bot.send_sticker(message.chat.id,ast)
f=False
t=False
@bot.message_handler(regexp="Ce faci") #Ce faci?
def send_faci(message):
	global t
	global f
	if message.text=="ce faci" or message.text=="Ce faci" or message.text=="Ce faci?" or message.text=="ce faci?" :
		d=random.randint(1, 5)
		if d==1:
			bot.send_message(message.chat.id,'Bine 😁\nTu?')
			f=True
		elif d==2:
			bot.send_message(message.chat.id,'Superb 😜😜\nTu?')
			f=True
		elif d==3:
			bot.send_message(message.chat.id,'Azi cam greu 😔😔\nTu?')
			f=True
		elif d==4:
			bot.send_message(message.chat.id,'Momentan ma gindeam la tine, cind o sa-mi scrii 😁\nTu?')
			f=True
		elif d==5:
			bot.send_message(message.chat.id,'Calculam si verificam cit va fi 1244*ln(25)+466 😁\nTu?')
			f=True
			t=True

@bot.message_handler(regexp="cit") #rasp
def send_ras(message):
	send_faci(message)
	if t:
		bot.send_message(message.chat.id,'4470,2815261360417320066892210668\n😐😐😐')

#Raspuns user
@bot.message_handler(regexp='bine')
def send_message(message):

	send_faci(message)
	if f==True:
		bot.send_message(message.chat.id,'Ma bucur 😄😄😄')

@bot.message_handler(regexp='la fel')
def send_message(message):

	send_faci(message)
	if f==True:
		bot.send_message(message.chat.id,'Wow 😄😄😄')

@bot.message_handler(regexp='tot')
def send_message(message):

	send_faci(message)
	if f==True:
		bot.send_message(message.chat.id,'😄😄😄')

@bot.message_handler(regexp='rau')
def send_message(message):

	send_faci(message)
	if f==True:
		bot.send_message(message.chat.id,'Se mai intimpla 😔😔, vei vedea ca totul va fi bine')

@bot.message_handler(regexp='stau')
def send_message(message):

	send_faci(message)
	if f==True:
		bot.send_message(message.chat.id,'Eu tot 👌')

@bot.message_handler(regexp='nimic')
def send_message(message):

	send_faci(message)
	if f==True:
		bot.send_message(message.chat.id,'Nu poate fi 😱😱😱')
#pina aici


@bot.message_handler(regexp="Alune")	#Srl Deceneu
def echo_all(message):
	foro=open('dece.jpg', 'rb')
	ast=open('astea.tgs','rb')
	bot.send_photo(message.chat.id,foro)
	bot.send_message(message.chat.id,"https://deceneu.netlify.com/")
	bot.send_message(message.chat.id,"Hei,stiai ca, alunele de pădure pot fi consumate sub diverse forme: crude (oferă cele mai multe beneficii) sau prăjite (au un gust pe care foarte mulți oameni îl găsesc mai plăcut), în salate de legume (grăsimile sănătoase prezente în alune facilitează absorbția deverșilor nutrienți găsiți în legume) sau în salate de fructe uscate, nuci și semințe, în înghețată...")
	bot.send_message(message.chat.id,"Daca esti interesat, suna-ne!!\nComanda online https://deceneu.netlify.com/contactare.html \nNoi asteptam!!")
	bot.send_sticker(message.chat.id,ast)
	bot.send_contact(message.chat.id,phone_number='+37378173074',first_name='SRL Deceneu-Alune de padure')

@bot.message_handler(content_types="sticker")	#Oricare alt raspunt
def echo_all(message):
	t = lorem.text()
	bot.send_message(message.chat.id,t)

@bot.message_handler(regexp="Mersi")#Rasp la Mersi
def ans_mersi(message):
	bot.send_message(message.chat.id,'Cu placere 😀😀😀')

@bot.message_handler(regexp="Pk")#la revedere
def ans_mersi(message):
	bot.send_message(message.chat.id,'Ne mai vedem 😉😉')
@bot.message_handler(regexp="Pa")#la revedere
def ans_mersi(message):
	bot.send_message(message.chat.id,'Pe curind 😉😉')
@bot.message_handler(regexp="La revedere")#la revedere
def ans_mersi(message):
	bot.send_message(message.chat.id,'La revedere 😉😉')
@bot.message_handler(regexp="Noapte buna")#la revedere
def ans_mersi(message):
	bot.send_message(message.chat.id,'Noapte buna ⭐️⭐️🌙🌙😉😉')

#***********************************************************



@bot.message_handler(regexp="Pizza")#Comanda pizza
def com_pizza4(message):
	bot.reply_to(message,"Vrei Pizza???🍕🍕🍕🍕")
	bot.send_message(message.chat.id,'Pot sa-ti recomand...')
	bot.send_message(message.chat.id,'https://dodopizza.ro/bucuresti')
	bot.send_message(message.chat.id,'Sau hai sa incercam sa comanzi pe botul nostru 😀😀')	
	bot.send_message(message.chat.id,'Comanzi pe Bot?')
	bot.send_message(message.chat.id,'Raspunde cu Da! sau Nu!')
	com_pizza.h=True

@bot.message_handler(regexp="nu!")# NU Comanda pizza pe bot
def com_pizza_1(message):
	if com_pizza.h :
		bot.send_message(message.chat.id,'Atunci poti accesa web-site-ul')
		bot.send_message(message.chat.id,'https://dodopizza.ro/bucuresti')
		com_pizza.d=False
	else :
		bot.send_message(message.chat.id,'Ce NU??')

@bot.message_handler(regexp="da!")#Comanda pizza pe bot
def com_pizza_1(message):
	if com_pizza.h :
		bot.send_message(message.chat.id,'Hai sa incepem, te ascult')
		com_pizza.d=True
	else :
		bot.send_message(message.chat.id,'Ce DA??')

@bot.message_handler(regexp="Gata")#Gata lista
def com_pizza_3(message):
	if com_pizza.d:
		bot.send_message(message.chat.id,"Comanda ta este:")
		for i in range(com_pizza.n):
			bot.send_message(message.chat.id,com_pizza.li[i])	
	com_pizza.d=False	
	com_pizza.h=False
	d=random.randint(10, 120)
	bot.send_message(message.chat.id,"Comanda va fi gata in "+str(d)+" min")
	bot.send_message(message.chat.id,"Te vom telefona cind vom fi gata 😉😉😉")	


@bot.message_handler()#Lista
def com_pizza_2(message):
	if com_pizza.d:
		com_pizza.n=com_pizza.n+1
		com_pizza.li.append(message.text)
		bot.send_message(message.chat.id,str(com_pizza.n)+"."+message.text)
	else:
		bot.send_message(message.chat.id,'Scuze, dar nu stiu ce sa-ti raspund 😔😔😔.\nInca incerc sa ma perfectionez.')
		
#*****************************************************************

bot.polling(none_stop=True)

