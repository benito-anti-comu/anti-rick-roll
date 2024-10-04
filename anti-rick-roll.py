#importiamo sleep da time
from time import sleep

#creriamo una funzione
def caratteri_finali(testo, n):
    return testo[-n:]  # Restituisce gli ultimi n caratteri del testo

#creriamo un messaggio di testo
print("""

!ATTENZIONE!
Questo programma e in fase di sviluppo,
quindi per ora non potra vedere tutti i link se sono rick roll.

""")

#dove si va a vedere se i link sono rick roll
while True:
    testo_utente = input("Inserisci un URL: ")

    # Controlla se gli ultimi 3 caratteri sono un link di rick roll
    if caratteri_finali(testo_utente, 3) == 'XcQ' or caratteri_finali(testo_utente, 3) == 'gG0'or caratteri_finali(testo_utente, 3) == 'nRw' or caratteri_finali(testo_utente, 3) == 'pv0':
        print("questo link e un rick roll\n")
        sleep(2)
    else:
        print("Questo link è sicuro, non ci sono rick roll.\n")
        sleep(2)
