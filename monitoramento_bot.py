import telebot #biblioteca para o bot
import schedule # programar o envio da produção em determinada hora
import time
import _thread #para deixar o polling e o envio programado rolando em paralelo
import threading

hora_envio = "08:00" #horário de envio automático das informações
CHAVE_API = " " #chave do equipamento em que o bot vai rodar (fornecido pelo telegram)
user_id=  #ID do Usuário que vai interagir com o bot

bot = telebot.TeleBot(CHAVE_API)

def runBot(): #thread do poll -> para permitir o acesso às informações a qualquer momento (basta enviar qualquer caracter pro bot)
    #bot.polling()
    bot.infinity_polling(timeout=10, long_polling_timeout=5)

def runSchedulers(): #thread do envio programado das inforamções

    def job():
        print("deu a hora de enviar")
        try:
            file_read = open(f'~/, 'r+').read().splitlines() #caminho do arquivo que vai ser lido com as informações
        except:
            file_read = None
            #bot.reply_to(mensagem, "Arquivo nao lido")
            return bot.send_message(user_id, "Arquivo nao lido.")
        if file_read:
            lido = """ 
            {}
            """.format("\n".join(file_read[0:])) #para converter uma lista em uma string multilinhas
            return bot.send_message(user_id, lido)

    schedule.every().day.at(hora_envio).do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)

def verificar(mensagem):
    return True

@bot.message_handler(func=verificar)

def responder(mensagem):
    try:
        file_read = open(f'~/', 'r+').read().splitlines() #caminho do arquivo que vai ser lido com as informações
    except:
        file_read = None
        bot.reply_to(mensagem, "Arquivo nao lido")
    if file_read:
        lido = """
        {}
        """.format("\n".join(file_read[0:]))
        bot.reply_to(mensagem, lido)
        #print(mensagem)

if __name__ == "__main__":
    t1 = threading.Thread(target=runBot)
    t2 = threading.Thread(target=runSchedulers)
    # starting thread 1 
    t1.start() 
    # starting thread 2 
    t2.start()


