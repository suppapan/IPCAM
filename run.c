#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
int main() {
 
    
    goto Update;
        Update:
      
           
            printf("Install requirements packet...\n");
            sleep(3);
            system("yum update -y");
            system("apt-get update -y");
            printf("Making Output list...\n")
            sleep(5);
            printf("[scanner] Scanner process initialized. Scanning started.\n")
            system("echo YOUR IPCAM LIST : > output.txt");
system("python3 scan.py");
    return 0;
}
