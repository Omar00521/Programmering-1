travelbag = []

while True:
   menyval = input("1. Kolla i resväskan\n"
                   "2. Lägg sak i resväskan\n"
                   "3. Ta bort sak i resväskan\n"
                   "4. Avsluta program")

   if menyval == "1":
       print("i väskan har du: ", end="")
       print(*travelbag, sep=",")

   elif menyval == "2":
       travelbag.append (input("vad vill du lägga till?"))

   elif menyval == "3":
       travelbag.remove (input("vad vill du ta bort?"))

   elif menyval == "4":
       break