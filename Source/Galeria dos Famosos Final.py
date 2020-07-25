from tkinter import *

# Base
ja = Tk()
frame = Frame(ja, bg='#ffffff')
frame.pack(side="top", fill="both", expand=True)
ja.title('Galeria dos Famosos')
ja.iconbitmap('benzene.ico')
w, h = ja.winfo_screenwidth(), ja.winfo_screenheight()
ja.geometry("%dx%d+0+0" % (w, h))
canvas = Canvas(ja, width=w, height=h, bg='#ffffff')
canvas.pack()
canvas.create_line(100, 200, 200, 200, fill="#ffffff")

# Layout
bb = PhotoImage(file='blackboard.png')
bblab = Label(ja, image=bb, borderwidth=0, highlightthickness=0)
bblab.place(x=250, y=0)
til = PhotoImage(file='tiles.png')
tilab = Label(ja, image=til, borderwidth=0, highlightthickness=0)
tilab.place(x=0, y=0)


# Metano
metano = PhotoImage(file='metanoo.png')
metlab = Label(ja, image=metano, borderwidth=0, highlightthickness=0)
metlab.place(x=270, y=40)
metdados = metlab.place_info()
mettitle = Label(ja, text='Metano', font=('arial', 36), bg='#ffffff', borderwidth=6, relief=GROOVE)
mettitle.place(x=650, y=40)
mettdados = mettitle.place_info()
metinfo = Label(ja, font=('arial', 25),
                borderwidth=10,
                relief=GROOVE,
                text='Nome comercial: Biogás ou Gás Natural.\nFunção: Hidrocarboneto.\nUsa-se o nome Biogás quando sua obtenção for por\nmeios'
                     ' naturais e Gás Natural quando for obtido como fóssil.\n'
                     ' É liberado pelo arroto de vacas, lixo, cemitérios e pantanos.')
metinfo.place(x=485, y=150)
metindados = metinfo.place_info()
metlab.visib = True
metlab.place_forget()
mettitle.place_forget()
metinfo.place_forget()


def btmet():
    if metlab.visib:
        purge()
        metlab.place(metdados)
        mettitle.place(mettdados)
        metinfo.place(metindados)
        btmet['text'] = 'Fechar Metano'
        metlab.visib = not metlab.visib
    else:
        metlab.place_forget()
        mettitle.place_forget()
        metinfo.place_forget()
        btmet['text'] = 'Metano'
        metlab.visib = not metlab.visib


btmet = Button(ja, width=25, text='Metano', command=btmet)
btmet.place(x=10, y=10)

# Etano
etano = PhotoImage(file='etano.png')
etlab = Label(ja, image=etano, borderwidth=0, highlightthickness=0)
etlab.place(x=270, y=40)
etdados = etlab.place_info()
ettitle = Label(ja, text='Etano', font=('arial', 36), bg='#ffffff', borderwidth=10, relief=GROOVE)
ettitle.place(x=650, y=40)
ettdados = ettitle.place_info()
etinfo = Label(ja, font=('arial', 25),
                borderwidth=10,
                relief=GROOVE,
                text='Função: Hidrocarboneto.\nÉ basicamente a mesma coisa do Metano, mas \n'
                     'com menos importância.')
etinfo.place(x=485, y=150)
etindados = etinfo.place_info()
etlab.visib = True
etlab.place_forget()
ettitle.place_forget()
etinfo.place_forget()


def btet():
    if etlab.visib:
        purge()
        etlab.place(etdados)
        ettitle.place(ettdados)
        etinfo.place(etindados)
        btet['text'] = 'Fechar Etano'
        etlab.visib = not etlab.visib
    else:
        etlab.place_forget()
        ettitle.place_forget()
        etinfo.place_forget()
        btet['text'] = 'Etano'
        etlab.visib = not etlab.visib


btet = Button(ja, width=25, text='Etano', command=btet)
btet.place(x=10, y=40)

# Propano
propano = PhotoImage(file='propano.png')
prolab = Label(ja, image=propano, borderwidth=0, highlightthickness=0)
prolab.place(x=270, y=40)
prodados = prolab.place_info()
protitle = Label(ja, text='Propano', font=('arial', 36), bg='#ffffff', borderwidth=6, relief=GROOVE)
protitle.place(x=650, y=40)
protdados = protitle.place_info()
proinfo = Label(ja, font=('arial', 25),
                borderwidth=10,
                relief=GROOVE,
                text='Nome Comercial: Gás de Cozinha.\n'
                 'Função: Hidrocarboneto.\nObtido a partir da liquefação do Petróleo, podendo ser \n'
                     'chamado de Gás Liquefeito de Petróleo, ou G.L.P.')
proinfo.place(x=565, y=150)
proindados = proinfo.place_info()
prolab.visib = True
prolab.place_forget()
protitle.place_forget()
proinfo.place_forget()


