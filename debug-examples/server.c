#include <stdio.h>
#include <stdlib.h>
#include <arpa/inet.h>
#include <string.h>
#include <unistd.h> 

int main (){


    int sockfd = socket(AF_INET, SOCK_STREAM, 0);
    if (sockfd == -1) {
        perror("socket");
        exit(EXIT_FAILURE);
    }

   struct sockaddr_in server_addr = {.sin_family = AF_INET,
                                    .sin_port = htons(8080),
                                    .sin_addr.s_addr = inet_addr("127.0.0.1")};

    int bind_result = bind(sockfd,(struct sockaddr*)&server_addr,sizeof(server_addr));
    if (bind_result == -1) {
        perror("bind");
        close(sockfd);
        exit(EXIT_FAILURE);
    }
    listen(sockfd,5);
    int client_fd = accept(sockfd,NULL,NULL);
        if (client_fd == -1) {
            perror("accept");
            close(sockfd);
            exit(EXIT_FAILURE);
        }
    while(1) {
    
   //  char *buffer = 0 ;
        char buffer[1024]={0};
        ssize_t nbytes  = recv(client_fd,buffer,sizeof(buffer)-1,0);
	char *c =NULL ;
	*c = 'X';

	if (nbytes > 0) {
            buffer[nbytes] = '\0';
            printf("Received %zd bytes: %s\n", nbytes, buffer);
        } else if (nbytes == 0) {
            printf("Client disconnected\n");
            close(client_fd);
            continue;
        } else {
            perror("recv");
            close(client_fd);
            continue;
        }
        printf(">>");
        char msg[1024] = {0};
        scanf("%s",msg);
        send(client_fd, msg, strlen(msg), 0);
    

    
    }
    
    close(client_fd);
}
