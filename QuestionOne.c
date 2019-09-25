#include <stdio.h>
/**
#This problem was recently asked by Google.
#Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
#For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
*/
int main()
{
    int k = 10;
    int arr [10] ={ 1,2,3,4,5,6,7,8,9,10};//Our test array
    if ( check_array(arr,k) == 0){
        printf("True");
    }
    else{
        printf("false");
    }
    return 0;
}

int check_array( int arr[],int k ){
    
    for ( int i = 0 ; i < 10 ; ++i){
        for ( int j = 0 ; j <10 ;++j){
            if ( arr[i] +arr[j] == k ){
                return 0;//REpresntation of true
            }
        }
    }
    return 1;//Representation of false
}