def btpro():
    if prolab.visib:
        purge()
        prolab.place(prodados)
        protitle.place(protdados)
        proinfo.place(proindados)
        btpro['text'] = 'Fechar Propano'
        prolab.visib = not prolab.visib
    else:
        prolab.place_forget()
        protitle.place_forget()
        proinfo.place_forget()
        btpro['text'] = 'Propano'
        prolab.visib = not prolab.visib


btpro = Button(ja, width=25, text='Propano', command=btpro)
btpro.place(x=10, y=70)

# Butano
butano = PhotoImage(file='butano.png')
butlab = Label(ja, image=butano, borderwidth=0, highlightthickness=0)
butlab.place(x=270, y=40)
butdados = butlab.place_info()
buttitle = Label(ja, text='Butano', font=('arial', 36), bg='#ffffff', borderwidth=6, relief=GROOVE)
buttitle.place(x=650, y=40)
buttdados = buttitle.place_info()
butinfo = Label(ja, font=('arial', 25),
                borderwidth=10,
                relief=GROOVE,
                text='Função: Hidrocarboneto.\nÉ, assim como o Butano, um Gás de Cozinha, assim\n'
                     ' como um G.L.P.')
butinfo.place(x=570, y=150)
butindados = butinfo.place_info()
butlab.visib = True
butlab.place_forget()
buttitle.place_forget()
butinfo.place_forget()


def btbut():
    if butlab.visib:
        purge()
        butlab.place(butdados)
        buttitle.place(buttdados)
        butinfo.place(butindados)
        btbut['text'] = 'Fechar Butano'
        butlab.visib = not butlab.visib
    else:
        butlab.place_forget()
        buttitle.place_forget()
        butinfo.place_forget()
        btbut['text'] = 'Butano'
        butlab.visib = not butlab.visib


btbut = Button(ja, width=25, text='Butano', command=btbut)
btbut.place(x=10, y=100)

# Heptano, Octano e Nonano
heptano = PhotoImage(file='heptano.png')
heplab = Label(ja, image=heptano, borderwidth=0, highlightthickness=0)
heplab.place(x=270, y=135)
hepdados = heplab.place_info()
heptitle = Label(ja, text='Heptano, Octano e Nonano', font=('arial', 36), bg='#ffffff', borderwidth=6, relief=GROOVE)
heptitle.place(x=450, y=40)
heptdados = heptitle.place_info()
hepinfo = Label(ja, font=('arial', 25),
                borderwidth=10,
                relief=GROOVE,
                text='Nome Comercial: Gasolina.\n'
                     'Função: Hidrocarboneto. \n'
                     'Suas qualidades são definidas pela porcentagem de Isoctano (C8H18) no \n'
                     'composto, sendo essa porcentagem conhecida como \"octanagem\"')
hepinfo.place(x=270, y=250)
heptindados = hepinfo.place_info()
heplab.visib = True
heplab.place_forget()
heptitle.place_forget()
hepinfo.place_forget()


def bthep():
    if heplab.visib:
        purge()
        heplab.place(hepdados)
        heptitle.place(heptdados)
        hepinfo.place(heptindados)
        bthep['text'] = 'Fechar Gasolinas'
        heplab.visib = not heplab.visib
    else:
        heplab.place_forget()
        heptitle.place_forget()
        hepinfo.place_forget()
        bthep['text'] = 'Gasolinas'
        heplab.visib = not heplab.visib


bthep = Button(ja, width=25, text='Gasolinas', command=bthep)
bthep.place(x=10, y=130)

# Eteno
eteno = PhotoImage(file='eteno.png')
etalab = Label(ja, image=eteno, borderwidth=0, highlightthickness=0)
etalab.place(x=270, y=40)
etadados = etalab.place_info()
etatitle = Label(ja, text='Eteno', font=('arial', 36), bg='#ffffff', borderwidth=6, relief=GROOVE)
etatitle.place(x=650, y=40)
etatdados = etatitle.place_info()
etainfo = Label(ja, font=('arial', 25),
                borderwidth=10,
                relief=GROOVE,
                text='Nome Comercial: Etileno.\n'
                     'Função: Hidrocarboneto.\nÉ usado para o amadurecimento de frutas.\n'
                     'Assim como os outros alquenos, sofre reações de adição.')
etainfo.place(x=370, y=250)
etaindados = etainfo.place_info()
etalab.visib = True
etalab.place_forget()
etatitle.place_forget()
etainfo.place_forget()


def bteta():
    if etalab.visib:
        purge()
        etalab.place(etadados)
        etatitle.place(etatdados)
        etainfo.place(etaindados)
        bteta['text'] = 'Fechar Eteno'
        etalab.visib = not etalab.visib
    else:
        etalab.place_forget()
        etatitle.place_forget()
        etainfo.place_forget()
        bteta['text'] = 'Eteno'
        etalab.visib = not etalab.visib


bteta = Button(ja, width=25, text='Eteno', command=bteta)
bteta.place(x=10, y=160)

