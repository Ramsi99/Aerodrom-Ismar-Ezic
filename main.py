import sqlite3
from datetime import datetime

#Admin
class Admin:
    def __init__(self, id_admin, ime_admin, prezime_admin, username_admin, password_admin, role_admin):
        self.id_admin = id_admin
        self.ime_admin = ime_admin
        self.prezime_admin = prezime_admin
        self.username_admin = username_admin
        self.password_admin = password_admin
        self.role_admin = "A"

    #Hardcode prvog admina
    def prviAdmin(self):
        connection = sqlite3.connect('aerodrom.db')
        cursor = connection.cursor()

        cursor.execute("INSERT INTO admin (ime_admin, prezime_admin, username_admin, password_admin, role_admin) VALUES ('Ismar', 'Ezic', 'Ramsi99', '1234', 'A')")

        connection.commit()
        connection.close()


    #ADMIN
    def registerAdmin(self):
        connection = sqlite3.connect('aerodrom.db')
        cursor = connection.cursor()

        ime_admin = input("Unesite ime novog admina: ")
        prezime_admin = input("Unesite prezime novog admina: ")
        username_admin = input("Unesite username novog admina: ")
        password_admin = input("Unesite password novog admina: ")
        role_admin = 'A'

        a = Admin(None, ime_admin, prezime_admin, username_admin, password_admin, 'A')

        cursor.execute(f"SELECT * FROM admin WHERE username_admin = '{username_admin}'")
        postojeci_admin = cursor.fetchone()

        while postojeci_admin is not None:
            print("Username je zauzet, pokušajte ponovo\n ")
            username_admin = input("Unesite username novog admina: ")
            cursor.execute(f"SELECT * FROM admin WHERE username_admin = '{username_admin}'")
            postojeci_admin = cursor.fetchone()

        cursor.execute("INSERT INTO admin (ime_admin, prezime_admin, username_admin, password_admin, role_admin) VALUES (?, ?, ?, ?, ?)", (ime_admin, prezime_admin, username_admin, password_admin, role_admin))
        print("Uspješno ste dodali admina! \n ")

        connection.commit()
        connection.close()


    def ispisAdmin(self):
        connection = sqlite3.connect('aerodrom.db')
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM admin")
        ispis = cursor.fetchall()
        print(f"Lista Admina: \n {ispis}")

    def updateAdmin(self, id_admin, new_ime_admin, new_prezime_admin, new_username_admin, new_password_admin):
        connection = sqlite3.connect('aerodrom.db')
        cursor = connection.cursor()


        cursor.execute("UPDATE admin SET ime_admin = ?, prezime_admin = ?, username_admin = ?, password_admin = ? WHERE id_admin = ?", (new_ime_admin, new_prezime_admin, new_username_admin, new_password_admin, id_admin))

        connection.commit()
        connection.close()

    def obrisiAdmin(self, id_admin):
        connection = sqlite3.connect('aerodrom.db')
        cursor = connection.cursor()

        cursor.execute(f"SELECT * FROM admin WHERE id_admin = ?", (id_admin,))
        admin = cursor.fetchone()

        if admin:
            cursor.execute("DELETE FROM admin WHERE id_admin = ?", (id_admin,))
        else:
            print("Ne postoji admin sa tim ID-em\n ")

        connection.commit()
        connection.close()

#User
class User:
    def __init__(self, id_user, ime_user, prezime_user, tezina_prtljage_user, klasa_user, username_user, password_user, role_user):
        self.id_user = id_user
        self.ime_user = ime_user
        self.prezime_user = prezime_user
        self.tezina_prtljage_user = tezina_prtljage_user
        self.klasa_user = klasa_user
        self.role_user = role_user

        self.username_user = username_user
        self.password_user = password_user


    def registerUserasAdmin(self):
        connection = sqlite3.connect('aerodrom.db')
        cursor = connection.cursor()

        ime_user = input("Unesite ime usera: ")
        prezime_user = input("Prezime usera: ")
        tezina_prtljage_user = ""
        klasa_user = ""
        username_user = input("Unesite username usera: ")
        password_user = input("Unesite password usera: ")
        role_user = 'P'

        cursor.execute("INSERT INTO user (ime_user, prezime_user, tezina_prtljage_user, klasa_user, username_user, password_user, role_user) VALUES (?, ?, ?, ?, ?, ?, ?)", (ime_user, prezime_user, tezina_prtljage_user, klasa_user, username_user, password_user, role_user))
        print("Uspješno ste dodali usera! \n ")
        connection.commit()
        connection.close()

    def ispisUserasAdmin(self):
        connection = sqlite3.connect('aerodrom.db')
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM user")
        ispis = cursor.fetchall()
        print(f"Lista Usera: \n {ispis}")

    def updateUserasAdmin(self, new_ime_user, new_prezime_user, new_klasa_user, new_username_user, new_password_user, id_user):
        connection = sqlite3.connect('aerodrom.db')
        cursor = connection.cursor()

        cursor.execute("UPDATE user SET ime_user = ?, prezime_user = ?, klasa_user = ?, username_user = ?, password_user = ? WHERE id_user = ?", (new_ime_user, new_prezime_user, new_klasa_user, new_username_user, new_password_user, id_user))

        connection.commit()
        connection.close()

    def obrisiUserasAdmin(self, id_user):
        connection = sqlite3.connect('aerodrom.db')
        cursor = connection.cursor()

        cursor.execute(f"SELECT * FROM user WHERE id_user = ?", (id_user,))
        obrisi_user = cursor.fetchone()

        if obrisi_user:
            cursor.execute(f"DELETE FROM user WHERE id_user = ?", (id_user,))
            print("User je uspješno obrisan ")

        else:
            print("User s tim ID-em ne postoji")

        connection.commit()
        connection.close()

#Pilot
class Pilot:
    def __init__(self, id_pilot, ime_pilot, prezime_pilot, broj_letova_pilot, plata_pilot):
        self.id_pilot = id_pilot
        self.ime_pilot = ime_pilot
        self.prezime_pilot = prezime_pilot
        self.broj_letova_pilot = broj_letova_pilot
        self.plata_pilot = plata_pilot


    def registerPilot(self):
        connection = sqlite3.connect('aerodrom.db')
        cursor = connection.cursor()

        ime_pilot = input("Unesite ime novog pilota: ")
        prezime_pilot = input("Unesite prezime novog pilota: ")
        broj_letova_pilot = int(input("Unesite broj letova novog pilota: "))
        plata_pilot = int(input("Unesite platu pilota: "))

        p = Pilot(None, ime_pilot, prezime_pilot, broj_letova_pilot, plata_pilot)

        cursor.execute("INSERT INTO pilot (ime_pilot, prezime_pilot, broj_letova_pilot, plata_pilot) VALUES (?, ?, ?, ?)",(ime_pilot, prezime_pilot, broj_letova_pilot, plata_pilot))
        print("Uspješno ste dodali pilota! \n")

        connection.commit()
        connection.close()


    def ispisPilot(self):
        connection = sqlite3.connect('aerodrom.db')
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM pilot")
        ispis = cursor.fetchall()
        print(f"Lista Pilota: \n {ispis}")

    def updatePilot(self, id_pilot, new_ime_pilot, new_prezime_pilot, new_broj_letova_pilot, new_plata_pilot):
        connection = sqlite3.connect('aerodrom.db')
        cursor = connection.cursor()

        cursor.execute("UPDATE pilot SET ime_pilot = ?, prezime_pilot = ?, broj_letova_pilot = ?, plata_pilot = ? WHERE id_pilot = ?", (new_ime_pilot, new_prezime_pilot, new_broj_letova_pilot, new_plata_pilot, id_pilot))

        connection.commit()
        connection.close()

    def obrisiPilot(self, id_pilot):
        connection = sqlite3.connect('aerodrom.db')
        cursor = connection.cursor()

        cursor.execute(f"SELECT * FROM pilot WHERE id_pilot = ?", (id_pilot,))
        pilot = cursor.fetchone()

        if pilot:
            cursor.execute("DELETE FROM pilot WHERE id_pilot = ?", (id_pilot,))
            print("Pilot je uspješno obrisan ")
        else:
            print("Ne postoji pilot s tim ID-em")

        connection.commit()
        connection.close()

