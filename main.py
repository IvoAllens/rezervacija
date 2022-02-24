#instalē un importē nepieciešamās bibliotēkas
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from tkcalendar import Calendar, DateEntry
from datetime import date
import datetime
from datetime import timedelta

#mainīgie ar cenām
bro=7
cena2=40
cenaVIP=60
cena3=55
cena2telpu=70
cena4=70
cena_dz=85

#izveido nepieciešamos sarakstus
numuri=["divvietīgs(40€)","divvietīgs - VIP(60€)","trīsvietīgs(55€)","trīsvietīgs - divu telpu(70€)","četrvietīgs(70€)","četrvietīgs - pet(85€)"]
skaits=["1","2","3","4","5"]
iespejas=["Jā","Nē"]

#atrod šodienas datumu
sodiena=str(datetime.datetime.today()).split()[0]

#atver teksta failus, katram numura lielumam , kurā tiek saglabāti aizņemtie datumi
f=open("divvietigs.txt","a")
f.close()
f=open("VIP.txt","a")
f.close()
f=open("trisvietigs.txt","a")
f.close()
f=open("trisvietigs2telpu.txt", "a")
f.close()
f=open("cetrvietigs.txt","a")
f.close()
f=open("dzivnieku.txt","a")
f.close()

#izveido sākuma ekrānu
window=Tk()
window.title("Viesnīca - MARIVO")
window.geometry("550x300")
window.config(background="#89cff0")

