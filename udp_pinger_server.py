#!/usr/bin/env python3
# -*- coding: utf-8 -*-


#O código a seguir implementa totalmente um servidor ping. você precisa compilar e execute este código antes de executar seu programa cliente. *Você não precisa para modificar este código.*

#Neste código de servidor, 30% dos pacotes do cliente são simulados para serem perdido. Você deve estudar este código cuidadosamente, pois ele irá ajudá-lo a escrever seu cliente de ping.

#  módulo para gerar pacotes perdidos aleatórios
import random
import socket

# Cria um soquete UDP

# Observe o uso de SOCK_DGRAM para pacotes UDP
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Atribuir endereço IP e número da porta ao soquete
serverSocket.bind(('', 12000))

while True:
    # Gera número aleatório no intervalo de 0 a 10
    rand = random.randint(0, 10)

    # Receba o pacote do cliente junto com o endereço de onde ele está vindo
    message, address = serverSocket.recvfrom(1024)

    # mensagem do cliente em maíuscuki
    message = message.upper()

    # Se rand for menor que 4, consideras o pacote perdido e não  responde
    if rand < 4:
        continue

    # Caso contrário, o servidor responde
    serverSocket.sendto(message, address)
