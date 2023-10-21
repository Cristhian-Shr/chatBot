import os

def processar_resposta(resposta,nome):
    if resposta == '1':
        print(f'{os.linesep}{nome}, aguarde um momento!{os.linesep}')
    elif resposta == '2':
        print(f'{os.linesep}{nome}, uma Landing Page é uma página web focada em converter visitantes em ações desejadas, como compras ou cadastros. O objetivo é aumentar a taxa de conversão e fornecer uma experiência otimizada e direcionada ao usuário. O investimento para sua empresa ter uma LP é de inicial R$1.250,00. Para prosseguir digite a opção 1.{os.linesep}')
    elif resposta == '3':
        print(f'{os.linesep}{nome}, u2m site é uma coleção de páginas da web acessíveis por um endereço URL. Serve para fornecer informações, serviços ou produtos ao público online, sendo uma ferramenta essencial para divulgação, interação e alcance de público na era digital. O investimento para sua empresa ter um site é de inicial R$2.800,00. Para prosseguir digite a opção 1.{os.linesep}')
    elif resposta == '4':
        print(f'{os.linesep}{nome}, resposta4. Para prosseguir digite a opção 1.{os.linesep}')
    else:
        print('Sem opção ou invalida, digite apenas 1, 2, 3 e 4!')

def start():
    #Apresentar o chatbot
    print ('Olá, tudo bem?!')
    #pedir o nome
    nome = input ('Digite o seu nome: ')
    #pedir o contato
    contato = input ('Digite o seu contato: ')
    while True:
         #oferecer o menu de opção
        resposta = input (f'Como posso te ajudar?{os.linesep} [1] - Falar diretamente comigo!{os.linesep} [2] - Landing Page!{os.linesep} [3] - Site!{os.linesep} [4] - Anuncios pagos!{os.linesep}')
        #processar a resta enviada
        processar_resposta(resposta,nome)

if __name__ == '__main__':
    start()