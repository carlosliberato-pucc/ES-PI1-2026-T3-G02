import votacao.auth as auth
import votacao.zeresima as zeresima
import menus as menus

def abrirVotacao():
    
    if auth.autenticarMesario():
        zeresima.zeresima()

        menus.menuOperarVotacao()

def operarVotacao():
    pass

def encerrarVotacao():
    pass