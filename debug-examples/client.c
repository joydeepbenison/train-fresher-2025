#include<stdio.h>
#include<stdlib.h>
#include<arpa/inet.h>
#include<string.h>
#include<unistd.h>  

int main(){
int socket_fd = socket(AF_INET,SOCK_STREAM,0);
if (socket_fd == -1){
    perror("socket");          
    exit(EXIT_FAILURE);
}

struct sockaddr_in server_addr = {.sin_family = AF_INET,
                                  .sin_port = htons(8080),
                                  .sin_addr.s_addr = inet_addr("127.0.0.1")};


int client_connect = connect(socket_fd, (struct sockaddr *)&server_addr, sizeof(server_addr));
if (client_connect == -1) {
    perror("connect");
    exit(EXIT_FAILURE);
}

while(1){
    printf(">>");
    char msg[1024] = {0};
   scanf("%s",msg);
    send(socket_fd, msg, strlen(msg), 0);
    sleep(1);
    char recv_msg[1024] = {0};
    memset(recv_msg, 0, sizeof(recv_msg));
    recv(socket_fd, recv_msg, sizeof(recv_msg)-1, 0);
    printf("Server: %s\n", recv_msg);
}

close(socket_fd);
return 0;

}