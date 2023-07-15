# TelegramPythonBot
Bot para envio de informações via telegram.

# TelegramPythonBot
Bot para envio de informações via telegram. 

############## ETAPAS PARA CRIAÇÃO/EXECUÇÃO DO BOT ##############

1 - Criar o bot
- No telegram, pesquise "BotFather"
- Na conversa com o BotFather, digite /newbot
- Escolha um nome para o seu bot. Ex: bot_monitoramento
- Escolha o “username” do bot, que deve terminar em “bot”. Ex: “monitoramento_bot”.
- Se o nome do usuário do bot for válido, um TOKEN será gerado. Esse token deve ser usado no programA monitoramento_bot.py 

2 - Configurar o BOT no dispositivo do medidor
- Envie o arquivo monitoramento_bot.py para o dispositivo via SFTP
- Envíe o arquivo monitoramento.service para o dispositivo via SFTP para a pasta /etc/systemd/system/ 
- Instale as bibliotecas com o seguinte comando:
	sudo pip3 install pytelegrambotapi && sudo pip3 install schedule 

3 - Colocar o bot pra rodar
- No terminal do dispositivo, digite: 
	sudo systemctl enable monitoramento.service
- Em seguida, digite:
	sudo systemctl daemon-reload
- Em seguida, digite:
	sudo systemctl start monitoramento.service
- Comandos juntos (alternativo):
 	sudo systemctl enable gridzerobot.service && sudo systemctl daemon-reload && sudo systemctl start gridzerobot.service

###################### BIBLIOTECAS NECESSÁRIAS ######################

Bibliotecas necessárias:
sudo pip install thread6 && 
sudo pip install schedule &&
sudo pip3 install pyTelegramBotAPI &&
sudo pip3 install telebot