#izveido funkciju, kas veiks savu darbību kad būs nospiests rezervēt
def rezervet():
  #paņem un saglabā ievadītās vērtības
  vards1=vards_kaste.get()
  uzvards1=uzvards_kaste.get()
  tel1=tel_kaste.get()
  epasts1=epasts_kaste.get()
  numurs1=numurs_kaste.get()
  naktis1=naktis_kaste.get()
  kal1=kalendars.get()
  kalendars1=kal1.replace("/","-")
  brokastis1 = brokastis_kaste.get()
  kom1=kom_kaste.get()

  #sadala iegūto laika stringu pa dienām, mēnešiem, gadiem
  ie = kal1.split("/")
  dd = int(ie[2])
  mm = int(ie[1])
  yy = int(ie[0])

  #visu iegūto informāciju par klientu saglabā teksta failā
  def klients():
    f=open("klients.txt","a")
    f.write("Nummura lielums: " + numurs1 + "\n")
    f.write("Ar brokastīm? " + brokastis1 + "\n")
    f.write("Klienta vārds: " + vards1 + "\n")
    f.write("Klienta uzvārds: " + uzvards1 + "\n")
    f.write("Klienta telefona nummurs: " + tel1 + "\n")
    f.write("Klienta e-pasts: " + epasts1 + "\n")
    ierasanas_k = datetime.date(yy, mm, dd) 
    paliek_k = ierasanas_k + timedelta(days = int(naktis1)) 
    f.write("Klienta apmešanās laiks: no "+kalendars1 +" līdz "+ str(paliek_k) +"\n")
    f.write("Apmaksājamā summa: "+ str(summa) + "€"+"\n")
    f.write("Papildus komentāri: " + kom1 + "\n\n")
    f.close()

  #izdara pārbaudi vai visi lauciņi tiek aizpildīti
  if vards1=="" or uzvards1=="" or tel1=="" or epasts1=="" or numurs1=="" or kal1=="" or naktis1=="" or brokastis1=="":
    print("Trūkst informācijas!")
  else:
    #pārbauda vai ievadītais datums nav senāks par šodienu
    if kalendars1<sodiena:
      print("Ievadītais datums nav derīgs, tas jau ir pagājis!")
      print("Lūdzu ievadiet datumu sākot ar " + sodiena)
    else:
      if numurs1=="divvietīgs(40€)":
        #izveido sarakstu, ar datumiem, kurus vēlas rezervēt
        grib2=[]
        for i in range (int(naktis1)+1):
          ierasanas = datetime.date(yy, mm, dd) 
          paliek = ierasanas + timedelta(days = i) 
          grib2.append(str(paliek))
          i=+1
        #izveido sarakstu ar aizņemtajiem numuriem, ņemot no teksta faila 
        aiznemts2=[]
        for f in open("divvietigs.txt", "r").readlines(): 
          aiznemts2.append(f.strip())
        #pārbauda vai vēlamie datumi ir aizņemti vai nē
        for i in grib2:
          if i in aiznemts2:
            print("Šie datumi nav pieejami!")
            aiznemts2.sort()
            print('\n'.join(map(str, aiznemts2)))
            print("Lūdzu izvēlieties citu sev vēlamo datumu!")
            break
          else:
            print("Šie datumi ir pieejami!")
            #tā kā numurs ir pieejams vēlamajos datumos, tad šie datumi tiek pievienoti teksta failam
            for i in range (int(naktis1)+1):
              ierasanas = datetime.date(yy, mm, dd) 
              paliek = ierasanas + timedelta(days = i) 
              f=open("divvietigs.txt","a")
              f.write(str(paliek) +"\n")
              i=+1
            #pārbauda vai lietotājs vēlas brokastis vai nē un aprēķina apmaksājamo summu
            if brokastis1=="Jā":
              summa=(cena2+(2*bro))*int(naktis1)
              print("Apmaksājamā summa: " + str(summa) + "€")
            else:
              summa=cena2*int(naktis1)
              print("Apmaksājamā summa: " + str(summa) + "€")
            #izsauc funkciju, lai tiktu saglabāta visa klienta aizpildītā informācija
            klients()
            print("Viesnīca ir rezervēta!")
            break
      
      elif numurs1=="divvietīgs - VIP(60€)":
        #izveido sarakstu, ar datumiem, kurus vēlas rezervēt
        gribVIP=[]
        for i in range (int(naktis1)+1):
          ierasanas = datetime.date(yy, mm, dd) 
          paliek = ierasanas + timedelta(days = i) 
          gribVIP.append(str(paliek))
          i=+1
        #izveido sarakstu ar aizņemtajiem numuriem, ņemot no teksta faila 
        aiznemtsVIP=[]
        for f in open("VIP.txt", "r").readlines(): 
          aiznemtsVIP.append(f.strip())
        #pārbauda vai vēlamie datumi ir aizņemti vai nē
        for i in gribVIP:
          if i in aiznemtsVIP:
            print("Šie datumi nav pieejami!")
            aiznemtsVIP.sort()
            print('\n'.join(map(str, aiznemtsVIP)))
            print("Lūdzu izvēlieties citu sev vēlamo datumu!")
            break
          else:
            print("Šie datumi ir pieejami!")
            #tā kā numurs ir pieejams vēlamajos datumos, tad šie datumi tiek pievienoti teksta failam
            for i in range (int(naktis1)+1):
              ierasanas = datetime.date(yy, mm, dd) 
              paliek = ierasanas + timedelta(days = i) 
              f=open("VIP.txt","a")
              f.write(str(paliek) +"\n")
              i=+1
            #pārbauda vai lietotājs vēlas brokastis vai nē un aprēķina apmaksājamo summu
            if brokastis1=="Jā":
              summa=(cenaVIP+(2*bro))*int(naktis1)
              print("Apmaksājamā summa: " + str(summa) + "€")
            else:
              summa=cenaVIP*int(naktis1)
              print("Apmaksājamā summa: " + str(summa) + "€")
            #izsauc funkciju, lai tiktu saglabāta visa klienta aizpildītā informācija
            klients()
            print("Viesnīca ir rezervēta!")
            break
      
      elif numurs1=="trīsvietīgs(55€)":
        #izveido sarakstu, ar datumiem, kurus vēlas rezervēt
        grib3=[]
        for i in range (int(naktis1)+1):
          ierasanas = datetime.date(yy, mm, dd) 
          paliek = ierasanas + timedelta(days = i) 
          grib3.append(str(paliek))
          i=+1
        #izveido sarakstu ar aizņemtajiem numuriem, ņemot no teksta faila
        aiznemts3=[] 
        for f in open("trisvietigs.txt", "r").readlines(): 
          aiznemts3.append(f.strip())
        #pārbauda vai vēlamie datumi ir aizņemti vai nē
        for i in grib3:
          if i in aiznemts3:
            print("Šie datumi nav pieejami!")
            aiznemts3.sort()
            print('\n'.join(map(str, aiznemts3)))
            print("Lūdzu izvēlieties citu sev vēlamo datumu!")
            break
          else:
            print("Šie datumi ir pieejami!")
            #tā kā numurs ir pieejams vēlamajos datumos, tad šie datumi tiek pievienoti teksta failam
            for i in range (int(naktis1)+1):
              ierasanas = datetime.date(yy, mm, dd) 
              paliek = ierasanas + timedelta(days = i) 
              f=open("trisvietigs.txt","a")
              f.write(str(paliek) +"\n")
              i=+1
            #pārbauda vai lietotājs vēlas brokastis vai nē un aprēķina apmaksājamo summu
            if brokastis1=="Jā":
              summa=(cena3+(3*bro))*int(naktis1)
              print("Apmaksājamā summa: " + str(summa) + "€")
            else:
              summa=cena3*int(naktis1)
              print("Apmaksājamā summa: " + str(summa) + "€")
            #izsauc funkciju, lai tiktu saglabāta visa klienta aizpildītā informācija
            klients()
            print("Viesnīca ir rezervēta!")
            break
      elif numurs1=="trīsvietīgs - divu telpu(70€)":
        #izveido sarakstu, ar datumiem, kurus vēlas rezervēt
        grib2telpu=[]
        for i in range (int(naktis1)+1):
          ierasanas = datetime.date(yy, mm, dd) 
          paliek = ierasanas + timedelta(days = i) 
          grib2telpu.append(str(paliek))
          i=+1
        #izveido sarakstu ar aizņemtajiem numuriem, ņemot no teksta faila 
        aiznemts2telpu=[]
        for f in open("trisvietigs2telpu.txt", "r").readlines(): 
          aiznemts2telpu.append(f.strip())
        #pārbauda vai vēlamie datumi ir aizņemti vai nē
        for i in grib2telpu:
          if i in aiznemts2telpu:
            print("Šie datumi nav pieejami!")
            aiznemts2telpu.sort()
            print('\n'.join(map(str, aiznemts2telpu)))
            print("Lūdzu izvēlieties citu sev vēlamo datumu!")
            break
          else:
            print("Šie datumi ir pieejami!")
            #tā kā numurs ir pieejams vēlamajos datumos, tad šie datumi tiek pievienoti teksta failam
            for i in range (int(naktis1)+1):
              ierasanas = datetime.date(yy, mm, dd) 
              paliek = ierasanas + timedelta(days = i) 
              f=open("trisvietigs2telpu.txt","a")
              f.write(str(paliek) +"\n")
              i=+1
            #pārbauda vai lietotājs vēlas brokastis vai nē un aprēķina apmaksājamo summu
            if brokastis1=="Jā":
              summa=(cena2telpu+(3*bro))*int(naktis1)
              print("Apmaksājamā summa: " + str(summa) + "€")
            else:
              summa=cena2telpu*int(naktis1)
              print("Apmaksājamā summa: " + str(summa) + "€")
            #izsauc funkciju, lai tiktu saglabāta visa klienta aizpildītā informācija
            klients()
            print("Viesnīca ir rezervēta!")
            break 

      elif numurs1=="četrvietīgs(70€)":
        #izveido sarakstu, ar datumiem, kurus vēlas rezervēt
        grib4=[]
        for i in range (int(naktis1)+1):
          ierasanas = datetime.date(yy, mm, dd) 
          paliek = ierasanas + timedelta(days = i) 
          grib4.append(str(paliek))
          i=+1
        #izveido sarakstu ar aizņemtajiem numuriem, ņemot no teksta faila
        aiznemts4=[] 
        for f in open("cetrvietigs.txt", "r").readlines(): 
          aiznemts4.append(f.strip())
        #pārbauda vai vēlamie datumi ir aizņemti vai nē
        for i in grib4:
          if i in aiznemts4:
            print("Šie datumi nav pieejami!")
            aiznemts4.sort()
            print('\n'.join(map(str, aiznemts4)))
            print("Lūdzu izvēlieties citu sev vēlamo datumu!")
            break
          else:
            print("Šie datumi ir pieejami!")
            #tā kā numurs ir pieejams vēlamajos datumos, tad šie datumi tiek pievienoti teksta failam
            for i in range (int(naktis1)+1):
              ierasanas = datetime.date(yy, mm, dd) 
              paliek = ierasanas + timedelta(days = i) 
              f=open("cetrvietigs.txt","a")
              f.write(str(paliek) +"\n")
              i=+1
            #pārbauda vai lietotājs vēlas brokastis vai nē un aprēķina apmaksājamo summu
            if brokastis1=="Jā":
              summa=(cena4+(4*bro))*int(naktis1)
              print("Apmaksājamā summa: " + str(summa) + "€")
            else:
              summa=cena4*int(naktis1)
              print("Apmaksājamā summa: " + str(summa) + "€")
            #izsauc funkciju, lai tiktu saglabāta visa klienta aizpildītā informācija
            klients()
            print("Viesnīca ir rezervēta!")
            break

      else:
        #izveido sarakstu, ar datumiem, kurus vēlas rezervēt
        grib_dz=[]
        for i in range (int(naktis1)+1):
          ierasanas = datetime.date(yy, mm, dd) 
          paliek = ierasanas + timedelta(days = i) 
          grib_dz.append(str(paliek))
          i=+1
        #izveido sarakstu ar aizņemtajiem numuriem, ņemot no teksta faila
        aiznemts_dz=[] 
        for f in open("dzivnieku.txt", "r").readlines(): 
          aiznemts_dz.append(f.strip())
        #pārbauda vai vēlamie datumi ir aizņemti vai nē
        for i in grib_dz:
          if i in aiznemts_dz:
            print("Šie datumi nav pieejami!")
            aiznemts_dz.sort()
            print('\n'.join(map(str, aiznemts_dz)))
            print("Lūdzu izvēlieties citu sev vēlamo datumu!")
            break
          else:
            print("Šie datumi ir pieejami!")
            #tā kā numurs ir pieejams vēlamajos datumos, tad šie datumi tiek pievienoti teksta failam
            for i in range (int(naktis1)+1):
              ierasanas = datetime.date(yy, mm, dd) 
              paliek = ierasanas + timedelta(days = i) 
              f=open("dzivnieku.txt","a")
              f.write(str(paliek) +"\n")
              i=+1
            #pārbauda vai lietotājs vēlas brokastis vai nē un aprēķina apmaksājamo summu
            if brokastis1=="Jā":
              summa=(cena_dz+(4*bro))*int(naktis1)
              print("Apmaksājamā summa: " + str(summa) + "€")
            else:
              summa=cena_dz*int(naktis1)
              print("Apmaksājamā summa: " + str(summa) + "€")
            #izsauc funkciju, lai tiktu saglabāta visa klienta aizpildītā informācija
            klients()
            print("Viesnīca ir rezervēta!")
            break


