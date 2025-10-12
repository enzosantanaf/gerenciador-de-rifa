import random

def verificar_numero_bilhete(rifa, total_bilhetes):
    try:
        numero_bilhete_informado = int(input('Informe o número do bilhete. \n> '))
        if numero_bilhete_informado not in range(1, total_bilhetes+1):
            print(f'\nErro: Informe um número entre 1 e {total_bilhetes}.\n')
            return False
        
        for bilhete in rifa:
            numero_bilhete_vendido = bilhete['numero_bilhete']
            if numero_bilhete_informado == numero_bilhete_vendido:
                print('\nErro: Bilhete já vendido! Informe outro número de bilhete.\n')
                return False

        return numero_bilhete_informado
    except ValueError:
        print(f'\nNúmero do bilhete inválido. Informe um número entre 1 e {total_bilhetes}.\n')
        return False


def registro_venda(rifa, total_bilhetes):
    nome_comprador = input('Informe o nome do comprador.\n> ')
    while True:
        numero_bilhete = verificar_numero_bilhete(rifa, total_bilhetes)
        if numero_bilhete != False:
            venda_bilhete = {
                'nome_comprador': nome_comprador,
                'numero_bilhete': numero_bilhete
            }
            return venda_bilhete


def resumo_vendas(rifa, total_bilhetes):
    bilhetes_vendidos = len(rifa)
    bilhetes_disponiveis = total_bilhetes - bilhetes_vendidos
    return bilhetes_vendidos, bilhetes_disponiveis
        

def sorteador(rifa):
    random.shuffle(rifa)
    bilhete_escolhido = random.choice(rifa)
    return bilhete_escolhido


def resultado_sorteio(bilhete_sorteado):
    nome_ganhador = bilhete_sorteado['nome_comprador']
    numero_bilhete_escolhido = bilhete_sorteado['numero_bilhete']
    resultado_sorteio = f'\n\n\nSorteio realizado!!!\nO ganhador é {nome_ganhador}, bilhete {numero_bilhete_escolhido}!\n\n'
    return resultado_sorteio


def iniciar_sorteio(rifa):
    bilhete_sorteado = sorteador(rifa)
    print(resultado_sorteio(bilhete_sorteado))


def nova_rifa():
    print('\n\nDejesa iniciar uma nova rifa?')
    nova_rifa = input('Digite "iniciar" para começar uma nova rifa \nou pressione qualquer tecla para encerrar o programa.\n> ')
    nova_rifa = nova_rifa.upper()
    if nova_rifa != 'INICIAR':
        print('Fim do programa!')
        return False
    return True
    
    
# Iniciando programa principal
if __name__ == '__main__':
    rifa = []
    total_bilhetes = 5
    while True:
        venda_bilhete = registro_venda(rifa, total_bilhetes)
        rifa.append(venda_bilhete)
        print(f'Venda concluída! Bilhete {venda_bilhete["numero_bilhete"]} vendido para {venda_bilhete["nome_comprador"]}.')

        bilhetes_vendidos, bilhetes_disponiveis = resumo_vendas(rifa, total_bilhetes)
        print(f'Bilhetes vendidos: {bilhetes_vendidos} | Bilhetes disponíveis: {bilhetes_disponiveis}\n')

        if bilhetes_disponiveis != 0:
            inicio_sorteio = input('\nPressione qualquer tecla para registrar uma nova venda.\nPara iniciar o sorteio, digite "iniciar".\n\n> ')
            inicio_sorteio = inicio_sorteio.upper()
            
            if inicio_sorteio == 'INICIAR':
                iniciar_sorteio(rifa)
                
                if nova_rifa():
                    rifa = []
                else:
                    break
        
            continue

        input('Todos os bilhetes foram vendidos. Pressione qualquer tecla para começar o sorteio.\n> ')
        iniciar_sorteio(rifa)

        if nova_rifa():
            rifa = []
        else:
            break
