#include <iostream>
void DELETE(int arr[] , int& size,int num){
    int x = -1;
    for(int i = 0 ; i < size ; i++){
        if(arr[i] == num){
             x = i;       
        }
    }
     if(x != -1 ){
      for (int i = x ; i < size -1 ; i++)
      {
         arr[i] = arr[i+1];
        
      }
     size--;
     }
     for (int i = 0; i < size; i++)
     {
         std::cout << arr[i] << std::endl;
      
     }
}

int main(){ 
int num , size = 9;
std::cout << "please enter the num" << std::endl;
std::cin >> num ;
std::cout<< "............................ " << std::endl;  
int arr[] = {1,2,3,4,5,6,7,8,9};
DELETE(arr,size,num);
}

