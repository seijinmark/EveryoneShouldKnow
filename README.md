<p align="center">
  <img src="https://i.ibb.co/tDtzDYn/esk.png" alt="Everyone Should Know Logo" border="0">
</p>

<br>

<details>
<summary>Versão em Português</summary>

# Bot de Notificação de Chamadas do Discord

Este é um bot do Discord projetado para notificar os usuários quando alguém entra em um canal de voz. Ele também mantém um registro de quantas vezes cada usuário entrou em chamadas.

## Funcionalidades

- Envia uma mensagem quando alguém entra em um canal de voz vazio
- Mantém um registro de quantas vezes cada usuário entrou em chamadas
- Exibe um placar dos usuários que mais entraram em chamadas
- Permite ativar/desativar as notificações de entrada em chamadas

## Comandos

- `/leaders`: Mostra quantas vezes cada usuário entrou em chamadas (top 10)
- `/toggle`: Ativa/desativa a funcionalidade de enviar mensagens quando alguém entra em uma chamada
- `/help`: Exibe a lista de comandos disponíveis

## Configuração

1. Clone este repositório
2. Crie um arquivo `.env` baseado no `.env.exemple` e preencha com suas informações:
   - `DISCORD_BOT_TOKEN`: Token do seu bot do Discord
   - `CHANNEL_X`: IDs dos canais que o bot deve monitorar (até 10 canais)
   - `NOTIFICATION_CHANNEL`: ID do canal onde as notificações serão enviadas
3. Instale as dependências: `pip install -r requirements.txt`
4. Execute o bot: `python bot.py`

## Uso com Docker

1. Construa a imagem Docker: `docker build -t discord-call-bot .`
2. Execute o contêiner: `docker run -d --env-file .env discord-call-bot`

## Contribuições

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues ou enviar pull requests.

## Licença

Este projeto está licenciado sob a Licença MIT. A Licença MIT é uma licença de software permissiva que permite o uso, cópia, modificação e distribuição do software, desde que o aviso de direitos autorais e a permissão sejam incluídos em todas as cópias ou partes substanciais do software. Esta licença não oferece garantias e os autores ou detentores dos direitos autorais não são responsáveis por quaisquer reivindicações, danos ou outras responsabilidades decorrentes do uso do software.

</details>

---

<br>

# Everyone Should Know

This Discord bot is designed to notify users when someone enters a voice channel. It also keeps a record of how many times each user has entered calls.

## Features

- Sends a message when someone enters an empty voice channel
- Keeps a record of how many times each user has entered calls
- Displays a leaderboard of users who have entered calls the most
- Allows enabling/disabling call entry notifications

## Commands

- `/leaders`: Shows how many times each user has entered calls (top 10)
- `/toggle`: Enables/disables the functionality of sending messages when someone enters a call
- `/help`: Displays the list of available commands

## Setup

1. Clone this repository
2. Create a `.env` file based on `.env.exemple` and fill it with your information:
   - `DISCORD_BOT_TOKEN`: Your Discord bot token
   - `CHANNEL_X`: IDs of the channels the bot should monitor (up to 10 channels)
   - `NOTIFICATION_CHANNEL`: ID of the channel where notifications will be sent
3. Install dependencies: `pip install -r requirements.txt`
4. Run the bot: `python bot.py`

## Using with Docker

1. Build the Docker image: `docker build -t discord-call-bot .`
2. Run the container: `docker run -d --env-file .env discord-call-bot`

## Contributions

Contributions are welcome! Feel free to open issues or submit pull requests.

## License

This project is licensed under the MIT License. The MIT License is a permissive software license that allows for use, copying, modification, and distribution of the software, provided that the copyright notice and permission are included in all copies or substantial portions of the software. This license comes with no warranties, and the authors or copyright holders are not liable for any claims, damages, or other liabilities arising from the use of the software.