# Etino
etino = PhotoImage(file='etino.png')
etinlab = Label(ja, image=etino, borderwidth=0, highlightthickness=0)
etinlab.place(x=260, y=40)
etinodados = etinlab.place_info()
etintitle = Label(ja, text='Etino', font=('arial', 36), bg='#ffffff', borderwidth=6, relief=GROOVE)
etintitle.place(x=650, y=40)
etintdados = etintitle.place_info()
etininfo = Label(ja, font=('arial', 25),
                borderwidth=10,
                relief=GROOVE,
                text='Nome comercial: Acetileno.\n'
                     'Função: Hidrocarboneto.\nÉ usado como gás de solda ou como gás de maçarico.\n'
                     '')
etininfo.place(x=553, y=150)
etinidados = etininfo.place_info()
etinlab.visib = True
etinlab.place_forget()
etintitle.place_forget()
etininfo.place_forget()


def btetin():
    if etinlab.visib:
        purge()
        etinlab.place(etinodados)
        etintitle.place(etintdados)
        etininfo.place(etinidados)
        btetin['text'] = 'Fechar Etino'
        etinlab.visib = not etinlab.visib
    else:
        etinlab.place_forget()
        etintitle.place_forget()
        etininfo.place_forget()
        btetin['text'] = 'Etino'
        etinlab.visib = not etinlab.visib


btetin = Button(ja, width=25, text='Etino', command=btetin)
btetin.place(x=10, y=190)

# Benzeno
benzeno = PhotoImage(file='benzeno.png')
benlab = Label(ja, image=benzeno, borderwidth=0, highlightthickness=0)
benlab.place(x=260, y=40)
bendados = benlab.place_info()
bentitle = Label(ja, text='Benzeno', font=('arial', 36), bg='#ffffff', borderwidth=6, relief=GROOVE)
bentitle.place(x=750, y=40)
bentdados = bentitle.place_info()
beninfo = Label(ja, font=('arial', 25),
                borderwidth=10,
                relief=GROOVE,
                text='Nome Comercial: Benzeno\n'
                     'Função: Hidrocarboneto.\nÉ usado como solvente orgânico.')
beninfo.place(x=260, y=200)
benidados = beninfo.place_info()
benlab.visib = True
benlab.place_forget()
bentitle.place_forget()
beninfo.place_forget()


def btben():
    if benlab.visib:
        purge()
        benlab.place(bendados)
        bentitle.place(bentdados)
        beninfo.place(benidados)
        btben['text'] = 'Fechar Benzeno'
        benlab.visib = not benlab.visib
    else:
        benlab.place_forget()
        bentitle.place_forget()
        beninfo.place_forget()
        btben['text'] = 'Benzeno'
        benlab.visib = not benlab.visib


btben = Button(ja, width=25, text='Benzeno', command=btben)
btben.place(x=10, y=220)

# Metilbenzeno
mebenzeno = PhotoImage(file='metilbenzeno.png')
mebenlab = Label(ja, image=mebenzeno, borderwidth=0, highlightthickness=0)
mebenlab.place(x=270, y=40)
mebendados = mebenlab.place_info()
mebentitle = Label(ja, text='Metilbenzeno', font=('arial', 36), bg='#ffffff', borderwidth=6, relief=GROOVE)
mebentitle.place(x=650, y=40)
mebentdados = mebentitle.place_info()
mebeninfo = Label(ja, font=('arial', 25),
                borderwidth=10,
                relief=GROOVE,
                text='Nome comercial: Tolueno\n'
                     'Função: Hidrocarboneto.\nÉ usado como solvente de tintas e colas. Conhecido e usado \n'
                     'como cola de sapateiro e como entorpecente.')
mebeninfo.place(x=370, y=200)
mebenidados = mebeninfo.place_info()
mebenlab.visib = True
mebenlab.place_forget()
mebentitle.place_forget()
mebeninfo.place_forget()


def btmeben():
    if mebenlab.visib:
        purge()
        mebenlab.place(mebendados)
        mebentitle.place(mebentdados)
        mebeninfo.place(mebenidados)
        btmeben['text'] = 'Fechar Metilbenzeno'
        mebenlab.visib = not mebenlab.visib
    else:
        mebenlab.place_forget()
        mebentitle.place_forget()
        mebeninfo.place_forget()
        btmeben['text'] = 'Metilbenzeno'
        mebenlab.visib = not mebenlab.visib


btmeben = Button(ja, width=25, text='Metilbenzeno', command=btmeben)
btmeben.place(x=10, y=250)

# Naftaleno
naftaleno = PhotoImage(file='naftaleno.png')
naftlab = Label(ja, image=naftaleno, borderwidth=0, highlightthickness=0)
naftlab.place(x=270, y=40)
naftdados = naftlab.place_info()
nafttitle = Label(ja, text='Naftaleno', font=('arial', 36), bg='#ffffff', borderwidth=6, relief=GROOVE)
nafttitle.place(x=650, y=40)
nafttdados = nafttitle.place_info()
naftinfo = Label(ja, font=('arial', 25),
                borderwidth=10,
                relief=GROOVE,
                text='Nome comercial: Naftalina\n'
                     'Função: Hidrocarboneto.\nÉ usado como repelente de insetos.')