#Stjuardesa
class Stjuardesa:
    def __init__(self, id_stjuardesa, ime_stjuardesa, prezime_stjuardesa, plata_stjuardesa):
        self.id_stjuardesa = id_stjuardesa
        self.ime_stjuardesa = ime_stjuardesa
        self.prezime_stjuardesa = prezime_stjuardesa
        self.plata_stjuardesa = plata_stjuardesa



    def registerStjuardesa(self):
        connection = sqlite3.connect('aerodrom.db')
        cursor = connection.cursor()

        ime_stjuardesa = input("Unesite ime nove stjuardese: ")
        prezime_stjuardesa = input("Unesite prezime nove stjuardese: ")
        plata_stjuardesa = int(input("Unesite platu nove stjuardese: "))


        s = Stjuardesa(None, ime_stjuardesa, prezime_stjuardesa, plata_stjuardesa)


        cursor.execute("INSERT INTO stjuardesa (ime_stjuardesa, prezime_stjuardesa, plata_stjuardesa) VALUES (?, ?, ?)", (ime_stjuardesa, prezime_stjuardesa, plata_stjuardesa))
        print("Uspješno ste dodali stjuardesu! \n ")

        connection.commit()
        connection.close()

    def ispisStjuardesa(self):
        connection = sqlite3.connect('aerodrom.db')
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM stjuardesa")
        ispis = cursor.fetchall()
        print(f"Lista Stjuardesa: \n {ispis}")

    def updateStjuardesa(self, id_stjuardesa, new_ime_stjuardesa, new_prezime_stjuardesa, new_plata_stjuardesa):
        connection = sqlite3.connect('aerodrom.db')
        cursor = connection.cursor()

        cursor.execute("UPDATE stjuardesa SET ime_stjuardesa = ?, prezime_stjuardesa = ?, plata_stjuardesa = ? WHERE id_stjuardesa = ?", (new_ime_stjuardesa, new_prezime_stjuardesa, new_plata_stjuardesa, id_stjuardesa))

        connection.commit()
        connection.close()

    def obrisiStjuardesa(self, id_stjuardesa):
        connection = sqlite3.connect('aerodrom.db')
        cursor = connection.cursor()

        cursor.execute(f"SELECT * FROM stjuardesa WHERE id_stjuardesa = ?", (id_stjuardesa,))
        pilot = cursor.fetchone()

        if pilot:
            cursor.execute("DELETE FROM stjuardesa WHERE id_stjuardesa = ?", (id_stjuardesa,))
            print("Stjuardesa je uspješno obrisana \n")
        else:
            print("Ne postoji stjuardesa s tim ID-em \n")

        connection.commit()
        connection.close()

#Avion
class Avion:
    def __init__(self, id_avion, model_avion, broj_sjedista_avion):
        self.id_avion = id_avion
        self.model_avion = model_avion
        self.broj_sjedista_avion = broj_sjedista_avion

    def registerAvion(self):
        connection = sqlite3.connect('aerodrom.db')
        cursor = connection.cursor()

        model_avion = input("Unesite model aviona: ")
        broj_sjedista_avion = int(input("Unesite broj sjedišta aviona: "))


        cursor.execute("INSERT INTO avion (model_avion, broj_sjedista_avion) VALUES (?, ?)", (model_avion, broj_sjedista_avion))
        print("Uspješno ste dodali avion! ")

        connection.commit()
        connection.close()

    def ispisAvion(self):
        connection = sqlite3.connect('aerodrom.db')
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM avion")
        ispis = cursor.fetchall()
        print(f"Lista Aviona: \n {ispis}")

    def updateAvion(self, id_avion, new_model_avion, new_broj_sjedista_avion):
        connection = sqlite3.connect('aerodrom.db')
        cursor = connection.cursor()

        cursor.execute("UPDATE avion SET model_avion = ?, broj_sjedista_avion = ? WHERE id_avion = ?", (new_model_avion, new_broj_sjedista_avion, id_avion))

        connection.commit()
        connection.close()

    def obrisiAvion(self, id_avion):
        connection = sqlite3.connect('aerodrom.db')
        cursor = connection.cursor()

        cursor.execute(f"SELECT * FROM pilot WHERE id_avion = ?", (id_avion,))
        pilot = cursor.fetchone()

        if pilot:
            cursor.execute("DELETE FROM avion WHERE id_avion = ?", (id_avion,))
            print("Avion je uspješno obrisan ")
        else:
            print("Ne postoji avion s tim ID-em \n")

        connection.commit()
        connection.close()

#Let
class Let:
    def __init__(self, id_let, cijena_karte_let, destinacija_let, vrijeme_let, datum_let, id_avion):
        self.id_let = id_let
        self.cijena_karte_let = cijena_karte_let
        self.destinacija_let = destinacija_let
        self.datum_let = datum_let
        self.vrijeme_let = vrijeme_let
        self.id_avion = id_avion

    def registerLet(self):
        connection = sqlite3.connect('aerodrom.db')
        cursor = connection.cursor()

        cijena_karte_let = int(input("Unesite cijenu karte: "))
        destinacija_let = input("Unesite destinaciju leta: ")

        datum_let = input("Unesite datum leta (dd.mm.gggg.): ")
        datum_let = datetime.strptime(datum_let, "%d.%m.%Y").date()
        datum_let_str = datum_let.strftime("%Y-%m-%d")

        vrijeme_let = input("Unesite vrijeme leta (SS:MM) :")
        vrijeme_let = datetime.strptime(vrijeme_let, "%H:%M").time()
        vrijeme_let_str = vrijeme_let.strftime("%H:%M:%S")

        id_avion = int(input("Unesite ID aviona koji je na ovom letu "))

        cursor.execute("INSERT INTO let (cijena_karte_let, destinacija_let, datum_let, vrijeme_let, id_avion) VALUES (?, ?, ?, ?, ?)",(cijena_karte_let, destinacija_let, datum_let_str, vrijeme_let_str, id_avion))
        print("Uspješno ste dodali let! ")

        connection.commit()
        connection.close()

    def ispisLet(self):
        connection = sqlite3.connect('aerodrom.db')
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM let")
        ispis = cursor.fetchall()
        print(f"Lista Letova: \n")
        print(ispis)
        print("")

    def updateLet(self, id_let, new_cijena_karte_let, new_destinacija_let, new_datum_let_str, new_vrijeme_let_str, new_id_avion):
        connection = sqlite3.connect('aerodrom.db')
        cursor = connection.cursor()

        cursor.execute("UPDATE let SET cijena_karte_let = ?, destinacija_let = ?, datum_let = ?, vrijeme_let = ?, id_avion = ? WHERE id_let = ?", (new_cijena_karte_let, new_destinacija_let, new_datum_let_str, new_vrijeme_let_str, new_id_avion, id_let))

        connection.commit()
        connection.close()

    def obrisiLet(self, id_let):
        connection = sqlite3.connect('aerodrom.db')
        cursor = connection.cursor()

        cursor.execute(f"SELECT * FROM let WHERE id_let = ?", (id_let,))
        let = cursor.fetchone()

        if let:
            cursor.execute("DELETE FROM let WHERE id_let = ?", (id_let,))
            print("Let je uspješno obrisan ")
        else:
            print("Ne postoji let s tim ID-em")

        connection.commit()
        connection.close()

