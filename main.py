import itens
import def_mod
import time
import keyboard

print("\nOlá, este 'jogo' foi feito com carinho pela Emi, e foi feito por pura diversão" \
"\nDivirta-se!!!!!" \
"\nTwitter: @haikari_emi"
"\nDiscord: @haikari_emi"
"\n---------------------")

while True:
    def_mod.money_ps()
    


    i = str(input("\n1. Shop \n2. Itens (Ignore it) \n3. Check your money \n4. AFK\n\nYou: "))

    if ("1" in i):
        def_mod.shop()

    if ("2" in i):
        None

    if ("3" in i):
        def_mod.money()

    if ("4"  in i):
        while True:
         print("press esc to stop")
         def_mod.money()
         print("-------------\n\n")
         def_mod.money_ps()
         
         
         if (keyboard.is_pressed("esc")):
             break
         
         time.sleep(1.0)