naftinfo.place(x=500, y=200)
naftidados = naftinfo.place_info()
naftlab.visib = True
naftlab.place_forget()
nafttitle.place_forget()
naftinfo.place_forget()


def btnaft():
    if naftlab.visib:
        purge()
        naftlab.place(naftdados)
        nafttitle.place(nafttdados)
        naftinfo.place(naftidados)
        btnaft['text'] = 'Fechar Naftaleno'
        naftlab.visib = not naftlab.visib
    else:
        naftlab.place_forget()
        nafttitle.place_forget()
        naftinfo.place_forget()
        btnaft['text'] = 'Naftaleno'
        naftlab.visib = not naftlab.visib


btnaft = Button(ja, width=25, text='Naftaleno', command=btnaft)
btnaft.place(x=10, y=280)

# Metanol
metanol = PhotoImage(file='METANOL.png')
mollab = Label(ja, image=metanol, borderwidth=0, highlightthickness=0)
mollab.place(x=270, y=40)
moldados = mollab.place_info()
moltitle = Label(ja, text='Metanol', font=('arial', 36), bg='#ffffff', borderwidth=6, relief=GROOVE)
moltitle.place(x=650, y=40)
moltdados = moltitle.place_info()
molinfo = Label(ja, font=('arial', 25),
                borderwidth=10,
                relief=GROOVE,
                text='Nome comercial: Álcool metílico.\n'
                     'Função: Álcool.\n'
                     'É obtido a partir da destilação da \n '
                     'madeira. Pode ser usado como \n'
                     'combustivel, mas é um componente tóxico.')
molinfo.place(x=600, y=200)
molidados = molinfo.place_info()
mollab.visib = True
mollab.place_forget()
moltitle.place_forget()
molinfo.place_forget()


def btmol():
    if mollab.visib:
        purge()
        mollab.place(moldados)
        moltitle.place(moltdados)
        molinfo.place(molidados)
        btmol['text'] = 'Fechar Metanol'
        mollab.visib = not mollab.visib
    else:
        mollab.place_forget()
        moltitle.place_forget()
        molinfo.place_forget()
        btmol['text'] = 'Metanol'
        mollab.visib = not mollab.visib


btmol = Button(ja, width=25, text='Metanol', command=btmol)
btmol.place(x=10, y=310)

# Etanol
etanol = PhotoImage(file='etanol.png')
eollab = Label(ja, image=etanol, borderwidth=0, highlightthickness=0)
eollab.place(x=270, y=40)
eoldados = eollab.place_info()
eoltitle = Label(ja, text='Etanol', font=('arial', 36), bg='#ffffff', borderwidth=6, relief=GROOVE)
eoltitle.place(x=650, y=40)
eoltdados = eoltitle.place_info()
eolinfo = Label(ja, font=('arial', 25),
                borderwidth=10,
                relief=GROOVE,
                text='Nome comercial: Álcool Etílico.\n'
                     'Função: Álcool.'
                     'Muito usado pela indústria farmaceutica.\n')
eolinfo.place(x=450, y=300)
eolidados = eolinfo.place_info()
eollab.visib = True
eollab.place_forget()
eoltitle.place_forget()
eolinfo.place_forget()


def bteol():
    if eollab.visib:
        purge()
        eollab.place(eoldados)
        eoltitle.place(eoltdados)
        eolinfo.place(eolidados)
        bteol['text'] = 'Fechar Etanol'
        eollab.visib = not eollab.visib
    else:
        eollab.place_forget()
        eoltitle.place_forget()
        eolinfo.place_forget()
        bteol['text'] = 'Etanol'
        eollab.visib = not eollab.visib


bteol = Button(ja, width=25, text='Etanol', command=bteol)
bteol.place(x=10, y=340)

# Glicerina
glicerina = PhotoImage(file='glicerina.png')
glicelab = Label(ja, image=glicerina, borderwidth=0, highlightthickness=0)
glicelab.place(x=270, y=40)
glicedados = glicelab.place_info()
glicetitle = Label(ja, text='Glicerina', font=('arial', 36), bg='#ffffff', borderwidth=6, relief=GROOVE)
glicetitle.place(x=650, y=40)
glicetdados = glicetitle.place_info()
gliceinfo = Label(ja, font=('arial', 25),
                borderwidth=10,
                relief=GROOVE,
                text='Nome IUPAC: Propan-1,2,3-triol.\n'
                     'Função: Álcool.\n'
                     'É usado como um umectante. Absorve \n'
                     'água. É hidratante. Faz ligações \n'
                     'de hidrogenio facilmente.')
gliceinfo.place(x=600, y=200)
gliceidados = gliceinfo.place_info()
glicelab.visib = True
glicelab.place_forget()
glicetitle.place_forget()
gliceinfo.place_forget()


