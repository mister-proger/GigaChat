#include <iostream>
#include <WinSock2.h>
#include <WS2tcpip.h>
#include <thread>
#include <string>
#include <ctime>

#pragma comment (lib, "Ws2_32.lib")

using namespace std;

SOCKET Connection;
bool Connected = false;

void SendData(string sender, string text, string recipient = "all")
{
    if (Connected)
    {
        string json = "{\"text\":\"" + text + "\",\"sender\":\"" + sender + "\",\"recipient\":\"" + recipient + "\"}";
        send(Connection, json.c_str(), json.size() + 1, 0);
    }
}

void ReceiveData()
{
    while (Connected)
    {
        char buffer[1024];
        memset(buffer, 0, sizeof(buffer));
        int bytesReceived = recv(Connection, buffer, sizeof(buffer), 0);

        if (bytesReceived > 0)
        {
            string data = string(buffer, 0, bytesReceived);

            // json parsing
            // ...

            cout << data << endl;
        }
        else if (bytesReceived == 0)
        {
            cout << "Server disconnected." << endl;
            Connected = false;
        }
        else
        {
            cout << "Error: " << WSAGetLastError() << endl;
            Connected = false;
        }
    }
}

void ConnectToServer(string host, int port, string mask)
{
    WSADATA wsData;
    WORD ver = MAKEWORD(2, 2);

    int wsOk = WSAStartup(ver, &wsData);

    if (wsOk != 0)
    {
        cout << "Can't initialize Winsock! Quitting" << endl;
        return;
    }

    SOCKET sock = socket(AF_INET, SOCK_STREAM, 0);
    if (sock == INVALID_SOCKET)
    {
        cout << "Can't create socket! Quitting" << endl;
        return;
    }

    sockaddr_in hint;
    hint.sin_family = AF_INET;
    hint.sin_port = htons(port);
    inet_pton(AF_INET, host.c_str(), &hint.sin_addr);

    int connResult = connect(sock, (sockaddr*)&hint, sizeof(hint));

    if (connResult == SOCKET_ERROR)
    {
        cout << "Can't connect to server!" << endl;
        closesocket(sock);
        WSACleanup();
        return;
    }

    char buf[1024];
    memset(buf, 0, sizeof(buf));
    sprintf_s(buf, sizeof(buf), mask.c_str());
    send(sock, buf, strlen(buf), 0);

    Connected = true;
    Connection = sock;

    thread receiveThread(ReceiveData);
    receiveThread.detach();
}

int main()
{
    string host;
    int port;
    string mask;
    string recipient;

    cout << "Enter server host: ";
    cin >> host;

    cout << "Enter server port: ";
    cin >> port;

    cout << "Enter login mask: ";
    cin >> mask;

    ConnectToServer(host, port, mask);

    while (Connected)
    {
        string message;

        cout << "Enter message: ";
        getline(cin, message);

        SendData(mask, message, recipient);
    }
}