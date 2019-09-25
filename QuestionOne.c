#include <stdio.h>

int main()
{
    int k = 10;
    int arr [10] ={ 1,2,3,4,5,6,7,8,9,10};
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
                return 0;
            }
        }
    }
    return 1;
}
