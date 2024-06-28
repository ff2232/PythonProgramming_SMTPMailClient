from socket import *

def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    mailserver = ('127.0.0.1', 1025)

    # Create socket called clientSocket and establish a TCP connection with mailserver and port
    # Fill in start

    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect(mailserver)

    # Fill in end

    recv = clientSocket.recv(1024).decode()


    # Send HELO command and print server response.
    HELOCommand = 'HELO Alice\r\n'
    clientSocket.send(HELOCommand.encode())
    recv1 = clientSocket.recv(1024).decode()

    # Send MAIL FROM command and handle server response.
    # Fill in start

    MAILFROMcommand = 'MAIL FROM: <ff2232@nyu.edu>\r\n'
    clientSocket.send(MAILFROMcommand.encode())
    recv2 = clientSocket.recv(1024).decode()


    # Fill in end

    # Send RCPT TO command and handle server response.
    # Fill in start

    RCPTTOcommand =  'RCPT TO: <nyulabs@gmail.com>\r\n'
    clientSocket.send(RCPTTOcommand.encode())
    recv3 = clientSocket.recv(1024).decode()

    # Fill in end

    # Send DATA command and handle server response.

    # Fill in start
    DATAcommand = 'DATA\r\n'
    clientSocket.send(DATAcommand.encode())
    recv4 = clientSocket.recv(1024).decode()
    
    # Fill in end

    # Send message data.
    # Fill in start

    message = 'I gotta get this right so I can back to studying'
    subject = 'Urgent'
    clientSocket.send(message.encode())
 
    # Fill in end

    # Message ends with a single period, send message end and handle server response.
    # Fill in start

    clientSocket.send('.\r\n'.encode())
    recv5 = clientSocket.recv(1024).decode()

    # Fill in end

    # Send QUIT command and handle server response.
    # Fill in start

    clientSocket.send('QUIT\r\n'.encode())

    # Fill in end


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')