#Gate
class Gate:
    def __init__(self, id_gate, broj_gate):
        self.id_gate = id_gate
        self.broj_gate = broj_gate


    def registerGate(self):
        connection = sqlite3.connect('aerodrom.db')
        cursor = connection.cursor()

        broj_gate = input("Unesite broj gate-a: ")
        g = Gate(None, broj_gate)
        print("")


        cursor.execute("INSERT INTO gate (broj_gate) VALUES ( ? )", (broj_gate,))
        print("Uspješno ste dodali gate! ")

        connection.commit()
        connection.close()

    def ispisGate(self):
        connection = sqlite3.connect('aerodrom.db')
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM gate")
        ispis = cursor.fetchall()
        print(f"Lista Gateova: \n {ispis}")


    def updateGate(self, id_gate, new_broj_gate):
        connection = sqlite3.connect('aerodrom.db')
        cursor = connection.cursor()

        cursor.execute("UPDATE gate SET broj_gate = ? WHERE id_gate = ?", (new_broj_gate, id_gate))

        connection.commit()
        connection.close()

    def obrisiGate(self, id_gate):
        connection = sqlite3.connect('aerodrom.db')
        cursor = connection.cursor()

        cursor.execute(f"SELECT * FROM gate WHERE id_gate = ?", (id_gate,))
        pilot = cursor.fetchone()

        if pilot:
            cursor.execute("DELETE FROM gate WHERE id_gate = ?", (id_gate,))
            print("Gate je uspješno obrisan ")
        else:
            print("Ne postoji gate s tim ID-em")

        connection.commit()
        connection.close()

#Security
class Security:
    def __init__(self, id_security, ime_security, prezime_security, plata_security, id_gate):
        self.id_security = id_security
        self.ime_security = ime_security
        self.prezime_security = prezime_security
        self.plata_security = plata_security
        self.id_gate = id_gate

    def registerSecurity(self):
        connection = sqlite3.connect('aerodrom.db')
        cursor = connection.cursor()

        ime_security = input("Unesite ime novog securitya : ")
        prezime_security = input("Unesite prezime novog securitya: ")
        plata_security = int(input("Unesite platu securitya: "))
        id_gate = int(input("Unesite ID gate-a na kojem radi ovaj security: "))

        s = Security(None, ime_security, prezime_security, plata_security, id_gate)

        cursor.execute("INSERT INTO security (ime_security, prezime_security, plata_security, id_gate) VALUES (?, ?, ?, ?)",(ime_security, prezime_security, plata_security, id_gate))
        print("Uspješno ste dodali securitya! ")

        connection.commit()
        connection.close()


    def ispisSecurity(self):
        connection = sqlite3.connect('aerodrom.db')
        cursor = connection.cursor()

        cursor.execute("SELECT * FROM security")
        ispis = cursor.fetchall()
        print(f"Lista Securitya: \n {ispis}")

    def updateSecurity(self, id_security, new_ime_security, new_prezime_security, new_plata_security, new_id_gate):
        connection = sqlite3.connect('aerodrom.db')
        cursor = connection.cursor()

        cursor.execute("UPDATE security SET ime_security = ?, prezime_security = ?, plata_security = ?, id_gate = ? WHERE id_security = ?", (new_ime_security, new_prezime_security, new_plata_security, new_id_gate, id_security))

        connection.commit()
        connection.close()

    def obrisiSecurity(self, id_security):
        connection = sqlite3.connect('aerodrom.db')
        cursor = connection.cursor()

        cursor.execute(f"SELECT * FROM security WHERE id_security = ?", (id_security,))
        pilot = cursor.fetchone()

        if pilot:
            cursor.execute("DELETE FROM security WHERE id_security = ?", (id_security,))
            print("Security je uspješno obrisan ")
        else:
            print("Ne postoji Security s tim ID-em")

        connection.commit()
        connection.close()


#Baza podataka
def BazaAerodrom():

   connection = sqlite3.connect('aerodrom.db')
   cursor = connection.cursor()

   #Tabela admin
   cursor.execute('''
        CREATE TABLE admin(
        id_admin INTEGER PRIMARY KEY AUTOINCREMENT,
        ime_admin VARCHAR(20),
        prezime_admin VARCHAR(20),
        username_admin VARCHAR(20) UNIQUE,
        password_admin VARCHAR(20),
        role_admin CHAR(1)
   )'''
  )


   # Tabela user
   cursor.execute('''
        CREATE TABLE user(
        id_user INTEGER PRIMARY KEY AUTOINCREMENT,
        ime_user VARCHAR(20),
        prezime_user VARCHAR(30),
        tezina_prtljage_user INTEGER,
        klasa_user INTEGER,
        username_user VARCHAR(20) UNIQUE,
        password_user VARCHAR(20),
        role_user CHAR(1)
        )'''
   )

   # Tabela pilot
   cursor.execute('''
       CREATE TABLE pilot(
       id_pilot INTEGER PRIMARY KEY AUTOINCREMENT,
       ime_pilot VARCHAR(20),
       prezime_pilot VARCHAR(30),
       broj_letova_pilot INTEGER,
       plata_pilot INTEGER
   )'''
   )

   # Tabela  stjuardesa
   cursor.execute('''
        CREATE TABLE stjuardesa(
        id_stjuardesa INTEGER PRIMARY KEY AUTOINCREMENT,
        ime_stjuardesa VARCHAR(20),
        prezime_stjuardesa VARCHAR(30),
        plata_stjuardesa INTEGER
   )'''
    )

   # Tabela avion
   cursor.execute('''
       CREATE TABLE avion(
       id_avion INTEGER PRIMARY KEY AUTOINCREMENT,
       model_avion VARCHAR(20),
       broj_sjedista_avion INTEGER
   )'''
    )

   # Tabela let
   cursor.execute('''
        CREATE TABLE let(
        id_let INTEGER PRIMARY KEY AUTOINCREMENT,
        cijena_karte_let INTEGER,
        destinacija_let VARCHAR(30),
        datum_let DATE,
        vrijeme_let DATETIME,
        id_avion INTEGER,
        FOREIGN KEY (id_avion) REFERENCES avion(id_avion)
   )'''
     )

   # Tabela gate
   cursor.execute('''
        CREATE TABLE gate(
        id_gate INTEGER PRIMARY KEY AUTOINCREMENT,
        broj_gate VARCHAR(20)
   )'''
    )

    # Tabela security
   cursor.execute('''
        CREATE TABLE security(
        id_security INTEGER PRIMARY KEY AUTOINCREMENT,
        ime_security VARCHAR(20),
        prezime_security VARCHAR(30),
        plata_security INTEGER,
        id_gate INTEGER,
        FOREIGN KEY (id_gate) REFERENCES gate(id_gate)
   )'''
   )

    # Tabela M:N user - let
   cursor.execute('''
            CREATE TABLE karta(
            id_karta INTEGER PRIMARY KEY AUTOINCREMENT,
            id_user INTEGER,
            id_let INTEGER,
            FOREIGN KEY (id_user) REFERENCES user(id_user),
            FOREIGN KEY (id_let) REFERENCES let(id_let)
       )'''
        )

   # Tabela M:N pilot - let
   cursor.execute('''
        CREATE TABLE pilot_let(
        id_pilot_let INTEGER PRIMARY KEY AUTOINCREMENT,
        id_pilot INTEGER,
        id_let INTEGER,
        FOREIGN KEY (id_pilot) REFERENCES pilot(id_pilot),
        FOREIGN KEY (id_let) REFERENCES let(id_let)
    )'''
    )

   # Tabela M:N stjuardesa - let
   cursor.execute('''
        CREATE TABLE stjuardesa_let(
        id_stjuardesa_let INTEGER PRIMARY KEY AUTOINCREMENT,
        id_stjuardesa INTEGER,
        id_let INTEGER,
        FOREIGN KEY (id_stjuardesa) REFERENCES stjuardesa(id_stjuardesa),
        FOREIGN KEY (id_let) REFERENCES let(id_let)
   )'''
   )

    # Tabela M:N gate-let
   cursor.execute('''
   CREATE TABLE pista(
   id_pista INTEGER PRIMARY KEY AUTOINCREMENT,
   id_gate INTEGER,
   id_let INTEGER,
   FOREIGN KEY (id_gate) REFERENCES gate(id_gate),
   FOREIGN KEY (id_let) REFERENCES let(id_let)
   )'''
    )

   connection.commit()
   connection.close()