def btglice():
    if glicelab.visib:
        purge()
        glicelab.place(glicedados)
        glicetitle.place(glicetdados)
        gliceinfo.place(gliceidados)
        btglice['text'] = 'Fechar Glicerina'
        glicelab.visib = not glicelab.visib
    else:
        glicelab.place_forget()
        glicetitle.place_forget()
        gliceinfo.place_forget()
        btglice['text'] = 'Glicerina'
        glicelab.visib = not glicelab.visib


btglice = Button(ja, width=25, text='Glicerina', command=btglice)
btglice.place(x=10, y=370)

# Hidroxibenzeno
hidrobenzeno = PhotoImage(file='hidroxibenzeno.png')
hidrobenlab = Label(ja, image=hidrobenzeno, borderwidth=0, highlightthickness=0)
hidrobenlab.place(x=270, y=40)
hidrobendados = hidrobenlab.place_info()
hidrobentitle = Label(ja, text='Hidroxibenzeno', font=('arial', 36), bg='#ffffff', borderwidth=6, relief=GROOVE)
hidrobentitle.place(x=650, y=40)
hidrobentdados = hidrobentitle.place_info()
hidrobeninfo = Label(ja, font=('arial', 25),
                borderwidth=10,
                relief=GROOVE,
                text='Nome comercial: Fenol comum ou Ácido Fênico. \n'
                     'Função: Fenol\n'
                     'Possui caráter ácido. É usado como antisseptico.')
hidrobeninfo.place(x=600, y=200)
hidrobenidados = hidrobeninfo.place_info()
hidrobenlab.visib = True
hidrobenlab.place_forget()
hidrobentitle.place_forget()
hidrobeninfo.place_forget()


def bthidroben():
    if hidrobenlab.visib:
        purge()
        hidrobenlab.place(hidrobendados)
        hidrobentitle.place(hidrobentdados)
        hidrobeninfo.place(hidrobenidados)
        bthidroben['text'] = 'Fechar Hidroxibenzeno'
        hidrobenlab.visib = not hidrobenlab.visib
    else:
        hidrobenlab.place_forget()
        hidrobentitle.place_forget()
        hidrobeninfo.place_forget()
        bthidroben['text'] = 'Hidroxibenzeno'
        hidrobenlab.visib = not hidrobenlab.visib


bthidroben = Button(ja, width=25, text='Hidroxibenzeno', command=bthidroben)
bthidroben.place(x=10, y=400)

# Aldeido Fórmico
aformico = PhotoImage(file='cetonaaaa.png')
aforlab = Label(ja, image=aformico, borderwidth=0, highlightthickness=0)
aforlab.place(x=270, y=40)
afordados = aforlab.place_info()
afortitle = Label(ja, text='Metanal', font=('arial', 36), bg='#ffffff', borderwidth=6, relief=GROOVE)
afortitle.place(x=700, y=40)
afortdados = afortitle.place_info()
aforinfo = Label(ja, font=('arial', 25),
                borderwidth=10,
                relief=GROOVE,
                text='Nome comercial: Formol, Formaldeido ou Aldeído Fórmico.\n'
                     'Função: Aldeido.\n'
                     'Usado como conservante de tecidos e animais.')
aforinfo.place(x=400, y=430)
aforidados = aforinfo.place_info()
aforlab.visib = True
aforlab.place_forget()
afortitle.place_forget()
aforinfo.place_forget()


def btafor():
    if aforlab.visib:
        purge()
        aforlab.place(afordados)
        afortitle.place(afortdados)
        aforinfo.place(aforidados)
        btafor['text'] = 'Fechar Metanal'
        aforlab.visib = not aforlab.visib
    else:
        aforlab.place_forget()
        afortitle.place_forget()
        aforinfo.place_forget()
        btafor['text'] = 'Metanal'
        aforlab.visib = not aforlab.visib


btafor = Button(ja, width=25, text='Metanal', command=btafor)
btafor.place(x=10, y=430)

# Propanona
ppanona = PhotoImage(file='propanona.png')
ppanlab = Label(ja, image=ppanona, borderwidth=0, highlightthickness=0)
ppanlab.place(x=270, y=40)
ppandados = ppanlab.place_info()
ppantitle = Label(ja, text='Propanona', font=('arial', 36), bg='#ffffff', borderwidth=6, relief=GROOVE)
ppantitle.place(x=650, y=40)
ppantdados = ppantitle.place_info()
ppaninfo = Label(ja, font=('arial', 25),
                borderwidth=10,
                relief=GROOVE,
                text='Nome comercial: Acetona\n'
                     'Função: Cetona.\n'
                     'É usado para tirar esmaltes e como\n'
                     ' solvente orgânico.')
ppaninfo.place(x=600, y=180)
ppanidados = ppaninfo.place_info()
ppanlab.visib = True
ppanlab.place_forget()
ppantitle.place_forget()
ppaninfo.place_forget()