#numura lieluma izvēlēšanās ar izvēles variantiem
liel=Label(window,text="Izvēlieties numura veidu: *",background="#89cff0")
liel.place(x=10, y=10)
numurs_kaste=Combobox(window,values=numuri)
numurs_kaste.place(x=10,y=30)

#ierašanās izvēle ar kalendāru un iespēja izvēlēties, cik naktis paliks
teksts=Label(window,text="Izvēlieties ierašanās datumu: *",background="#89cff0").place(x=10,y=60)
kalendars=DateEntry(window,date_pattern='yyyy/mm/dd')
kalendars.place(x=10, y=80)
teksts2=Label(window,text="Izvēlieties cik naktis paliksiet: *",background="#89cff0").place(x=10,y=110)
naktis_kaste=Combobox(window,values=skaits)
naktis_kaste.place(x=10,y=130)

#brokastu izvēle
brokastis = Label(window,
                  text="Vai brokastosiet(7€ pers.)? *",
                  background="#89cff0").place(x=10, y=160)
brokastis_kaste = Combobox(window, value=iespejas)
brokastis_kaste.place(x=10, y=180)

#parāda kādas vērtības var būt katram mainīgajam
vards_vertiba=StringVar
uzvards_vertiba=StringVar
tel_vertiba=StringVar
epasts_vertiba=StringVar
check_vertiba=IntVar
numurs_vertiba=StringVar(window)
ierasanas=StringVar
kom_vertiba=StringVar