#admin komande
def adminKomande():
        connection = sqlite3.connect('aerodrom.db')
        cursor = connection.cursor()

        print("1. Tabela -> Admin\n2. Tabela -> User\n3. Tabela -> Pilot\n4. Tabela -> Stjuardesa\n5. Tabela -> Avion\n6. Tabela -> Security\n7. Tabela -> Gate\n8. Tabela -> Let\n9. Tabela -> Pilot-Let\n10. Tabela -> Stjuardesa-Let\n11. Tabela -> Gate-Let\n12. Tabela -> User-Let\n13.-> Prikaz svih letova\n14.-> Prikaz rezervisanih karata\n15.-> Odjava ")
        izbor_tabele = int(input("Odaberite kojom tabelom želite manipulisati: "))


        #admin
        if izbor_tabele == 1:

            print("0.-> Stopirajte program\n1.-> Registrujte admina\n2.-> Ispišite sve admine\n3.-> Ažurirajte podatke o adminu\n4.-> Obrišite admina iz baze\n5.-> Povratak na odabir tabele ")
            izbor_komande = int(input("Odaberite komandu nad tabelom "))

            while True:
                if izbor_komande == 1:
                    admin_obj.registerAdmin()
                    print("\n")

                elif izbor_komande == 2:
                    print("")
                    print("(ID admin), (Ime), (Prezime), (Username), (Password), (Role)")
                    admin_obj.ispisAdmin()
                    print("\n")

                elif izbor_komande == 3:
                    id_admin = int(input("Unesite ID admina kojeg želite ažurirati: "))
                    a = Admin(id_admin, "", "", "", "", 'A')
                    new_ime_admin = input("Ažurirajte ime admina: ")
                    new_prezime_admin = input("Ažurirajte prezime admina: ")
                    new_username_admin = input("Ažurirajte username admina: ")
                    new_password_admin = input("Ažurirajte password admina: ")
                    a.updateAdmin(id_admin, new_ime_admin, new_prezime_admin, new_username_admin, new_password_admin)
                    print("\n")

                elif izbor_komande == 4:
                    id_obrisi_admin = int(input("Unesite ID admina kojeg želite obrisati: "))
                    a = Admin(0, "", "", "", "", "A")
                    a.obrisiAdmin(id_obrisi_admin)
                    print("Uspješno ste obrisali admin-a \n")

                elif izbor_komande == 5:
                    adminKomande()
                    print("\n")

                elif izbor_komande == 0:
                    print("Kraj programa \n")
                    break

                else:
                    print("Greška! Izbor komandi mora biti od 1 do 5 \n")
                    break

                izbor_komande = int(input("Odaberite komandu nad tabelom: "))

        #user
        elif izbor_tabele == 2:

            print("0.-> Stopirajte program\n1.-> Registrujte usera\n2.-> Ispišite sve usere\n3.-> Ažurirajte podatke usera\n4.-> Obrišite usera iz baze\n5.-> Povratak na odabir tabele ")
            izbor_komande = int(input("Izaberite komandu nad tabelom User: "))

            while True:
                if izbor_komande == 1:
                    user_obj.registerUserasAdmin()
                    print("\n")

                elif izbor_komande == 2:
                    print("")
                    print("(ID user), (Ime), (Prezime), (Tezina Prtljage), (Klasa), (Username), (Password), (Role)")
                    user_obj.ispisUserasAdmin()
                    print("\n")

                elif izbor_komande == 3:
                    id_user = int(input("Unesite ID usera kojeg želite ažurirati: "))
                    u = User(id_user, "", "", "", "", "", "", 'A')
                    new_ime_admin = input("Ažurirajte ime usera: ")
                    new_prezime_user = input("Ažurirajte prezime usera: ")
                    new_klasa_user = int(input("Unesite klasu usera: "))
                    new_username_user = input("Ažurirajte username usera: ")
                    new_password_user = input("Ažurirajte password usera: ")
                    u.updateUserasAdmin(new_ime_admin, new_prezime_user, new_klasa_user, new_username_user, new_password_user, id_user)
                    print("\n")


                elif izbor_komande == 4:
                    id_obrisi_user = int(input("Unesite ID usera kojeg zelite obrisati: "))
                    u = User(0, "", "", "", "", "", "", 'P')
                    u.obrisiUserasAdmin(id_obrisi_user)
                    print("Uspješno ste obrisali user-a\n")

                elif izbor_komande == 5:
                    adminKomande()
                    print("\n")

                elif izbor_komande == 0:
                    print("Kraj programa \n")
                    break

                else:
                    print("Greška! Izbor komandi mora biti od 1 do 5 \n")
                    break

                izbor_komande = int(input("Odaberite komandu nad tabelom: "))

        #pilot
        elif izbor_tabele == 3:

            print("0.-> Stopirajte program\n1.-> Registrujte pilota\n2.-> Ispišite sve pilote\n3.-> Ažurirajte podatke pilota\n4.-> Obrišite pilota iz baze\n5.-> Povratak na odabir tabele ")
            izbor_komande = int(input("Izaberite komandu nad tabelom Pilot: "))

            while True:
                if izbor_komande == 1:
                    pilot_obj.registerPilot()
                    print("\n")

                elif izbor_komande == 2:
                    print("")
                    print("(ID pilot), (Ime), (Prezime), (Broj letova), (Plata)")
                    pilot_obj.ispisPilot()
                    print("\n")

                elif izbor_komande == 3:
                    id_pilot = int(input("Unesite ID pilota kojeg želite ažurirati: "))
                    p = Pilot(id_pilot, "", "", "", "",)
                    new_ime_pilot = input("Ažurirajte ime pilota: ")
                    new_prezime_pilot = input("Ažurirajte prezime pilota: ")
                    new_broj_letova_pilot = input("Ažurirajte broj letova pilota: ")
                    new_plata_pilot = input("Ažurirajte platu pilota: ")
                    p.updatePilot(id_pilot, new_ime_pilot, new_prezime_pilot, new_broj_letova_pilot, new_plata_pilot)
                    print("\n")

                elif izbor_komande == 4:
                    id_pilot = int(input("Unesite ID pilota kojeg žeite obrisati: "))
                    p = Pilot(0, "", "", "", "")
                    p.obrisiPilot(id_pilot)
                    print("Uspješno ste obrisali pilot-a\n")

                elif izbor_komande == 5:
                    adminKomande()
                    print("\n")

                elif izbor_komande == 0:
                    print("Kraj programa \n")
                    break

                else:
                    print("Greška! Izbor komandi mora biti od 1 do 5 \n")
                    break

                izbor_komande = int(input("Odaberite komandu nad tabelom: "))

        #stjuardesa
        elif izbor_tabele == 4:

            print("0.-> Stopirajte program\n1.-> Registrujte stjuardesu\n2.-> Ispišite sve stjuardese\n3.-> Ažurirajte podatke stjuardese\n4.-> Obrišite stjuardesu iz baze\n5.-> Povratak na odabir tabele ")
            izbor_komande = int(input("Izaberite komandu nad tabelom Stjuardesa: "))

            while True:
                if izbor_komande == 1:
                    stjuardesa_obj.registerStjuardesa()
                    print("\n")

                elif izbor_komande == 2:
                    print("")
                    print("(ID stjuardesa), (Ime), (Prezime), (Plata)")
                    stjuardesa_obj.ispisStjuardesa()
                    print("\n")

                elif izbor_komande == 3:
                    id_stjuardesa = int(input("Unesite ID stjuardese koju želite ažurirati: "))
                    s = Stjuardesa(id_stjuardesa, "", "", "")
                    new_ime_stjuardesa = input("Ažurirajte ime stjuardese: ")
                    new_prezime_pilot = input("Ažurirajte prezime stjuardese: ")
                    new_plata_stjuardesa = input("Ažurirajte platu stjuardese: ")
                    s.updateStjuardesa(id_stjuardesa, new_ime_stjuardesa, new_prezime_pilot, new_plata_stjuardesa)
                    print("Uspješno ste ažurirali stjuardesu!\n")

                elif izbor_komande == 4:
                    id_stjuardesa = int(input("Unesite ID stjuardese koju žeite obrisati: "))
                    s = Stjuardesa(0, "", "", "")
                    s.obrisiStjuardesa(id_stjuardesa)
                    print("Uspješno ste obrisali stjuardesu\n ")

                elif izbor_komande == 5:
                    adminKomande()
                    print("\n")

                elif izbor_komande == 0:
                    print("Kraj programa \n")
                    break

                else:
                    print("Greška! Izbor komandi mora biti od 1 do 5 \n")
                    break

                izbor_komande = int(input("Odaberite komandu nad tabelom: "))

        #avion
        elif izbor_tabele == 5:
            print("0.-> Stopirajte program\n1.-> Registrujte avion\n2.-> Ispišite listu svih aviona\n3.-> Ažurirajte podatke o avionu\n4.-> Obrišite avion iz baze\n5.-> Povratak na odabir tabele ")
            izbor_komande = int(input("Izaberite komandu nad tabelom Avion: "))

            while True:
                if izbor_komande == 1:
                    avion_obj.registerAvion()
                    print("\n")

                elif izbor_komande == 2:
                    print("")
                    print("(ID avion), (Model Aviona), (Broj sjedišta)")
                    avion_obj.ispisAvion()
                    print("\n")

                elif izbor_komande == 3:
                    id_avion = int(input("Unesite ID aviona kojeg želite ažurirati: "))
                    a = Avion(id_avion, "", "")
                    new_model_avion = input("Ažurirajte model aviona: ")
                    new_broj_sjedista_avion = int(input("Ažurirajte broj sjedista aviona:  "))
                    a.updateAvion(id_avion, new_model_avion, new_broj_sjedista_avion)
                    print("Uspješno ste ažurirali avion! \n")

                elif izbor_komande == 4:
                    id_avion = int(input("Unesite ID aviona koju žeite obrisati \n "))
                    a = Avion(0, "", "")
                    a.obrisiAvion(id_avion)
                    print("Avion je uspješno obrisan \n")

                elif izbor_komande == 5:
                    adminKomande()
                    print("\n")

                elif izbor_komande == 0:
                    print("Kraj programa \n")
                    break

                else:
                    print("Greška! Izbor komandi mora biti od 1 do 5 \n")
                    break

                izbor_komande = int(input("Odaberite komandu nad tabelom: "))

        #security
        elif izbor_tabele == 6:

            print("0.-> Stopirajte program\n1.-> Registrujte security\n2.-> Ispišite sve securitye\n3.-> Ažurirajte podatke o securityu\n4.-> Obrišite securitya iz baze\n5.-> Povratak na odabir tabele ")
            izbor_komande = int(input("Izaberite komandu nad tabelom Security: "))

            while True:
                if izbor_komande == 1:
                    security_obj.registerSecurity()
                    print("\n")

                elif izbor_komande == 2:
                    print("")
                    print("(ID security), (Ime), (Prezime), (Plata), (Gate na kojem security radi)")
                    security_obj.ispisSecurity()
                    print("\n")

                elif izbor_komande == 3:
                    id_security = int(input("Unesite ID securitya kojeg želite ažurirati: "))
                    s = Security(id_security, "", "", "", "")
                    new_ime_security = input("Ažurirajte ime security: ")
                    new_prezime_security = input("Ažurirajte prezime securitya: ")
                    new_plata_security = input("Ažurirajte platu securitya: ")
                    new_id_gate = int(input("Ažurirajte ID gate-a na kojem security radi: "))
                    s.updateSecurity(id_security, new_ime_security, new_prezime_security, new_plata_security, new_id_gate)
                    print("Uspješno ste ažurirali securitya!\n")

                elif izbor_komande == 4:
                    id_security = int(input("Unesite ID securitya koju žeite obrisati: "))
                    s = Security(0, "", "", "", "")
                    s.obrisiSecurity(id_security)
                    print("\n")

                elif izbor_komande == 5:
                    adminKomande()
                    print("\n")

                elif izbor_komande == 0:
                    print("Kraj programa \n")
                    break

                else:
                    print("Greška! Izbor komandi mora biti od 1 do 5 \n")
                    break

                izbor_komande = int(input("Odaberite komandu nad tabelom: "))

        #gate
        elif izbor_tabele == 7:

            print("0.-> Stopirajte program\n1.-> Registrujte gate\n2.-> Ispišite sve gateove\n3.-> Ažurirajte podatke o gateu\n4.-> Obrišite gate iz baze\n5.-> Povratak na odabir tabele ")
            izbor_komande = int(input("Izaberite komandu nad tabelom Gate: "))

            while True:
                if izbor_komande == 1:
                    gate_obj.registerGate()

                elif izbor_komande == 2:
                    print("")
                    print("(ID gate), (Broj gate-a)")
                    gate_obj.ispisGate()

                elif izbor_komande == 3:
                    id_gate = int(input("Unesite ID gate-a kojeg želite ažurirati: "))
                    g = Gate(id_gate, "")
                    new_broj_gate = input("Ažurirajte broj gate-a: ")
                    g.updateGate(id_gate, new_broj_gate)
                    print("Uspješno ste ažurirali gate-a!")

                elif izbor_komande == 4:
                    id_gate = int(input("Unesite ID gate-a koju žeite obrisati: "))
                    g = Gate(0, "")
                    g.obrisiGate(id_gate)

                elif izbor_komande == 5:
                    adminKomande()

                elif izbor_komande == 0:
                    print("Kraj programa \n")
                    break

                else:
                    print("Greška! Izbor komandi mora biti od 1 do 5 \n")
                    break

                izbor_komande = int(input("Odaberite komandu nad tabelom: "))

        #let
        elif izbor_tabele == 8:

            print("0.-> Stopirajte program\n1.-> Registrujte let\n2.-> Ispišite sve letove\n3.-> Ažurirajte podatke o letu\n4.-> Obrišite let iz baze\n5.-> Povratak na odabir tabele ")
            izbor_komande = int(input("Izaberite komandu nad tabelom Let: "))

            while True:
                if izbor_komande == 1:
                    let_obj.registerLet()
                    print("\n")

                elif izbor_komande == 2:
                    print("")
                    print("(ID let), (Cijena karte), (Destinacija leta), (Datum leta), (Vrijeme leta)")
                    let_obj.ispisLet()
                    print("")

                elif izbor_komande == 3:
                    id_let = int(input("Unesite ID leta koji želite ažurirati: "))
                    l = Let(id_let, "", "", "", "", "")
                    new_cijena_karte_let = int(input("Ažurirajte cijenu leta: "))
                    new_destinacija_let = input("Ažurirajte destinaciju leta: ")

                    new_datum_let = input("Ažurirajte datum leta (dd.mm.gggg): ")
                    new_datum_let = datetime.strptime(new_datum_let, "%d.%m.%Y").date()
                    new_datum_let_str = new_datum_let.strftime("%Y-%m-%d")



                    new_vrijeme_let = input("Ažurirajte vrijeme leta: ")
                    new_vrijeme_let = datetime.strptime(new_vrijeme_let, "%H:%M").time()
                    new_vrijeme_let_str = new_vrijeme_let.strftime("%H:%M:%S")

                    new_id_avion = int(input("Ažurirajte ID aviona koji je na ovom letu: "))

                    l.updateLet(id_let, new_cijena_karte_let, new_destinacija_let, new_datum_let_str, new_vrijeme_let_str, new_id_avion)
                    print("Uspješno ste ažurirali let!\n")

                elif izbor_komande == 4:
                    id_let = int(input("Unesite ID leta koji žeite obrisati: "))
                    l = Let(0, "", "", "", "", "")
                    l.obrisiLet(id_let)

                elif izbor_komande == 5:
                    adminKomande()

                elif izbor_komande == 0:
                    print("Kraj programa \n")
                    break

                else:
                    print("Greška! Izbor komandi mora biti od 1 do 5 \n")
                    break

                izbor_komande = int(input("Odaberite komandu nad tabelom: "))

        #Pilot-Let (M:N)
        elif izbor_tabele == 9:

            print("0.-> Prekid programa\n1.-> Registrujte pilota na let\n2.-> Ispišite ID-pilota i ID-letova koji su povezani\n3.-> Ažurirajte kolonu pilot-let\n4.-> Obrišite kolonu pilot-let\n5.-> Povratak na odabir tabele ")
            izbor_komande = int(input("Izaberite komandu: "))

            #Registruj pilota i let
            while True:
                if izbor_komande == 1:
                    connection = sqlite3.connect('aerodrom.db')
                    cursor = connection.cursor()

                    id_pilot = int(input("Unesite ID pilota kojem želite dodijeliti let: "))
                    id_let = int(input("Unesite ID leta na koji želite postaviti pilota: "))

                    cursor.execute("SELECT * FROM pilot WHERE id_pilot = ?", (id_pilot,))
                    pilot = cursor.fetchone()

                    cursor.execute("SELECT * FROM let WHERE id_let = ?", (id_let,))
                    let = cursor.fetchone()

                    if pilot and let:
                        cursor.execute("INSERT INTO pilot_let (id_pilot, id_let) VALUES (?, ?)", (id_pilot, id_let))
                        print("Uspješno ste dodali pilota na let")

                    else:
                        print("Greška! Ne postoji pilot ili let sa ID-em koji ste unijeli ")
                    connection.commit()
                    connection.close()

                #ispis
                elif izbor_komande == 2:

                    connection = sqlite3.connect('aerodrom.db')
                    cursor = connection.cursor()

                    cursor.execute("SELECT * FROM pilot_let")

                    ispis = cursor.fetchall()
                    print("")
                    print("Svi ID-pilota i ID-letova: (ID red) (ID pilot), (ID let): ")
                    print(ispis)

                    connection.commit()
                    connection.close()

            #ažuriraj
                elif izbor_komande == 3:
                    connection = sqlite3.connect('aerodrom.db')
                    cursor = connection.cursor()

                    id_pilot_let = int(input("Unesite ID kolone koju želite ažurirati: "))


                    cursor.execute("SELECT * FROM pilot_let WHERE id_pilot_let = ?", (id_pilot_let,))

                    pilot_let = cursor.fetchone()

                    if pilot_let:
                        new_id_pilot = int(input("Ažurirajte ID pilota: "))
                        new_id_let = int(input("Ažurirajte ID leta: "))

                        cursor.execute("UPDATE pilot_let SET id_pilot = ?, id_let = ? WHERE id_pilot_let = ?", (new_id_pilot, new_id_let, id_pilot_let))
                        print("Uspješno ste ažurirali ID-eve ")
                    else:
                        print("Greška! Ne postoji kolona sa unešenim ID-em ")

                    connection.commit()
                    connection.close()

                #obriši
                elif izbor_komande == 4:
                    connection = sqlite3.connect('aerodrom.db')
                    cursor = connection.cursor()

                    id_pilot_let = int(input("Uneiste ID kolone koju želite obrisati: "))

                    cursor.execute("SELECT * FROM pilot_let WHERE id_pilot_let = ?", (id_pilot_let,))
                    pilot_let = cursor.fetchone()

                    if pilot_let:
                        cursor.execute("DELETE FROM pilot_let WHERE id_pilot_let = ?", (id_pilot_let,))
                        print("Uspješno ste obrisali kolonu sa unijetim ID-em ")

                    else:
                        print("Greška! Ne postoji kolona sa unijetim ID-em ")

                    connection.commit()
                    connection.close()

                elif izbor_komande == 5:
                    adminKomande()

                else:
                    print("Greška! Izbor komande mora biti od 1 do 4 ")

                print("")
                print("0.-> Prekid programa\n1.-> Registrujte pilota na let\n2.-> Ispišite ID-pilota i ID-letova koji su povezani\n3.-> Ažurirajte kolonu pilot-let\n4.-> Obrišite kolonu pilot-let\n5.-> Povratak na odabir tabele ")
                izbor_komande = int(input("Izaberite komandu: "))

        #Stjuardesa-Let (M:N)
        elif izbor_tabele == 10:

            print("0.-> Prekid programa\n1.-> Registrujte stjuardesu na let\n2.-> Ispišite ID-stjuardese i ID-letova koji su povezani\n3.-> Ažurirajte kolonu stjuardesa-let\n4.-> Obrišite kolonu stjuardesa-let\n5.-> Povratak na odabir tabele ")
            izbor_komande = int(input("Izaberite komandu: "))

            # Registruj stjuardesu na let
            while True:
                if izbor_komande == 1:
                    connection = sqlite3.connect('aerodrom.db')
                    cursor = connection.cursor()

                    id_stjuardesa = int(input("Unesite ID stjuardese kojoj želite dodijeliti let: "))
                    id_let = int(input("Unesite ID leta na koji želite postaviti stjuardesu: "))

                    cursor.execute("SELECT * FROM stjuardesa WHERE id_stjuardesa = ?", (id_stjuardesa,))
                    stjuardesa = cursor.fetchone()

                    cursor.execute("SELECT * FROM let WHERE id_let = ?", (id_let,))
                    let = cursor.fetchone()

                    if stjuardesa and let:
                        cursor.execute("INSERT INTO stjuardesa_let (id_stjuardesa, id_let) VALUES (?, ?)", (id_stjuardesa, id_let))
                        print("Uspješno ste dodali stjuardesu na let")

                    else:
                        print("Greška! Ne postoji stjuardesa ili let sa ID-em koji ste unijeli ")
                    connection.commit()
                    connection.close()

                # ispis
                elif izbor_komande == 2:

                    connection = sqlite3.connect('aerodrom.db')
                    cursor = connection.cursor()

                    cursor.execute("SELECT * FROM stjuardesa_let")

                    ispis = cursor.fetchall()
                    print("")
                    print("Svi ID-stjuardesa i ID-letova: (ID red) (ID stjuardesa), (ID let): ")
                    print(ispis)

                    connection.commit()
                    connection.close()

                # ažuriraj
                elif izbor_komande == 3:
                    connection = sqlite3.connect('aerodrom.db')
                    cursor = connection.cursor()

                    id_stjuardesa_let = int(input("Unesite ID kolone koju želite ažurirati: "))

                    cursor.execute("SELECT * FROM stjuardesa_let WHERE id_stjuardesa_let = ?", (id_stjuardesa_let,))

                    stjuardesa_let = cursor.fetchone()

                    if stjuardesa_let:
                        new_id_stjuardesa = int(input("Ažurirajte ID pilota: "))
                        new_id_let = int(input("Ažurirajte ID leta: "))

                        cursor.execute("UPDATE stjuardesa_let SET id_stjuardesa = ?, id_let = ? WHERE id_stjuardesa_let = ?", (new_id_stjuardesa, new_id_let, id_stjuardesa_let))
                        print("Uspješno ste ažurirali ID-eve ")
                    else:
                        print("Greška! Ne postoji kolona sa unešenim ID-em ")

                    connection.commit()
                    connection.close()

                # obriši
                elif izbor_komande == 4:
                    connection = sqlite3.connect('aerodrom.db')
                    cursor = connection.cursor()

                    id_stjuardesa_let = int(input("Uneiste ID kolone koju želite obrisati: "))

                    cursor.execute("SELECT * FROM stjuardesa_let WHERE id_stjuardesa_let = ?", (id_stjuardesa_let,))
                    pilot_let = cursor.fetchone()

                    if pilot_let:
                        cursor.execute("DELETE FROM stjuardesa_let WHERE id_stjuardesa_let = ?", (id_stjuardesa_let,))
                        print("Uspješno ste obrisali kolonu sa unijetim ID-em ")

                    else:
                        print("Greška! Ne postoji kolona sa unijetim ID-em ")

                    connection.commit()
                    connection.close()

                elif izbor_komande == 5:
                    adminKomande()

                else:
                    print("Greška! Izbor komande mora biti od 1 do 4 ")

                print("")
                print("0.-> Prekid programa\n1.-> Registrujte stjuardesu na let\n2.-> Ispišite ID-stjuardese i ID-letova koji su povezani\n3.-> Ažurirajte kolonu stjuardesa-let\n4.-> Obrišite kolonu stjuardesa-let\n5.-> Povratak na odabir tabele ")
                izbor_komande = int(input("Izaberite komandu: "))

        #Gate-Let (M:N)
        elif izbor_tabele == 11:
            print("0.-> Prekid programa\n1.-> Dodijelite gate-u let\n2.-> Ispišite ID-gateova i ID-letova koji su povezani\n3.-> Ažurirajte kolonu gate-let\n4.-> Obrišite kolonu gate-let\n5.-> Povratak na odabir tabele ")
            izbor_komande = int(input("Izaberite komandu: "))

            # Registruj pilota i let
            while True:
                if izbor_komande == 1:
                    connection = sqlite3.connect('aerodrom.db')
                    cursor = connection.cursor()

                    id_gate = int(input("Unesite ID gate-a kojim želite spojiti let: "))
                    id_let = int(input("Unesite ID leta na koji želite postaviti gate: "))

                    cursor.execute("SELECT * FROM gate WHERE id_gate = ?", (id_gate,))
                    gate = cursor.fetchone()

                    cursor.execute("SELECT * FROM let WHERE id_let = ?", (id_let,))
                    let = cursor.fetchone()

                    if gate and let:
                        cursor.execute("INSERT INTO pista (id_gate, id_let) VALUES (?, ?)", (id_gate, id_let))
                        print("Uspješno ste spojili gate i let, odnosno postavili pistu ")

                    else:
                        print("Greška! Ne postoji gate ili let sa ID-em koji ste unijeli ")
                    connection.commit()
                    connection.close()

                # ispis
                elif izbor_komande == 2:

                    connection = sqlite3.connect('aerodrom.db')
                    cursor = connection.cursor()

                    cursor.execute("SELECT * FROM pista")

                    ispis = cursor.fetchall()
                    print("")
                    print("Svi ID-gateova i ID-letova: (ID red) (ID gate), (ID let): ")
                    print(ispis)

                    connection.commit()
                    connection.close()

                # ažuriraj
                elif izbor_komande == 3:
                    connection = sqlite3.connect('aerodrom.db')
                    cursor = connection.cursor()

                    id_pista = int(input("Unesite ID kolone koju želite ažurirati: "))

                    cursor.execute("SELECT * FROM pista WHERE id_pista = ?", (id_pista,))

                    pista = cursor.fetchone()

                    if pista:
                        new_id_gate = int(input("Ažurirajte ID gate-a: "))
                        new_id_let = int(input("Ažurirajte ID leta: "))

                        cursor.execute("UPDATE pista SET id_gate = ?, id_let = ? WHERE id_pista = ?", (new_id_gate, new_id_let, id_pista,))
                        print("Uspješno ste ažurirali ID-eve ")
                    else:
                        print("Greška! Ne postoji kolona sa unešenim ID-em ")

                    connection.commit()
                    connection.close()

                # obriši
                elif izbor_komande == 4:
                    connection = sqlite3.connect('aerodrom.db')
                    cursor = connection.cursor()

                    id_pista = int(input("Uneiste ID kolone koju želite obrisati: "))

                    cursor.execute("SELECT * FROM pista WHERE id_pista = ?", (id_pista,))
                    pista = cursor.fetchone()

                    if pista:
                        cursor.execute("DELETE FROM pista WHERE id_pista = ?", (id_pista,))
                        print("Uspješno ste obrisali kolonu sa unijetim ID-em ")

                    else:
                        print("Greška! Ne postoji kolona sa unijetim ID-em ")

                    connection.commit()
                    connection.close()

                elif izbor_komande == 5:
                    adminKomande()

                else:
                    print("Greška! Izbor komande mora biti od 1 do 4 ")

                print("")
                print("0.-> Prekid programa\n1.-> Dodijelite gate-u let\n2.-> Ispišite ID-gateova i ID-letova koji su povezani\n3.-> Ažurirajte kolonu gate-let\n4.-> Obrišite kolonu gate-let\n5.-> Povratak na odabir tabele ")
                izbor_komande = int(input("Izaberite komandu: "))

        #User-Let(M:N)
        elif izbor_tabele == 12:
            # ispis
            izbor_komande = int(input("0.-> Kraj programa\n1.-> Ispis ID-eva putnika na letu, na osnovu unešenog ID-a leta\n2.-> Povratak na odabir tabele  "))

            while True:
                if izbor_komande == 1:
                    connection = sqlite3.connect('aerodrom.db')
                    cursor = connection.cursor()

                    id_let = int(input("Unesite ID leta na kojem želite provjeriti putnike"))

                    cursor.execute("SELECT id_user FROM karta WHERE id_let = ?", (id_let,))

                    ispis = cursor.fetchone()
                    print("Na letu (ID)", (id_let,), ", su putnici sa ID-evima:")
                    print(ispis)

                    connection.commit()
                    connection.close()

                elif izbor_komande == 0:
                    print("Kraj programa!")
                    exit()

                elif izbor_komande == 2:
                    adminKomande()

                else:
                    print("Greška! Izbor komandi mora biti 0 ili 1")

                izbor_komande = int(input("0.-> Kraj programa\n1.-> Ispis ID-eva putnika na letu, na osnovu unešenog ID-a leta\n2.-> Povratak na odabir tabele  "))

        #posada na letu (na osnovu ID-a)
        elif izbor_tabele == 13:

            print("")
            print("0.-> Završite program\n1.-> Povratak na odabir tabele \n2.-> Ispis svih clanova posade na osnovu ID-a leta: ")
            izbor_komande = int(input("Unesite komandu: "))

            while True:
                if izbor_komande == 0:
                    print("Kraj programa! ")
                    exit()

                elif izbor_komande == 1:
                    adminKomande()

                elif izbor_komande == 2:
                    connection = sqlite3.connect('aerodrom.db')
                    cursor = connection.cursor()

                    id_let = int(input("Unesite ID leta čiju posadu želite provjeriti: "))
                    cursor.execute("SELECT pilot.ime_pilot, stjuardesa.ime_stjuardesa, avion.model_avion, pilot.id_pilot, stjuardesa.id_stjuardesa, avion.id_avion FROM let JOIN pilot_let ON let.id_let = pilot_let.id_let JOIN pilot ON pilot_let.id_pilot = pilot.id_pilot JOIN stjuardesa_let ON let.id_let = stjuardesa_let.id_let JOIN stjuardesa ON stjuardesa_let.id_stjuardesa = stjuardesa.id_stjuardesa JOIN avion ON let.id_avion = avion.id_avion WHERE let.id_let = ?", (id_let,))

                    ispis = cursor.fetchall()

                    print("")
                    print("Ime pilota; Ime stjuardese; Model aviona; ID-pilota; ID-stjuardese; ID-aviona")
                    print(ispis)

                    connection.commit()
                    connection.close()

                else:
                    print("Greška! Izbor mora biti 0 ili 1 ")

                print("")
                print("0.->Završite program\n1.-> Povratak na odabir tabele \n2.->Ispis svih radnika na letu na osnovu ID-a: ")
                izbor_komande = int(input("Unesite komandu: "))

        #rezervisane karte
        elif izbor_tabele == 14:
            cursor.execute("SELECT * FROM karta ")
            karta = cursor.fetchall()
            print("")
            print("(ID karta) (ID user) (ID let)")
            print(karta)

        #odjava
        elif izbor_tabele == 15:
            print("Odjavili ste se! \n")
            main()

        else:
            print("Greška! Izbor mora biti od 1 do 15")
            exit()