def btppan():
    if ppanlab.visib:
        purge()
        ppanlab.place(ppandados)
        ppantitle.place(ppantdados)
        ppaninfo.place(ppanidados)
        btppan['text'] = 'Fechar Propanona'
        ppanlab.visib = not ppanlab.visib
    else:
        ppanlab.place_forget()
        ppantitle.place_forget()
        ppaninfo.place_forget()
        btppan['text'] = 'Propanona'
        ppanlab.visib = not ppanlab.visib


btppan = Button(ja, width=25, text='Propanona', command=btppan)
btppan.place(x=10, y=460)

# Etoxietano
etoxetano = PhotoImage(file='etoxietano.png')
etoxlab = Label(ja, image=etoxetano, borderwidth=0, highlightthickness=0)
etoxlab.place(x=270, y=40)
etoxdados = etoxlab.place_info()
etoxtitle = Label(ja, text='Etoxietano', font=('arial', 36), bg='#ffffff', borderwidth=6, relief=GROOVE)
etoxtitle.place(x=650, y=40)
etoxtdados = etoxtitle.place_info()
etoxinfo = Label(ja, font=('arial', 25),
                borderwidth=10,
                relief=GROOVE,
                text='Nome IUPAC: Etoxietano, Eter dietílico\n'
                     'ou Dietil Ester.\n'
                     'Nome Comercial: Éter Comum ou Éter etílico.\n'
                     'É usado como anestésico e como entorpecente.')
etoxinfo.place(x=600, y=180)
etoxidados = etoxinfo.place_info()
etoxlab.visib = True
etoxlab.place_forget()
etoxtitle.place_forget()
etoxinfo.place_forget()


def btetox():
    if etoxlab.visib:
        purge()
        etoxlab.place(etoxdados)
        etoxtitle.place(etoxtdados)
        etoxinfo.place(etoxidados)
        btetox['text'] = 'Fechar Etoxietano'
        etoxlab.visib = not etoxlab.visib
    else:
        etoxlab.place_forget()
        etoxtitle.place_forget()
        etoxinfo.place_forget()
        btetox['text'] = 'Etoxietano'
        etoxlab.visib = not etoxlab.visib


btetox = Button(ja, width=25, text='Etoxietano', command=btetox)
btetox.place(x=10, y=490)

# Ácido Metanóico
ametanoico = PhotoImage(file='amet.png')
ametlab = Label(ja, image=ametanoico, borderwidth=0, highlightthickness=0)
ametlab.place(x=270, y=40)
ametdados = ametlab.place_info()
amettitle = Label(ja, text='Ácido Metanoico', font=('arial', 36), bg='#ffffff', borderwidth=6, relief=GROOVE)
amettitle.place(x=800, y=40)
amettdados = amettitle.place_info()
ametinfo = Label(ja, font=('arial', 25),
                borderwidth=10,
                relief=GROOVE,
                text='Nome Comercial: Ácido Fórmico.\n'
                     'Função: Ácido Carboxílico.\n'
                     'Encontrado em picadas de insetos.')
ametinfo.place(x=800, y=180)
ametidados = ametinfo.place_info()
ametlab.visib = True
ametlab.place_forget()
amettitle.place_forget()
ametinfo.place_forget()


def btamet():
    if ametlab.visib:
        purge()
        ametlab.place(ametdados)
        amettitle.place(amettdados)
        ametinfo.place(ametidados)
        btamet['text'] = 'Fechar Ácido Metanoico'
        ametlab.visib = not ametlab.visib
    else:
        ametlab.place_forget()
        amettitle.place_forget()
        ametinfo.place_forget()
        btamet['text'] = 'Ácido Metanoico'
        ametlab.visib = not ametlab.visib


btamet = Button(ja, width=25, text='Ácido Metanoico', command=btamet)
btamet.place(x=10, y=520)

# Ácido Etanoico
aetanoico = PhotoImage(file='acido aceeetico.png')
aetlab = Label(ja, image=aetanoico, borderwidth=0, highlightthickness=0)
aetlab.place(x=250, y=40)
aetdados = aetlab.place_info()
aettitle = Label(ja, text='Ácido Etanoico', font=('arial', 36), bg='#ffffff', borderwidth=6, relief=GROOVE)
aettitle.place(x=800, y=40)
aettdados = aettitle.place_info()
aetinfo = Label(ja, font=('arial', 25),
                borderwidth=10,
                relief=GROOVE,
                text='Nome Comercial: Ácido Acético ou Vinagre.\n'
                     'Função: Ácido Carboxílico.\n'
                     'É usado como condimento.')
aetinfo.place(x=520, y=550)
aetidados = aetinfo.place_info()
aetlab.visib = True
aetlab.place_forget()
aettitle.place_forget()
aetinfo.place_forget()


def btaet():
    if aetlab.visib:
        purge()
        aetlab.place(aetdados)
        aettitle.place(aettdados)
        aetinfo.place(aetidados)
        btaet['text'] = 'Fechar Ácido Etanoico'
        aetlab.visib = not aetlab.visib
    else:
        aetlab.place_forget()
        aettitle.place_forget()
        aetinfo.place_forget()
        btaet['text'] = 'Ácido Etanoico'
        aetlab.visib = not aetlab.visib


