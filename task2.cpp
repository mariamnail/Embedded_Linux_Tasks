#include <iostream>

int search(int arr[] , int size,int num){
    int x;
    for(int i = 0 ; i < size ; i++){
        if(arr[i] == num){
             x = 1;
        }
    }
     if(x == 1){
        std::cout << "The num " << num << " is found " << std::endl;
     }
     else{
        std::cout << "The num " << num << " is not found " << std::endl;
     }

}

int main(){ 
int num;
std::cout << "please enter the num" << std::endl;
std::cin >> num ;
int arr[] = {1,2,33,4,77,44,99,33,100};
int s = search(arr,9,num);
}