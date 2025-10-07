rifa = []


def verificar_numero_bilhete(numero_bilhete_informado, rifa):
    if numero_bilhete_informado not in range(1, 100+1):
        print('\nErro: Informe um número entre 1 e 100.\n')
        return False
    for bilhete in rifa:
        numero_bilhete_vendido = bilhete['numero_bilhete']
        if numero_bilhete_informado == numero_bilhete_vendido:
            print('\nErro: Bilhete já vendido! Informe outro número de bilhete.\n')
            return False
    return True


def registro_venda():
    nome_comprador = input('Informe o nome do comprador.\n> ')
    while True:
        try:
            numero_bilhete = int(input('Informe o número do bilhete. \n> '))
            if verificar_numero_bilhete(numero_bilhete, rifa):
                venda_bilhete = {
                    'nome_comprador': nome_comprador,
                    'numero_bilhete': numero_bilhete
                }
                return venda_bilhete
        except:
            print('\nNúmero do bilhete inválido. Informe um número entre 1 e 100.\n')


def resumo_vendas(rifa):
    total_bilhetes = 100
    bilhetes_vendidos = len(rifa)
    bilhetes_disponiveis = total_bilhetes - bilhetes_vendidos
    return bilhetes_vendidos, bilhetes_disponiveis
        


while True:
    venda_bilhete = registro_venda()
    rifa.append(venda_bilhete)
    print(f'Venda concluída! Bilhete {venda_bilhete["numero_bilhete"]} vendido para {venda_bilhete["nome_comprador"]}.')
    
    bilhetes_vendidos, bilhetes_disponiveis = resumo_vendas(rifa)
    print(f'Bilhetes vendidos: {bilhetes_vendidos} | Bilhetes disponíveis: {bilhetes_disponiveis}\n')
    
    iniciar_sorteio = input('\nPressione qualquer tecla para registrar uma nova venda.\nPara iniciar o sorteio, digite "iniciar".\n\n> ')
    iniciar_sorteio = iniciar_sorteio.upper()

    if iniciar_sorteio == 'INICIAR':
        break
    
    if bilhetes_disponiveis == 0:
        print('Todos os bilhetes foram vendidos. Pressione qualquer tecla para começar o sorteio.')
        iniciar_sorteio = input('> ')
        break