def loginAdmin():
    connection = sqlite3.connect('aerodrom.db')
    cursor = connection.cursor()

    username_admin = input("Unesite Vaš admin username: ")
    password_admin = input("Unesite Vaš admin password: ")

    cursor.execute("SELECT ime_admin FROM admin WHERE username_admin = ? AND password_admin = ?", (username_admin, password_admin))

    admin = cursor.fetchone()

    if admin:
        print("")
        print("Uspješno ste se ulogovali kao admin / ovlašteno lice, {}".format(admin[0], "\n"))
        adminKomande()
    else:
        print("Pogrešno unešen username ili password! ")



def registerUser():

    connection = sqlite3.connect('aerodrom.db')
    cursor = connection.cursor()

    username_user = input("Unesite Vas username: ")
    password_user = input("Unesite Vas password: ")
    ime_user = input("Unesite Vase ime: ")
    prezime_user = input("Unesite Vase prezime: ")
    role_user = 'P'

    u = User(ime_user, prezime_user, "", "", "", username_user, password_user, 'P')

    cursor.execute(f"SELECT * FROM user WHERE username_user = '{username_user}'")
    postojeci_user = cursor.fetchone()

    while postojeci_user is not None:
        print("Username je zauzet ")
        username_user = input("Unesite neki drugi username ")
        cursor.execute(f"SELECT * FROM user WHERE username_user = '{username_user}'")
        postojeci_user = cursor.fetchone()

    cursor.execute("INSERT INTO user (username_user, password_user, ime_user, prezime_user, role_user) VALUES (?, ?, ?, ?, ?)",(username_user, password_user, ime_user, prezime_user, role_user))
    print("Uspješna registracija!\n")

    connection.commit()

    izbor_komande_reg = int(input("0.-> da se vratite na glavni meni\n1.-> Login\n2.-> Prekid programa: "))

    if izbor_komande_reg == 0:
        main()

    elif izbor_komande_reg == 1:
        loginUser()

    elif izbor_komande_reg == 2:
        print("Kraj programa")
        exit()

    else:
        print("Greška! Izbor mora biti 0, 1 ili 2")



    connection.commit()
    connection.close()