btaet = Button(ja, width=25, text='Ácido Etanoico', command=btaet)
btaet.place(x=10, y=550)

# Ácido Benzoico
abenzoico = PhotoImage(file='acidbenzo.png')
abenlab = Label(ja, image=abenzoico, borderwidth=0, highlightthickness=0)
abenlab.place(x=270, y=40)
abendados = abenlab.place_info()
abentitle = Label(ja, text='Ácido Benzoico', font=('arial', 36), bg='#ffffff', borderwidth=6, relief=GROOVE)
abentitle.place(x=850, y=40)
abentdados = abentitle.place_info()
abeninfo = Label(ja, font=('arial', 25),
                borderwidth=10,
                relief=GROOVE,
                text=''
                     'Função: Ácido Carboxílico.\n'
                     'É usado como conservante de alimentos.')
abeninfo.place(x=650, y=380)
abenidados = abeninfo.place_info()
abenlab.visib = True
abenlab.place_forget()
abentitle.place_forget()
abeninfo.place_forget()


def btaben():
    if abenlab.visib:
        purge()
        abenlab.place(abendados)
        abentitle.place(abentdados)
        abeninfo.place(abenidados)
        btaben['text'] = 'Fechar Ácido Benzoico'
        abenlab.visib = not abenlab.visib
    else:
        abenlab.place_forget()
        abentitle.place_forget()
        abeninfo.place_forget()
        btaben['text'] = 'Ácido Benzoico'
        abenlab.visib = not abenlab.visib


btaben = Button(ja, width=25, text='Ácido Benzoico', command=btaben)
btaben.place(x=10, y=580)

# Fenilamina
famizoico = PhotoImage(file='anilina.png')
familab = Label(ja, image=famizoico, borderwidth=0, highlightthickness=0)
familab.place(x=270, y=40)
famidados = familab.place_info()
famititle = Label(ja, text='Fenilamina', font=('arial', 36), bg='#ffffff', borderwidth=6, relief=GROOVE)
famititle.place(x=650, y=40)
famitdados = famititle.place_info()
famiinfo = Label(ja, font=('arial', 25),
                borderwidth=10,
                relief=GROOVE,
                text='Nome Comercial: Anilina\n'
                     'Função: Amina e Fenol.\n'
                     'É usado como conservante de alimentos.')
famiinfo.place(x=670, y=180)
famiidados = famiinfo.place_info()
familab.visib = True
familab.place_forget()
famititle.place_forget()
famiinfo.place_forget()


def btfami():
    if familab.visib:
        purge()
        familab.place(famidados)
        famititle.place(famitdados)
        famiinfo.place(famiidados)
        btfami['text'] = 'Fechar Fenilamina'
        familab.visib = not familab.visib
    else:
        familab.place_forget()
        famititle.place_forget()
        famiinfo.place_forget()
        btfami['text'] = 'Fenilamina'
        familab.visib = not familab.visib


btfami = Button(ja, width=25, text='Fenilamina', command=btfami)
btfami.place(x=10, y=610)

# Triclorometano
cloroformio = PhotoImage(file='cloroformio.png')
clofolab = Label(ja, image=cloroformio, borderwidth=0, highlightthickness=0)
clofolab.place(x=270, y=40)
clofodados = clofolab.place_info()
clofotitle = Label(ja, text='Tricolorometano', font=('arial', 36), bg='#ffffff', borderwidth=6, relief=GROOVE)
clofotitle.place(x=650, y=40)
clofotdados = clofotitle.place_info()
clofoinfo = Label(ja, font=('arial', 25),
                borderwidth=10,
                relief=GROOVE,
                text='Nome IUPAC: Triclorometano ou Tricloreto de Metila\n'
                     'Nome Comercial: Cloroformio\n'
                     'Função: Haleto Orgânico.\n'
                     'É usado como analgésico e como entorpecente.')
clofoinfo.place(x=575, y=180)
clofoidados = clofoinfo.place_info()
clofolab.visib = True
clofolab.place_forget()
clofotitle.place_forget()
clofoinfo.place_forget()


def btclofo():
    if clofolab.visib:
        purge()
        clofolab.place(clofodados)
        clofotitle.place(clofotdados)
        clofoinfo.place(clofoidados)
        btclofo['text'] = 'Fechar Triclorometano'
        clofolab.visib = not clofolab.visib
    else:
        clofolab.place_forget()
        clofotitle.place_forget()
        clofoinfo.place_forget()
        btclofo['text'] = 'Triclorometano'
        clofolab.visib = not clofolab.visib


btclofo = Button(ja, width=25, text='Triclorometano', command=btclofo)
btclofo.place(x=10, y=640)

