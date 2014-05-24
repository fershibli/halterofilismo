import msvcrt, os, time, thread, socket

ascii_art=[
    [
        "",
        "",
        "",
        "",
        "",
        "               ('-')",
        "         _____/     \\_____",
        "        /        Y        \\",
        "        |   |         |   |",
        "        |   |\\   I   /|   |",
        "       (  |   |  H  |  |  )",
        "        /  \\<   > <   >/  \\",
        "  |||   \\  /:   : :   :\\  /   |||",
        "--|||:--|nm|-----------|mn|--:|||--",
        "  |||                         |||"
    ],
    [
        "",
        "",
        "",
        "",
        "",
        "               ('-')",
        "         _____/     \\_____",
        "        /        Y        \\",
        "        |   |         |   |",
        "        |   |\\   I   /|   |",
        "        (  |  |  H  |  |  )",
        "  |||  /   \\<   > <   >/   \\  |||",
        "--|||:--|nm|-----------|mn|--:|||--",
        "  |||       |__|   |__|       |||",
        ""
    ],
    [
        "",
        "",
        "",
        "",
        "",
        "               ('-')",
        "         _____/     \\_____",
        "        /        Y        \\",
        "       |    |         |    |",
        "        \\   )\\   I   /(   /",
        "  |||   (  |  |  H  |  |  )   |||",
        "--|||:--|nm|-----------|mn|--:|||--",
        "  |||       :   : :   :       |||",
        "            |__|   |__|",
        ""
    ],
    [
        "",
        "",
        "",
        "",
        "",
        "               ('=')",
        "         _____/     \\_____",
        "      /          Y          \\",
        "     |     |           |     |",
        "  ||| \\     )\\   I   /(     / |||",
        "--|||:--|nm|-----------|mn|--:|||--",
        "  |||   ````<   > <   >````   |||",
        "            :   : :   :",
        "            |__|   |__|",
        ""
    ],
    [
        "",
        "",
        "",
        "",
        "",
        "               (o_o)",
        "         _____/     \\_____",
        "      /          Y          \\",
        "  |||(      )         (      )|||",
        "--|||:--|nm|-----------|mn|--:|||--",
        "  |||  \\___)  |  H  |  (___/  |||",
        "            <   > <   > ",
        "            :   : :   :",
        "            |__|   |__|",
        ""
    ],
    [
        "",
        "",
        "",
        "",
        "",
        "               (o_o)",
        "         _____//   \\\\_____",
        "  ||| /          Y          \\ |||",
        "--|||:--|nm|-----------|mn|--:|||--",
        "  ||| \\(    )\\   I   /(    )/ |||",
        "       \\___/  |  H  |  \\___/",
        "            <   > <   >",
        "            :   : :   :",
        "            |__|   |__|",
        ""
    ],
    [
        "",
        "",
        "",
        "",
        "",
        "               (O_O)",
        "  |||    _____//   \\\\_____    |||",
        "--|||:--|uu|-----------|uu|--:|||--",
        "  |||( /    )         (    \\ )|||",
        "      \\    /)\\   I   /(\\    /",
        "       \\___/  |  H  |  \\___/",
        "            <   > <   >",
        "            :   : :   :",
        "            |__|   |__|",
        ""
    ],
    [
        "",
        "",
        "",
        "",
        "",
        "  |||          (OxO)          |||",
        "--|||:--|uu|-----------|uu|--:|||--",
        "  |||( /   \\`    Y    `/   \\ )|||",
        "      (\\   /|        | \\   /)",
        "       \\.../ \\   I   / \\.../",
        "              |  H  |",
        "           <    > <    >",
        "            :   : :   :",
        "            |__|   |__|",
        ""
    ],
    [
        "",
        "",
        "  |||                         |||",
        "--|||:-|uu|-------------|uu|-:|||--",
        "  ||| /    \\   (@_@)   /    \\ |||",
        "       (  ) __//   \\\\__ (  )",
        "    ( \\____/     Y     \\____/ )",
        "     ```\\__|           |__/```",
        "           \\\\    I    //",
        "              |  H  |",
        "             /  \\_/  \\",
        "           <    > <    >",
        "            :   : :   :",
        "            |__|   |__|",
        ""
    ],
    [
        "  |||                         |||",
        "--|||:-|uu|-------------|uu|-:|||--",
        "  |||/    \\             /    \\|||",
        "     \\    /             \\    /",
        "     (   \\     (@_@)     /   )",
        "     ((   ))__//   \\\\__((   ))",
        "      \\          Y          /",
        "        \\\\ |           | //",
        "            \\    I    /",
        "              |  H  |",
        "             /  \\_/  \\",
        "           <    > <    >",
        "            :   : :   :",
        "            |__|   |__|",
        ""
    ]]

jogando=True
poder_p1=0
poder_p2=0
vitorias_p1=0
vitorias_p2=0
numero_jogos=0
tecla_apertada=''
tecla_anterior=''

socketServidor=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
porta1=input("Porta de Entrada(por exemplo 20123): ")
porta2=input("Porta de Saida(por exemplo 20124): ")
try:
    socketServidor.bind(("", porta1))
    print('Escuta')