def loginUser():
    connection = sqlite3.connect('aerodrom.db')
    cursor = connection.cursor()

    username_user = input("Unesite Vaš username: ")
    password_user = input("Unesite Vaš password: ")

    cursor.execute("SELECT ime_user FROM user WHERE username_user = ? AND password_user = ? AND role_user = 'P'", (username_user, password_user))

    user = cursor.fetchone()

    if user:
        print("Uspješno ste se ulogovali, {}".format(user[0], "\n"))

        logged_username = username_user
        logged_password = password_user

        print("0.-> Završite program\n1.-> Odjavite se\n2.-> Rezervišite kartu")
        izbor_komande = int(input("Odaberite komandu: "))

        if izbor_komande == 0:
            print("Kraj programa! ")
            exit()

        elif izbor_komande == 1:
            logged_username = ""
            logged_password = ""
            print("")
            print("Odjavili ste se!\n")
            main()

        #funkcija rezervisanja karte
        elif izbor_komande == 2:

            print("")

            tezina_prtljage_user = int(input("Unesite težinu prtljage (10kg max) : "))
            klasa_user = int(input("Unesite željenu klasu sjedenja (od 1 do 3) : "))

            if 0 < klasa_user > 3 or tezina_prtljage_user > 10:
                print("Klasa mora biti od 1 do 3, a maksimalna težina je 10 kg ")
                exit()

            else:
                print("")
                print("Svi letovi na koje možete rezervisati karte: ")
                print("Podaci o letu ( Broj leta; Cijena leta (KM); Destinacija leta; Datum leta; Vrijeme leta; Broj aviona ) ")
                let_obj.ispisLet()

                izbor_leta = int(input("Unesite let (broj) na koji želite rezervisati kartu "))
                cursor.execute("SELECT id_let FROM let WHERE id_let = ?", (izbor_leta,))
                odabrani_let = cursor.fetchone()

                cursor.execute("SELECT id_user FROM user WHERE username_user = ? AND password_user = ?", (logged_username, logged_password))
                logovani_korisinik = cursor.fetchone()

                cursor.execute("UPDATE  user SET tezina_prtljage_user = ?, klasa_user = ?", (tezina_prtljage_user, klasa_user,))
                cursor.execute("INSERT INTO karta (id_user, id_let) VALUES (?, ?)", (logovani_korisinik[0], odabrani_let[0]))
                pocetni_zaslon = int(input("Uspješno ste rezervisali kartu! Hvala Vam na narudžbi! Za printanje karte i povratak na početni zaslon pritisnite 1: "))



                #izrada karte

                cursor.execute("SELECT id_karta FROM karta ORDER BY id_karta DESC LIMIT 1")
                id_karta = cursor.fetchone()

                cursor.execute("SELECT ime_user FROM user WHERE username_user = ?", (logged_username,))
                ime_user = cursor.fetchone()

                cursor.execute("SELECT prezime_user FROM user WHERE username_user = ?", (logged_username,))
                prezime_user = cursor.fetchone()

                cursor.execute("SELECT destinacija_let FROM let WHERE id_let = ?", (izbor_leta,))
                destinacija_let = cursor.fetchone()

                cursor.execute("SELECT cijena_karte_let FROM let WHERE id_let = ?", (izbor_leta,))
                cijena_let = cursor.fetchone()

                cursor.execute("SELECT vrijeme_let FROM let WHERE id_let = ?", (izbor_leta,))
                vrijeme_let = cursor.fetchone()

                cursor.execute("SELECT datum_let FROM let WHERE id_let = ?", (izbor_leta,))
                datum_let = cursor.fetchone()

                cursor.execute("SELECT id_avion FROM let WHERE id_let = ?", (izbor_leta,))
                id_avion = cursor.fetchone()

                karta = open("karta.txt", "w")

                karta.write("ID karte: ")
                karta.write(str(id_karta))
                karta.write("\n")

                karta.write("ID korisnika: ")
                karta.write(str(logovani_korisinik))
                karta.write("\n")

                karta.write("Ime putnika: ")
                karta.write(str(ime_user))
                karta.write("\n")

                karta.write("Prezime putnika: ")
                karta.write(str(prezime_user))
                karta.write("\n")

                karta.write("ID leta: ")
                karta.write(str(odabrani_let))
                karta.write("\n")

                karta.write("Tezina prtljage: ")
                karta.write(str(tezina_prtljage_user) + " kg")
                karta.write("\n")

                karta.write("Klasa sjedišta: ")
                karta.write(str(klasa_user))
                karta.write("\n")

                karta.write("Cijena leta: ")
                karta.write(str(cijena_let) + " KM")
                karta.write("\n")

                karta.write("Destinacija leta: ")
                karta.write(str(destinacija_let))
                karta.write("\n")

                karta.write("Vrijeme leta: ")
                karta.write(str(vrijeme_let))
                karta.write("\n")

                karta.write("Datum leta: ")
                karta.write(str(datum_let))
                karta.write("\n")

                karta.write("ID aviona na ovom letu: ")
                karta.write(str(id_avion))
                karta.write("\n")


                while pocetni_zaslon != 1:
                    pocetni_zaslon = int(input("Uspješno ste rezervisali kartu! Hvala Vam na narudžbi! Za printanje karte i povratak na početni zaslon pritisnite 1: "))



                    if pocetni_zaslon == 1:
                        logged_username = ""
                        logged_password = ""
                        main()


            connection.commit()
            connection.close()


    else:
        print("Pogrešno unešen username ili password!")


