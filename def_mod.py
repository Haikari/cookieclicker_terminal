import itens

def shop():
    print(f"\n-- Shop -- \n" \
    f"\nWarning! A typo could stop the program! \n"
    f"\n0.  Exit" \
    f"\n1.  Click (+1/s|${itens.click_price})|{itens.click_qntd}) - Isso é um terminal, não tem como clicar manualmente" \
    f"\n2.  Grandma (+5/s|${itens.vovo_price}|{itens.vovo_qntd}) - Coloque a sua vó para trabalhar"
    f"\n3.  Chá (+100/s|${itens.cha_price}|{itens.cha_qntd}) - Chá faz bem para a alma, não é?"
    f"\n4.  Alexa (+500/s|${itens.alexa_price}|{itens.alexa_qntd}) - Por que não uma Alexa?"
    f"\n5.  Yomi Yori (+2.2k/s|${itens.yomiyori_price}|{itens.yomiyori_qntd}) - o preço correto para o BPM correto"
    f"\n6.  Monster (+4k/s|${itens.monster_price}|{itens.monster_qntd}) - Já provou o novo monster rosa?"
    f"\n7.  ASSEMBLY (+15k/s|${itens.asm_price}|{itens.asm_qntd}) - A única linguagem de programação que me recuso a entender"
    f"\n8.  Yuri (+40k/s|${itens.yuri_price}|{itens.yuri_qntd}) - 'me coloca como uma ryo Yamada cabeçuda', Yuri 2026"
    f"\n9.  Emi Cute Cute (+220k|${itens.emi_price}|{itens.emi_qntd}) - Amo a pessoa nos itens 10 e 11"
    f"\n10. Saki-Chan (+400k|${itens.sakichan_price}|{itens.sakichan_qntd}) - Oblivionis, não temerei o esquecimento"
    f"\n11. Takao Kanon (+1M|${itens.takaokanon_price}|{itens.takaokanon_qntd}) - Se pudesse, a Emi passaria horas falando de mim")

    i = str(input("\nYou: "))
    a = "\nYou can't buy it\n"

    if (i == "0"):
        None

    if (i == "1" and itens.dindin >= itens.click_price):
        itens.dindin -= itens.click_price
        itens.click_qntd+=1
        itens.click_price*=itens.aum
        itens.click = 1*itens.click_qntd
        


    elif (i == "2" and itens.dindin >= itens.vovo_price):
        itens.dindin -= itens.vovo_price
        itens.vovo_qntd+=1
        itens.vovo_price*=itens.aum
        itens.vovo = 5*itens.vovo_qntd
    
    elif (i == "3" and itens.dindin >= itens.cha_price):
        itens.dindin -= itens.cha_price
        itens.cha_qntd+=1
        itens.cha_price*=itens.aum
        itens.cha = 100*itens.cha_qntd

    elif (i == "4" and itens.dindin >= itens.alexa_price):
        itens.dindin -= itens.alexa_price
        itens.alexa_qntd+=1
        itens.alexa_price*=itens.aum
        itens.alexa = 500*itens.alexa_qntd
    
    elif (i == "5" and itens.dindin >= itens.yomiyori_price):
        itens.dindin -= itens.yomiyori_price
        itens.yomiyori_qntd+=1
        itens.yomiyori_price*=itens.aum
        itens.yomiyori = 2200*itens.alexa_qntd

    elif (i == "6" and itens.dindin >= itens.monster_price):
        itens.dindin -= itens.monster_price
        itens.monster_qntd+=1
        itens.monster_price*=itens.aum
        itens.monster = 4000*itens.monster_qntd
    
    elif (i == "7" and itens.dindin >= itens.asm_price):
        itens.dindin -= itens.asm_price
        itens.asm_qntd+=1
        itens.asm_price*=itens.aum
        itens.asm = 15000*itens.asm_qntd
    
    elif (i == "8" and itens.dindin >= itens.yuri_price):
        itens.dindin -= itens.yuri_price
        itens.yuri_qntd+=1
        itens.yuri_price*=itens.aum
        itens.yuri = 40000*itens.yuri_qntd

    elif (i == "9" and itens.dindin >= itens.emi_price):
        itens.dindin -= itens.emi_price
        itens.emi_qntd+=1
        itens.emi_price*=itens.aum
        itens.emi = 220000*itens.emi_qntd

    elif (i == "10" and itens.dindin >= itens.sakichan_price):
        itens.dindin -= itens.sakichan_price
        itens.sakichan_qntd+=1
        itens.sakichan_price*=itens.aum
        itens.sakichan = 400000*itens.sakichan_qntd

    elif (i == "11" and itens.dindin >= itens.takaokanon_price):
        itens.dindin -= itens.takaokanon_price
        itens.takaokanon_qntd+=1
        itens.takaokanon_price*=itens.aum
        itens.takaokanon = 1000000*itens.takaokanon_qntd

    else:
        print(a)
   

def money():
    i = itens.click + itens.vovo + itens.cha + itens.alexa + itens.yomiyori + itens.monster + itens.asm + itens.yuri + itens.emi + itens.sakichan + itens.takaokanon
    print("\nYour money: ${}|{}/s \n".format(itens.dindin,i))
    

def money_ps():
    itens.dindin = itens.dindin + itens.click + itens.vovo + itens.cha + itens.alexa + itens.yomiyori + itens.monster + itens.asm + itens.yuri + itens.emi + itens.sakichan + itens.takaokanon