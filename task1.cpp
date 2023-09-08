#include <iostream>

int max(int arr[] , int size){
    int max_num = arr[0];
    for(int i = 0 ; i < size ; i++){
        if(arr[i] > max_num){
            max_num = arr[i];
        }
    }
   return max_num;
    //std::cout << "max num is " << max_num << std::endl;
}

int main(){ 
int arr[] = {1,2,33,4,77,44,99,33,100};
int MAX = max(arr,9);
std::cout << "max num is " << MAX << std::endl;
}