admin_obj = Admin(id_admin=None, ime_admin=None, prezime_admin=None, username_admin=None, password_admin=None, role_admin="A")
user_obj = User(id_user=None, ime_user=None, prezime_user=None, tezina_prtljage_user=None, klasa_user=None, username_user=None, password_user=None, role_user='P')
pilot_obj = Pilot(id_pilot=None, ime_pilot=None, prezime_pilot=None, broj_letova_pilot=None, plata_pilot=None)
stjuardesa_obj = Stjuardesa(id_stjuardesa=None, ime_stjuardesa=None, prezime_stjuardesa=None, plata_stjuardesa=None)
security_obj = Security(id_security=None, ime_security=None, prezime_security=None, plata_security=None, id_gate=None)
avion_obj = Avion(id_avion=None, model_avion=None, broj_sjedista_avion=None)
gate_obj = Gate(id_gate=None,broj_gate=None)
let_obj = Let(id_let=None, cijena_karte_let=None, destinacija_let=None, datum_let=None, vrijeme_let=None, id_avion=None)


#MAIN
def main():

    print("0.Prekid Programa\n1.Register\n2.Login\n3.Login(Admin)")
    unos = int(input("Unesite željenu opciju: "))

    if unos == 0:
        print("Prekid programa! ")
        print("")
        exit()

    elif unos == 1:
        registerUser()

    elif unos == 2:
        loginUser()

    elif unos == 3:
        loginAdmin()


main()
