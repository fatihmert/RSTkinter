#-*- coding:utf-8 -*-

####################################
####################################
# Name:   RSTkinter                #
# Author:  Fatih Mert Doğancan     #
# Web:    www.istihza.com          #
# Release: 17 Temmuz 2012          #
# Version: 0.0.1.4                 #
####################################
####################################
# Version 0.0.1 -> Release Çıkış!  #
# Thank you: umtsn, royan_367      #
####################################
# Version 0.0.1.2 -> Highlight'a   #
# hemen hemen tüm diller eklendi!  #
####################################
# Version 0.0.1.3 -> Başlıklar dü- #
# zenlendi ve kaydetme butonu ça-  #
# şır halde, meta eklendi          #
# Thank you: royan_367             #
####################################
# Version 0.0.1.4 -> Resim ekleme  #
# seçeneği geliştirildi. Numaralı  #
# liste devreye girdi.             #
# Thank you: royan_367             #
####################################


from Tkinter import *
from tkFileDialog import asksaveasfile as savefile

class RSTkinter:
    def __init__(self):
        self.pencere_load()
        self.araclar()

    def pencere_load(self):
        pencere.resizable(width=FALSE,height=FALSE)
        pencere.title("RSTkinter")
        #xrandr  | grep * | cut -d' ' -f4
        pencere.geometry("600x400+%s+%s"%(((pencere.winfo_screenwidth() - 600) / 2),((pencere.winfo_screenheight() - 400) / 2)))

    def araclar(self):
        h1 = Button(text=u"Başlıklar",command=self.h1p)
        h1.place(rely=0.0)

        italik = Button(text=u"İ",command=self.italik_p) # *bla bla*
        italik.place(rely=0.0,relx=0.08)

        kalin = Button(text="B",command=self.kalin_p) # **bla bla**
        kalin.place(rely=0.0,relx=0.104)

        sayili_liste = Button(text=u"Liste(Numaralı)",command=self.liste_p) # 1. bla bla
        sayili_liste.place(rely=0.0,relx=0.1305)

        liste = Button(text=u"Liste", command=self.numsuz_liste_p) # * bla bla
        liste.place(rely=0.0,relx=0.265)

        link = Button(text="Link", command=self.link) # 1
        link.place(rely=0.0,relx=0.318)

        resim = Button(text="Resim",command=self.resim_p) # .. image:: istihza.png
        resim.place(rely=0.0,relx=0.364)

        hl = Button(text="Highlight",command=self.hl_p) # .. highlight:: py (n) bla bla (n) (t) py kodu..
        hl.place(rely=0.0,relx=0.427)

        note = Button(text="Not",command=self.note_p) # .. note:: bla bla
        note.place(rely=0.0,relx=0.51)

        uyari = Button(text=u"Uyarı",command=self.uyari_p) # ..warning:: bla bla
        uyari.place(rely=0.0,relx=0.555)

        meta = Button(text="Meta",command=self.meta_p)
        meta.place(rely=0.0,relx=0.6125)

        kaydet = Button(text="Kaydet",command=self.kaydet)
        kaydet.place(rely=0.0,relx=0.92)

        kaydirmay = Scrollbar(pencere)
        #kaydirmax = Scrollbar(pencere)
        self.metin = Text(font="Helvetica 15 bold",yscrollcommand=kaydirmay.set)   # degisiklik

        self.metin.config(width = 51, height = 13)

        kaydirmay.place(relx=0.975,rely=0.0615,height=377)
        #kaydirmax.place(relx=0.0,rely=0.9)

        self.metin.place(rely=0.06,width=585,height=380)    # degisiklik

        #kaydirmax.config(command=self.metin.xview)
        kaydirmay.config(command=self.metin.yview)


    def kaydet(self):
        self.dosya_ayar = options = {}
        options['defaultextension'] = ''
        options['filetypes'] = [(u'Tüm dosyalar', '.*'), (u'RST belgeleri', '.rst'),("Text belgeleri",".txt")]
        options['initialdir'] = 'C:\\'
        options['initialfile'] = 'RSTkinter.rst'
        options['title'] = 'RSTkinter - Mevcut Çalışmanı Kaydet'
        cikis = savefile(mode="w",**self.dosya_ayar)
        #toctree ayarları eklenecek!
        cikis.write("..\n\tBu dosya RSTkinter 0.0.1.3 ile oluşturulmuştur.\n\tBenzer programlar için www.istihza.com adresini ziyaret ediniz!\n\n.. toctree::\n\t:maxdepth: 2\n\n%s"%str(self.metin.get(0.0,END)))
        cikis.close



    def link(self):
        link = Toplevel()
        link.title("RSTkinter - Link")
        link.resizable(width=FALSE,height=FALSE)
        link.geometry("200x140")

        linK = Label(link,text="Link: ")
        linK.place(relx=0.0,rely=0.0)

        self.linKk = Entry(link)    # degisiklik
        self.linKk.place(relx=0.15,rely=0.0075,width=165)    # degisiklik

        linK_isim = Label(link,text=u"Linkin görünen adı: ")
        linK_isim.place(relx=0.0,rely=0.15)

        self.linK_Isim = Entry(link)    # degisiklik
        self.linK_Isim.place(relx=0.48,rely=0.16,width=100)    # degisiklik

        link_yap = Button(link,text="Ekle",command=self.link_yap)
        link_yap.place(relx=0.42,rely=0.35)

    def link_yap(self):
        link_isim_al = self.linK_Isim.get()    # degisiklik
        link_adres_al = self.linKk.get()    # degisiklik

        if link_adres_al[:7] == "http://":
            link_son = "`%s <%s>`_"%(link_isim_al,link_adres_al)
        elif link_adres_al[7:10] == "www":
            link_son = "`%s <http://%s>`_"%(link_isim_al,link_adres_al)
        else:
            link_son = "`%s <http://www.%s>`_"%(link_isim_al,link_adres_al)

        return self.metin.insert(END,link_son)        # degisiklik

    ######################

    def resim_p(self):
        resim = Toplevel()
        resim.title("RSTkinter - Resim")
        resim.resizable(width=FALSE,height=FALSE)
        resim.geometry("200x140")

        resim_l = Label(resim,text=u"Resim adı: ")
        resim_l.place(relx=0.0,rely=0.0)

        self.resim_a = Entry(resim)
        self.resim_a.place(relx=0.3,rely=0.0)

        self.resim_d = StringVar(resim)
        self.resim_d.set(u"Uzantı Seçin!")

        resim_u = OptionMenu(resim,self.resim_d,"JPG","PNG",u"GİF","BMP",u"Tüm uzantılar")
        resim_u.place(relx=0.0,rely=0.15)

        resim_ekle = Button(resim,text=u"Ekle",command=self.resmi_ekle)
        resim_ekle.place(relx=0.7,rely=0.165,width=50)

        self.resimIAd = IntVar()
        self.resimIAd.set(0)

        resimIA = Checkbutton(resim,text=u"İnce ayarlar",variable=self.resimIAd)
        resimIA.place(relx=0.0,rely=0.34)

        resimHL = Label(resim,text=u"Yükseklik:")
        resimHL.place(relx=0.0,rely=0.48)

        self.resimHE= Entry(resim)
        self.resimHE.place(rely=0.48,relx=0.3,width=25)

        resimWL = Label(resim,text=u"Genişlik:")
        resimWL.place(relx=0.43,rely=0.48)

        self.resimWE = Entry(resim)
        self.resimWE.place(rely=0.48,relx=0.65,width=25)

        resimSL = Label(resim,text=u"Boyut:")
        resimSL.place(relx=0.0,rely=0.65)

        self.resimSE = Entry(resim)
        self.resimSE.place(rely=0.65,relx=0.23,width=25)

        resimAL = Label(resim,text=u"Açıklama: ")
        resimAL.place(rely=0.85,relx=0.0)

        self.resimAE = Entry(resim)
        self.resimAE.place(rely=0.85,relx=0.25)

        self.resimAld = StringVar()
        self.resimAld.set("Hiza seçin")

        self.hizalamalar = {
                u"Sağa":"right",
                "Sola":"left",
                "Ortala":"center",
                u"Olduğu gibi bırak":""
        }
        resimAlO = apply(OptionMenu,(resim,self.resimAld)+tuple(self.hizalamalar))
        resimAlO.place(rely=0.61,relx=0.5)

    def resmi_ekle(self):
        resim_adini_al = self.resim_a.get()
        resim_uzantisini_al = self.resim_d.get()
        ince_ayarlar = []
        if self.resimIAd.get() == 0:
            if resim_uzantisini_al == u"Uzantı Seçin!":
                import tkMessageBox
                tkMessageBox.showwarning(u"RSTkinter - Resim Hata",u"Lütfen bir uzantı seçiniz!")
                del tkMessageBox
            if resim_uzantisini_al == u"Tüm uzantılar":
                son_resim_ekle = "\n .. image:: %s.*"%resim_adini_al
            else:
                son_resim_ekle = "\n .. image:: %s.%s"%(resim_adini_al,resim_uzantisini_al.lower())

                return self.metin.insert(END,son_resim_ekle)
        else:
            # AHH BURASI ÇOK YOĞUN KISA YOLU VARSA KOD KALABALIĞINDAN KURTULSUN PROGRAM ;)
            if self.resimHE.get() != "" and self.resimWE.get() != "" and self.resimSE.get() != "" and self.resimAE.get() != "" and self.resimAld.get() != "":
                ince_ayarlar.insert(0,"\n\t:height: %s"%self.resimHE.get())
                ince_ayarlar.insert(0,"\n\t:width: %s"%self.resimWE.get())
                ince_ayarlar.insert(0,"\n\t:scale: %s %%"%self.resimSE.get())
                ince_ayarlar.insert(0,"\n\t:alt: %s"%self.resimAE.get())
                ince_ayarlar.insert(0,"\n\t:align: %s"%self.hizalamalar[self.resimAld.get()])
            elif self.resimHE.get() == "":
                ince_ayarlar.insert(0,"\n\t:width: %s"%self.resimWE.get())
                ince_ayarlar.insert(0,"\n\t:scale: %s %%"%self.resimSE.get())
                ince_ayarlar.insert(0,"\n\t:alt: %s"%self.resimAE.get())
                ince_ayarlar.insert(0,"\n\t:align: %s"%self.hizalamalar[self.resimAld.get()])
            elif self.resimWE.get() == "":
                ince_ayarlar.insert(0,"\n\t:scale: %s %%"%self.resimSE.get())
                ince_ayarlar.insert(0,"\n\t:alt: %s"%self.resimAE.get())
                ince_ayarlar.insert(0,"\n\t:align: %s"%self.hizalamalar[self.resimAld.get()])
                ince_ayarlar.insert(0,"\n\t:height: %s\n"%self.resimHE.get())
            elif self.resimWE.get() == "" and self.resimHE.get() == "":
                ince_ayarlar.insert(0,"\n\t:scale: %s %%"%self.resimSE.get())
                ince_ayarlar.insert(0,"\n\t:alt: %s"%self.resimAE.get())
                ince_ayarlar.insert(0,"\n\t:align: %s"%self.hizalamalar[self.resimAld.get()])
            elif self.resimSE.get() == "":
                ince_ayarlar.insert(0,"\n\t:height: %s"%self.resimHE.get())
                ince_ayarlar.insert(0,"\n\t:width: %s"%self.resimWE.get())
                ince_ayarlar.insert(0,"\n\t:alt: %s"%self.resimAE.get())
                ince_ayarlar.insert(0,"\n\t:align: %s"%self.hizalamalar[self.resimAld.get()])
            elif self.resimSE.get() == "" and self.resimWE.get() == "":
                ince_ayarlar.insert(0,"\n\t:height: %s"%self.resimHE.get())
                ince_ayarlar.insert(0,"\n\t:alt: %s"%self.resimAE.get())
                ince_ayarlar.insert(0,"\n\t:align: %s"%self.hizalamalar[self.resimAld.get()])
            elif self.resimSE.get() == "" and self.resimWE.get() == "" and self.resimHE.get() == "":
                ince_ayarlar.insert(0,"\n\t:alt: %s"%self.resimAE.get())
                ince_ayarlar.insert(0,"\n\t:align: %s"%self.hizalamalar[self.resimAld.get()])
            elif self.resimAE.get() == "":
                ince_ayarlar.insert(0,"\n\t:height: %s"%self.resimHE.get())
                ince_ayarlar.insert(0,"\n\t:width: %s"%self.resimWE.get())
                ince_ayarlar.insert(0,"\n\t:scale: %s %%"%self.resimSE.get())
                ince_ayarlar.insert(0,"\n\t:align: %s"%self.hizalamalar[self.resimAld.get()])
            elif self.resimAE.get() == "" and self.resimSE.get() == "":
                ince_ayarlar.insert(0,"\n\t:height: %s"%self.resimHE.get())
                ince_ayarlar.insert(0,"\n\t:width: %s"%self.resimWE.get())
                ince_ayarlar.insert(0,"\n\t:align: %s"%self.hizalamalar[self.resimAld.get()])
            elif self.resimAE.get() == "" and self.resimSE.get() == "" and self.resimWE.get() == "":
                ince_ayarlar.insert(0,"\n\t:height: %s"%self.resimHE.get())
                ince_ayarlar.insert(0,"\n\t:align: %s"%self.hizalamalar[self.resimAld.get()])
            elif self.resimAE.get() == "" and self.resimSE.get() == "" and self.resimWE.get() == "" and self.resimHE.get() == "":
                ince_ayarlar.insert(0,"\n\t:align: %s"%self.hizalamalar[self.resimAld.get()])
            elif self.resimAld.get() == "":
                ince_ayarlar.insert(0,"\n\t:height: %s"%self.resimHE.get())
                ince_ayarlar.insert(0,"\n\t:width: %s"%self.resimWE.get())
                ince_ayarlar.insert(0,"\n\t:scale: %s %%"%self.resimSE.get())
                ince_ayarlar.insert(0,"\n\t:alt: %s"%self.resimAE.get())
            elif self.resimAld.get() == "" and self.resimAE.get() == "":
                ince_ayarlar.insert(0,"\n\t:height: %s"%self.resimHE.get())
                ince_ayarlar.insert(0,"\n\t:width: %s"%self.resimWE.get())
                ince_ayarlar.insert(0,"\n\t:scale: %s %%"%self.resimSE.get())
            elif self.resimAld.get() == "" and self.resimAE.get() == "" and self.resimSE.get() == "":
                ince_ayarlar.insert(0,"\n\t:height: %s"%self.resimHE.get())
                ince_ayarlar.insert(0,"\n\t:width: %s"%self.resimWE.get())
            elif self.resimAld.get() == "" and self.resimAE.get() == "" and self.resimSE.get() == "" and self.resimHE.get() == "":
                ince_ayarlar.insert(0,"\n\t:width: %s"%self.resimWE.get())
            elif self.resimAld.get() == "" and self.resimAE.get() == "" and self.resimSE.get() == "" and self.resimHE.get() == "" and self.resimWE.get() == "":
                ince_ayarlar.insert(0,"")
            elif self.resimAld.get() == u"Olduğu gibi bırak":
                ince_ayarlar.insert(0,"\n\t:height: %s"%self.resimHE.get())
                ince_ayarlar.insert(0,"\n\t:width: %s"%self.resimWE.get())
                ince_ayarlar.insert(0,"\n\t:scale: %s %%"%self.resimSE.get())
                ince_ayarlar.insert(0,"\n\t:alt: %s"%self.resimAE.get())
            else:
                import tkMessageBox
                tkMessageBox.showwarning(u"RSTkinter - Resim Hata",u"Tekrar kontrol edin!")
                del tkMessageBox

            if resim_uzantisini_al == u"Tüm uzantılar":
                son_resim_ekle = "\n .. image:: %s.*"%resim_adini_al
            else:
                son_resim_ekle = "\n .. image:: %s.%s"%(resim_adini_al,resim_uzantisini_al.lower())

            ince_ayar_son = [i for i in ince_ayarlar]

            self.metin.insert(END, son_resim_ekle)

            for karDiz in ince_ayar_son:
                self.metin.insert(END, karDiz)

    ######################

    def italik_p(self):
        italik = Toplevel()
        italik.title("RSTkinter - İtalik")
        italik.resizable(width=FALSE,height=FALSE)
        italik.geometry("200x140")

        italik_l = Label(italik,text=u"İtalik olacak yazı: ")
        italik_l.place(relx=0.0,rely=0.0)

        self.italik_a = Entry(italik)
        self.italik_a.place(relx=0.3,rely=0.0)

        italik_b = Button(italik,text=u"Ekle",command=self.italik_yap)
        italik_b.place(relx=0.0,rely=0.2)

    def italik_yap(self):
        return self.metin.insert(END," *%s* "%self.italik_a.get())

    ######################

    def kalin_p(self):
        kalin = Toplevel()
        kalin.title("RSTkinter - Kalın")
        kalin.resizable(width=FALSE,height=FALSE)
        kalin.geometry("200x140")

        kalin_l = Label(kalin,text=u"Kalın olacak yazı: ")
        kalin_l.place(relx=0.0,rely=0.0)

        self.kalin_a = Entry(kalin)
        self.kalin_a.place(relx=0.3,rely=0.0)

        kalin_b = Button(kalin,text=u"Ekle",command=self.kalin_yap)
        kalin_b.place(relx=0.0,rely=0.2)

    def kalin_yap(self):
        return self.metin.insert(END," **%s** "%self.kalin_a.get())


    ######################

    def note_p(self):
        note = Toplevel()
        note.title("RSTkinter - Not")
        note.resizable(width=FALSE,height=FALSE)
        note.geometry("200x140")

        note_l = Label(note,text=u"Notu yazın: ")
        note_l.place(relx=0.0,rely=0.0)

        self.note_a = Text(note)
        self.note_a.place(relx=0.3,rely=0.0,width=130)

        note_b = Button(note,text=u"Ekle",command=self.note_yap)
        note_b.place(relx=0.0,rely=0.2)

    def note_yap(self):
        return self.metin.insert(END,"\n .. note:: %s "%self.note_a.get(1.0,END))

    ######################

    def uyari_p(self):
        uyari = Toplevel()
        uyari.title("RSTkinter - Not")
        uyari.resizable(width=FALSE,height=FALSE)
        uyari.geometry("200x140")

        uyari_l = Label(uyari,text=u"Uyarı yazın: ")
        uyari_l.place(relx=0.0,rely=0.0)

        self.uyari_a = Text(uyari)
        self.uyari_a.place(relx=0.3,rely=0.0,width=130)

        uyari_b = Button(uyari,text=u"Ekle",command=self.uyari_yap)
        uyari_b.place(relx=0.0,rely=0.2)

    def uyari_yap(self):
        return self.metin.insert(END,"\n ..warning:: %s "%self.uyari_a.get(1.0,END))

    ######################

    def hl_p(self):
        HL = Toplevel()
        HL.title("RSTkinter - Highlight")
        HL.resizable(width=FALSE,height=FALSE)
        HL.geometry("250x300")



        self.HL_d = StringVar(HL)
        self.HL_d.set(u"Dil Seçin!")

        self.diller = {
			"ABAP":"abap",
			"ANTLR":"antlr",
			"ActionScript":"as",
			"ActionScript 3":"as3",
			"ApacheConf":"apacheconf",
			"AppleScript":"applescript",
			"Asymptote":"asy",
			"BBCode":"bbcode",
			"Bash":"bash",
			"Batchfile":"bat",
			"Befunge":"befunge",
			"Boo":"boo",
			"Brainfuck":"brainfuck",
			"C":"c",
			"C#":"csharp",
            "C++":"cpp",
            "CMake":"cmake",
			"CSS":"css",
			"Cheetah":"cheetah",
			"Clojure":"clojure",
			"Cython":"cython",
			"D":"d",
			"Delphi":"delphi",
			"Diff":"diff",
			"Django/Jinja":"django",
			"Dylan":"dylan",
			"ERB":"erb",
			"Erlang":"erlang",
			"Evoque":"evoque",
			"Fortran":"fortran",
			"GAS":"gas",
			"GLSL":"glsl",
			"Genshi":"genshi",
			"Gherkin":"Cucumber",
			"Go":"go",
			"Groff":"groff",
			"HTML":"html",
			"Haskell":"haskell",
			"INI":"ini",
			"IRC logs":"irc",
			"Io":"io",
			"Java":"java",
			"Java Server Page":"jsp",
			"JavaScript":"js",
			"LLVM":"llvm",
			"Logtalk":"logtalk",
			"Lua":"lua",
			"MOOCode":"moocode",
			"MXML":"mxml",
			"Makefile":"make",
			"Mako":"mako",
			"Matlab":"matlab",
			"MiniD":"minid",
			"Modelica":"modelica",
			"MoinMoin/Trac Wiki":"trac-wiki",
			"MuPAD":"mupad",
			"MySQL":"mysql",
			"Myghty":"myghty",
			"NASM":"nasm",
			"Newspeak":"newspeak",
			"NumPy":"numpy",
			"OCaml":"ocaml",
			"Objective-C":"objective-c",
			"Ooc":"ooc",
			"PHP":"php",
			"POVRay":"pov",
			"Perl":"perl",
			"Prolog":"prolog",
			"Python":"python",
			"Python 3":"python3",
			"Python console":"pycon",
			"REBOL":"rebol",
			"RHTML":"rhtml",
			"Ragel":"ragel",
			"Raw token":"raw",
			"Redcode":"redcode",
			"Ruby":"rb",
			"Ruby Console":"rbcon",
			"S":"splus",
			"SQL":"sql",
			"Scala":"scala",
			"Scheme":"scheme",
			"Smalltalk":"smalltalk",
			"Smarty":"smarty",
			"SquidConf":"squidconf",
			"Tcl":"tcl",
			"Tcsh":"tcsh",
			"TeX":"tex",
			"Text":"text",
			"VB.net":"vb.net",
			"Vala":"vala",
			"VimL":"viml",
			"XML":"xml",
			"XSLT":"xslt",
			"YAML":"yaml",
			"reStructuredText":"rst",
			"SQLite3":"sqlite3"
        }

        HL_u = apply(OptionMenu,(HL,self.HL_d)+tuple(self.diller))
        HL_u.place(relx=0.0,rely=0.0)

        HL_l = Label(HL,text=u"Açıklamanızı yazın: ")
        HL_l.place(relx=0.0,rely=0.15)

        self.HL_a = Text(HL)
        self.HL_a.place(relx=0.05,rely=0.25,width=220,height=45)

        HL_l2 = Label(HL,text=u"Kodunuzu yazın: ")
        HL_l2.place(relx=0.0,rely=0.40)

        self.HL_k = Text(HL)
        self.HL_k.place(relx=0.05,rely=0.50,width=220,height=145)

        HL_b = Button(HL,text=u"Ekle",command=self.hl_yap)
        HL_b.place(relx=0.6,rely=0.01)


    def hl_yap(self):
        #return self.metin.insert(END,"\n ..highlight:: %s "%(self.HL_a.get(1.0,END)))
        hl_aciklama_cek = self.HL_a.get(1.0,END)
        hl_kod_cek = self.HL_k.get(1.0,END)
        hl_sonuc = "\n ..highlight:: %s\n%s\n \t%s"%(self.diller[self.HL_d.get()],hl_aciklama_cek,hl_kod_cek)
        return self.metin.insert(END,hl_sonuc)

    ######################


    def numsuz_liste_p(self):
        nsz_list = Toplevel()
        nsz_list.title("RSTkinter - Liste")
        nsz_list.resizable(width=FALSE,height=FALSE)
        nsz_list.geometry("200x140")

        nsz_list_l = Label(nsz_list,text=u"Listenin eleman sayısı: ")
        nsz_list_l.place(relx=0.0,rely=0.0)

        self.nsz_list_a = Entry(nsz_list)
        self.nsz_list_a.place(relx=0.01,rely=0.20)

        nsz_list_b = Button(nsz_list,text=u"Ekle",command=self.numsuz_liste_yap)
        nsz_list_b.place(relx=0.7,rely=0.17)

    def numsuz_liste_yap(self):
        numsuz_liste_sayisi = self.nsz_list_a.get()
        try:
            numsuz_liste_sonuc = " * BURAYA_YAZ!\n"*int(numsuz_liste_sayisi)
        except ValueError:
            print u"Sadece sayı girin!!"
        except:
            print u"Sadece sayı girin!"

        return self.metin.insert(END,numsuz_liste_sonuc)

    ######################

    def liste_p(self):
        liste_ = Toplevel()
        liste_.title("RSTkinter - Liste No")
        liste_.resizable(width=FALSE,height=FALSE)
        liste_.geometry("200x140")

        liste_l = Label(liste_,text=u"Liste sayısı:")
        liste_l.place(relx=0.0,rely=0.0)

        self.liste_a = Entry(liste_)
        self.liste_a.place(relx=0.01,rely=0.20)

        liste_b = Button(liste_,text=u"Ekle",command=self.liste_yap)
        liste_b.place(relx=0.7,rely=0.17)


    def liste_yap(self):
        return self.metin.insert(END, "#. BURAYA_YAZ!\n"*int(self.liste_a.get()))

    #############

    def h1p(self):
        h1pp = Toplevel()
        h1pp.title("RSTkinter - Başlıklar")
        h1pp.resizable(width=FALSE,height=FALSE)
        h1pp.geometry("200x33")

        self.h1p_d = StringVar(h1pp)
        self.h1p_d.set(u"Başlık")

        self.h1k = Entry(h1pp)
        self.h1k.place(relx=0.38,rely=0.03,width=80)

        hhk = ["H1","H2","H3","H4","H5","H6","H7"]

        h1p_u = apply(OptionMenu,(h1pp,self.h1p_d)+tuple(hhk))
        h1p_u.place(relx=0.001,rely=0.0)

        h1e = Button(h1pp,text=u"Ekle",command=self.h1y)
        h1e.place(relx=0.8,rely=0.03)

    def h1y(self):
        if self.h1p_d.get() == "H1":
            return self.metin.insert(END,"\n"+"*"*len(self.h1k.get())+"\n"+self.h1k.get()+"\n"+"*"*len(self.h1k.get())+"\n")
        elif self.h1p_d.get() == "H2":
            return self.metin.insert(END,"\n"+self.h1k.get()+"\n"+"*"*len(self.h1k.get())+"\n")
        elif self.h1p_d.get() == "H3":
            return self.metin.insert(END,"\n"+self.h1k.get()+"\n"+"="*len(self.h1k.get())+"\n")
        elif self.h1p_d.get() == "H4":
            return self.metin.insert(END,"\n"+self.h1k.get()+"\n"+"-"*len(self.h1k.get())+"\n")
        elif self.h1p_d.get() == "H5":
            return self.metin.insert(END,"\n"+self.h1k.get()+"\n"+"."*len(self.h1k.get())+"\n")
        elif self.h1p_d.get() == "H6":
            return self.metin.insert(END,"\n"+self.h1k.get()+"\n"+"~"*len(self.h1k.get())+"\n")
        elif self.h1p_d.get() == "H7":
            return self.metin.insert(END,"\n"+self.h1k.get()+"\n"+"`"*len(self.h1k.get())+"\n")
        else:
            import tkMessageBox
            tkMessageBox.showwarning(u"RSTkinter - Başlık Hata",u"Lütfen bir başlık seçiniz!")
            del tkMessageBox

    #############

    def meta_p(self):
        metap = Toplevel()
        metap.title("RSTkinter - Meta")
        metap.resizable(width=FALSE,height=FALSE)
        metap.geometry("182x100")

        decripL = Label(metap,text=u"Açıklama:")
        decripL.place(relx=0.0,rely=0.01)

        self.decripE = Entry(metap)
        self.decripE.place(rely=0.01,relx=0.3)

        keywL = Label(metap,text=u"Tags:")
        keywL.place(rely=0.22,relx=0.0)

        self.keywE = Entry(metap)
        self.keywE.place(rely=0.22,relx=0.3)

        metap_e = Button(metap,text="Ekle",command=self.meta_y)
        metap_e.place(relx=0.8,rely=0.45)

    def meta_y(self):
        return self.metin.insert(0.0,"\n.. meta::\n\t:description: %s\n\t:keywords: %s\n"%(self.decripE.get(),self.keywE.get()))





pencere = Tk()
rst = RSTkinter()

mainloop()