#izveido etiķetes informācijai par klientu
vards=Label(window, text="Vārds: *",background="#89cff0")
vards.place(x=250,y=10)
uzvards=Label(window, text="Uzvārds: *",background="#89cff0")
uzvards.place(x=250,y=50)
tel=Label(window,text="Tel. nr: *",background="#89cff0")
tel.place(x=250,y=90)
epasts=Label(window,text="E-pasts: *",background="#89cff0")
epasts.place(x=250,y=130)
kom=Label(window, text="Komentāri:",background="#89cff0")
kom.place(x=250, y=170)

#izveido kastes, kurās lietotājs varēs ievadīt iznformāciju par sevi
vards_kaste=Entry(window,textvariable=vards_vertiba)
vards_kaste.place(x=335,y=10)
uzvards_kaste=Entry(window,textvariable=uzvards_vertiba)
uzvards_kaste.place(x=335,y=50)
tel_kaste=Entry(window,textvariable=tel_vertiba)
tel_kaste.place(x=335,y=90)
epasts_kaste=Entry(window,textvariable=epasts_vertiba)
epasts_kaste.place(x=335,y=130)
kom_kaste=Entry(window,textvariable=kom_vertiba)
kom_kaste.place(x=335, y=170)
#atcerēties mani kastīte
check_kaste=Checkbutton(text="Atcerēties mani",variable=check_vertiba)
check_kaste.place(x=335,y=210)

#poga rezervēt, kas izsauc funkciju gatavs_vertiba
Button(text="Rezervēt",command=rezervet).place(x=225,y=250)

#uz ekrāna izveido pirmo lapu
window.mainloop()