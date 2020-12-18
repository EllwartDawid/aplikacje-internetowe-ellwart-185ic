
 Zezwolenia i uwierzytelnianie w DRF
 
 Stworzyłem dwie aplikacje
- posts
- rental
 
 Dzięki pakietowi Django-rest-auth dodany został widok dla logowania/wylogowania, resetu hasła/potwierdzeniu resetu hasła 
 
 Aby panel rejstracji działał należy wprowadzić zmiany w pliku setting.py. 
 Jeżeli ustawimy TokenAuthentication to dostęp będą mieli tylko użytkownicy z tokenem
 
 ![App](https://github.com/EllwartDawid/aplikacje-internetowe-ellwart-185ic/blob/master/Lab6/ss/dostęp.PNG)
 
 Stworzenie viewsetów:
 
 ![App](https://github.com/EllwartDawid/aplikacje-internetowe-ellwart-185ic/blob/master/Lab6/ss/userviewset.PNG)
 
 ![App](https://github.com/EllwartDawid/aplikacje-internetowe-ellwart-185ic/blob/master/Lab6/ss/userviewset1.PNG)
 
 Routers:
 
 ![App](https://github.com/EllwartDawid/aplikacje-internetowe-ellwart-185ic/blob/master/Lab6/ss/routers.PNG)
 
 ![App](https://github.com/EllwartDawid/aplikacje-internetowe-ellwart-185ic/blob/master/Lab6/ss/routers1.PNG)
 
 Licznik wizyt z użyciem cookies
 
 ![App](https://github.com/EllwartDawid/aplikacje-internetowe-ellwart-185ic/blob/master/Lab6/ss/ciasteczkakod.PNG)
 
 ![App](https://github.com/EllwartDawid/aplikacje-internetowe-ellwart-185ic/blob/master/Lab6/ss/ciasteczka.PNG)
 
 Widoki działania aplikacji:
 
 Lista użytkowników:
 
 ![App](https://github.com/EllwartDawid/aplikacje-internetowe-ellwart-185ic/blob/master/Lab6/ss/listaużytkowników.PNG)
 
 Konkretny użytkownik:
 
 ![App](https://github.com/EllwartDawid/aplikacje-internetowe-ellwart-185ic/blob/master/Lab6/ss/user1.PNG)
 
 Widok login:

![App](https://github.com/EllwartDawid/aplikacje-internetowe-ellwart-185ic/blob/master/Lab6/ss/login.PNG)

 Widok logout:

![App](https://github.com/EllwartDawid/aplikacje-internetowe-ellwart-185ic/blob/master/Lab6/ss/logout.PNG)

 Widok Password Reset:

![App](https://github.com/EllwartDawid/aplikacje-internetowe-ellwart-185ic/blob/master/Lab6/ss/passwordreset.PNG)

 Widok Password Reset Confirm:

![App](https://github.com/EllwartDawid/aplikacje-internetowe-ellwart-185ic/blob/master/Lab6/ss/passwordresetconfirm.PNG)

 Widok rejestracji nowego użytkownika:

![App](https://github.com/EllwartDawid/aplikacje-internetowe-ellwart-185ic/blob/master/Lab6/ss/registration.PNG)

 Tworzę nowego użytkownika:

![App](https://github.com/EllwartDawid/aplikacje-internetowe-ellwart-185ic/blob/master/Lab6/ss/dawidtest.PNG)

 Utworzono konto i wygenerowano key czyli token dla nowego użytkownika:

![App](https://github.com/EllwartDawid/aplikacje-internetowe-ellwart-185ic/blob/master/Lab6/ss/utworzonekonto.PNG)

 Teraz użytkownik może się zalogować:

![App](https://github.com/EllwartDawid/aplikacje-internetowe-ellwart-185ic/blob/master/Lab6/ss/logindawidtest.PNG)

 Nowy użytkownik po zalogowaniu:

![App](https://github.com/EllwartDawid/aplikacje-internetowe-ellwart-185ic/blob/master/Lab6/ss/loginaccept.PNG)

 Użytkownik został dodany do listy użytkowników:

![App](https://github.com/EllwartDawid/aplikacje-internetowe-ellwart-185ic/blob/master/Lab6/ss/listaużytkowników1.PNG)

 W panelu admina można zobaczyć token nowego użytkownika:

![App](https://github.com/EllwartDawid/aplikacje-internetowe-ellwart-185ic/blob/master/Lab6/ss/token.PNG)