except:
    socketServidor.bind(("", porta2))
    print('Escuta Except(algo provavelmente deu errado...)')
socketCliente=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
IP_visivel=socket.gethostbyname(socket.gethostname())
data=''
trava=True
    
def conexaoJogadores():
    global data
    time.sleep(0.1)
    while jogando:
        data,addr=socketServidor.recvfrom(2048)

while 8001:
    print ('\n Seu IP: '+str(IP_visivel)+' (Feche outras conexoes, como o HAMACHI).')
    resposta=input('\nEscolha:\n\n 1 : Se conectar\n\n 2 : Esperar\n\n-')
    if resposta==1:        
        try:
            thread.start_new_thread(conexaoJogadores,())
        except:
            print "ERRO: nao foi possivel iniciar a comunicacao entre os jogadores."
        IP_amigo=raw_input('\nQual eh o IP do seu amigo?\n-')
        while data!='IP':
            try:
                socketCliente.sendto(IP_visivel,(IP_amigo,porta2))
            except:
                socketCliente.sendto(IP_visivel,(IP_amigo,porta1))
        break
    elif resposta==2:
        print 'ouvindo...'
        data,addr=socketServidor.recvfrom(1024)
        IP_amigo=data
        print(data,addr)
        print(IP_amigo)
        try:
            socketCliente.sendto('IP',(IP_amigo,porta2))
            print('enviou 1')
        except:
            socketCliente.sendto('IP',(IP_amigo,porta1))
            print('enviou 2')
        try:
            thread.start_new_thread(conexaoJogadores,())
        except:
            print "ERRO: nao foi possivel iniciar a comunicacao entre os jogadores."
        break
    else:
        print('Digite 1 ou 2!')


def desenhaHalterofilistas(jogador,oponente):
    if jogador>9:
        jogador=9
    if oponente>9:
        oponente=9
    print "#"*77
    for i in range(15):
        print "# "+str(ascii_art[jogador][i]) + " "*( 35 - int(len(ascii_art[jogador][i])) )+" # "+str(ascii_art[oponente][i])+" "*( 35 - int(len(ascii_art[oponente][i])) )+" #"
    print "#"*77

def verificaTeclas(atual,anterior):
    global tecla_apertada, tecla_anterior, poder_p1
    if str(tecla_apertada)==atual:
        if tecla_anterior==anterior:
            poder_p1+=1
        tecla_anterior=str(tecla_apertada)

def dissipassaoEnergia():
    global poder_p1
    while 1:
        time.sleep(0.25)
        if poder_p1>1:
            poder_p1-=1

def verificaVitoria():
    global poder_p1, vitorias_p1,poder_p2, vitorias_p2, numero_jogos
    if poder_p1>=100 or poder_p2>=100:
        numero_jogos+=1
    if poder_p1>=100:
        vitorias_p1+=1
        poder_p1=0
    if poder_p2>=100:
        vitorias_p2+=1
        poder_p1=0

def leituraTeclado():
    global tecla_apertada
    time.sleep(0.2)
    while jogando:
        tecla_apertada = str(msvcrt.getch()).lower()

try:
    thread.start_new_thread(leituraTeclado,())
except:
    print "ERRO: nao foi possivel iniciar a leitura de teclado."

try:
    thread.start_new_thread(dissipassaoEnergia,())
except:
    print "ERRO: nao foi possivel iniciar as rotinas periodicas."


def painelHalf(texto1, texto2):
    print "# "+" "*(18-len(str(texto1)))+str(texto1)+" "*(18)+"#"+" "*(18)+str(texto2)+" "*(18-len(str(texto2)))+" #"

def painelHash(texto):
    print "#"+" "*(38-int(len(str(texto))/2))+str(texto)+" "*(37-int(len(str(texto))/2)-len(str(texto))%2)+"#"

while jogando:
    time.sleep(1/30)
    verificaTeclas("a","s")
    verificaTeclas("w","a")
    verificaTeclas("d","w")
    verificaTeclas("s","d")
    print "#"*77
    print "#"+" "*75+"#"
    painelHash("H A L T E R O F I L I S M O")
    print "#"+" "*75+"#"
    painelHash("Aperte repetidamente A W D S nesta sequencia para levantar o peso!")
    print "#"+" "*75+"#"
    socketCliente.sendto(str(poder_p1),(IP_amigo,porta2))
    try:
        poder_p2=int(data)
    except:
        pass
    print "#"*77+"\n"
    desenhaHalterofilistas(int(poder_p1/10),int(poder_p2/10))
    print "\n"+"#"*77
    painelHalf(" "," ")
    print "#"+" "*31+"PODER DE LUTA"+" "*31+"#"
    painelHalf(poder_p1,poder_p2)
    painelHalf(" "," ")
    painelHash("De "+str(numero_jogos)+" partidas, venceram:")
    painelHalf(str(vitorias_p1),str(vitorias_p2))
    painelHalf(" "," ")
    print "#"*77
    verificaVitoria()
    os.system('cls')
jogando=False
