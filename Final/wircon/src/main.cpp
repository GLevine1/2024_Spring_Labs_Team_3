
#include <WiFi.h>
#include <sys/socket.h>

const char* ssid = "Sunrise Parabellum"; // Name of Network, figure out how to make this work on a different hotspot
const char* password = "goeagles"; // Network Password
int serverSocket;
int clientSocket;

void setup() {
    Serial.begin(115200);
    delay(1000);
    // Connecting to Mutual WiFi Network
    WiFi.mode(WIFI_STA); //Optional
    WiFi.begin(ssid, password);
    Serial.println("\nConnecting");

    while(WiFi.status() != WL_CONNECTED){
        Serial.print(".");
        delay(100);
    }
    Serial.println("\nConnected to the WiFi network");
    Serial.print("Local ESP32 IP: ");
    Serial.println(WiFi.localIP());
    // SERVER SOCKET SECTION *************************
    // Used when Nvidia Sends Messages -> Heltec
    serverSocket = socket(AF_INET, SOCK_STREAM, 0); 
    sockaddr_in serverAddress; 
    serverAddress.sin_family = AF_INET; 
    serverAddress.sin_port = htons(8000); 
    String ipString = WiFi.localIP().toString();
    serverAddress.sin_addr.s_addr = inet_addr(ipString.c_str()); 
    // binding socket. 
    bind(serverSocket, (struct sockaddr*)&serverAddress, 
         sizeof(serverAddress)); 
    listen(serverSocket, 5); 
    // accepting connection request 
    clientSocket = accept(serverSocket, nullptr, nullptr); 
  
   

//     closing the socket. 
//    close(serverSocket);

    // // CLIENT SOCKET SECTION *************************
    //  // Used when Heltec Sends Messages -> Nvidia
    // clientSocket = socket(AF_INET, SOCK_STREAM, 0);   
    // // specifying address 
    // sockaddr_in serverAddress; 
    // serverAddress.sin_family = AF_INET; 
    // serverAddress.sin_port = htons(8000); 
    // serverAddress.sin_addr.s_addr = inet_addr("192.168.1.169"); //Should be changed

    // connect(clientSocket, (struct sockaddr*)&serverAddress, 
    //         sizeof(serverAddress)); 
    // // closing socket 
    // //close(clientSocket); 
    // //*************************************************
}

void loop() {
    // recieving data 
    char buffer[1024] = { 0 }; 
    recv(clientSocket, buffer, sizeof(buffer), 0); 
    Serial.println(buffer);
    // if(buffer == "close"){
    //     close(clientSocket);
    // }
    const char* message = "Hello, client!"; 
    send(clientSocket, message, strlen(message), 0); 
}