# Créditos
creditos = Label(ja, text='Todas as imagens foram baixadas pelo '
                         'Google Imagens.\n'
                         'Imagens foram editadas para a adicão de '
                         'bordas e conversão \n do tipo dos arquvios.\n'
                         'Programa escrito em Python usando o módulo tkinter\n'
                         ' \n'
                         'Fontes: Caderno TOP.\n'
                         'Site parceiro: thepowerofthechemistry.wordpress.com\n'
                         '(Feito pelo Igão) \n'
                         ' \n'
                         'Agradeço a todos que me ajudaram na criação do programa, vocês são fodas <3\n'
                         ' \n'
                         'Projetado e escrito por Israel Péres, aluno do 3-A do E.M.',
                font=('arial', 22), bg='#ffffff', borderwidth=6, relief=GROOVE)
creditos.place(x=270, y=10)
credinfo = creditos.place_info()
creditos.visib = True
creditos.place_forget()


def btcred():
    if creditos.visib:
        purge()
        creditos.place(credinfo)
        btcred['text'] = 'Fechar créditos'
        creditos.visib = not creditos.visib
    else:
        creditos.place_forget()
        btcred['text'] = 'Créditos'
        creditos.visib = not creditos.visib


btcred = Button(ja, width=25, text='Créditos', command=btcred)
btcred.place(x=10, y=670)

# Função Purge
def purge():
    metlab.place_forget()
    mettitle.place_forget()
    metinfo.place_forget()
    metlab.visib = True
    btmet['text'] = 'Metano'
    etlab.place_forget()
    ettitle.place_forget()
    etinfo.place_forget()
    etlab.visib = True
    btet['text'] = 'Etano'
    prolab.place_forget()
    protitle.place_forget()
    proinfo.place_forget()
    btpro['text'] = 'Propano'
    prolab.visib = True
    butlab.place_forget()
    buttitle.place_forget()
    butinfo.place_forget()
    btbut['text'] = 'Butano'
    butlab.visib = True
    heplab.place_forget()
    heptitle.place_forget()
    hepinfo.place_forget()
    bthep['text'] = 'Gasolinas'
    heplab.visib = True
    etalab.place_forget()
    etatitle.place_forget()
    etainfo.place_forget()
    bteta['text'] = 'Eteno'
    etalab.visib = True
    etinlab.place_forget()
    etintitle.place_forget()
    etininfo.place_forget()
    btetin['text'] = 'Etino'
    etinlab.visib = True
    benlab.place_forget()
    bentitle.place_forget()
    beninfo.place_forget()
    btben['text'] = 'Benzeno'
    benlab.visib = True
    mebenlab.place_forget()
    mebentitle.place_forget()
    mebeninfo.place_forget()
    btmeben['text'] = 'Metilbenzeno'
    mebenlab.visib = True
    naftlab.place_forget()
    nafttitle.place_forget()
    naftinfo.place_forget()
    btnaft['text'] = 'Naftaleno'
    naftlab.visib = True
    mollab.place_forget()
    moltitle.place_forget()
    molinfo.place_forget()
    btmol['text'] = 'Metanol'
    mollab.visib = True
    eollab.place_forget()
    eoltitle.place_forget()
    eolinfo.place_forget()
    bteol['text'] = 'Etanol'
    eollab.visib = True
    glicelab.place_forget()
    glicetitle.place_forget()
    gliceinfo.place_forget()
    btglice['text'] = 'Glicerina'
    glicelab.visib = True
    hidrobenlab.place_forget()
    hidrobentitle.place_forget()
    hidrobeninfo.place_forget()
    bthidroben['text'] = 'Hidroxibenzeno'
    hidrobenlab.visib = True
    aforlab.place_forget()
    afortitle.place_forget()
    aforinfo.place_forget()
    btafor['text'] = 'Metanal'
    aforlab.visib = True
    ppanlab.place_forget()
    ppantitle.place_forget()
    ppaninfo.place_forget()
    btppan['text'] = 'Propanona'
    ppanlab.visib = True
    etoxlab.place_forget()
    etoxtitle.place_forget()
    etoxinfo.place_forget()
    btetox['text'] = 'Etoxietano'
    etoxlab.visib = True
    ametlab.place_forget()
    amettitle.place_forget()
    ametinfo.place_forget()
    btamet['text'] = 'Ácido Metanóico'
    ametlab.visib = True
    aetlab.place_forget()
    aettitle.place_forget()
    aetinfo.place_forget()
    btaet['text'] = 'Ácido Etanoico'
    aetlab.visib = True
    abenlab.place_forget()
    abentitle.place_forget()
    abeninfo.place_forget()
    btaben['text'] = 'Ácido Benzoico'
    abenlab.visib = True
    familab.place_forget()
    famititle.place_forget()
    famiinfo.place_forget()
    btfami['text'] = 'Fenilamina'
    familab.visib = True
    clofolab.place_forget()
    clofotitle.place_forget()
    clofoinfo.place_forget()
    btclofo['text'] = 'Triclorometano'
    clofolab.visib = True
    creditos.place_forget()
    btcred['text'] = 'Créditos'
    creditos.visib = True

ja.mainloop()
