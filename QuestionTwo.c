
#include <stdio.h>

/**
 * This problem was asked by Uber.
 * 
 * Given an array of integers
 * 
 * return a new array such that each element at index i of the new array is the product of all the numbers in the original array
 * 
 * except the one at i.
 * 
 * For example, if our input was [1, 2, 3, 4, 5]
 * 
 * the expected output would be [120, 60, 40, 30, 24].
 * 
 * If our input was [3, 2, 1], the expected output would be [2, 3, 6].
*/
int main(){
        
        int arr [5] = {1, 2, 3, 4, 5};
        int ans_arr [5];
        reduce_array(arr,ans_arr);
        for(int i = 0;i<5;++i){
            printf("%d\n",ans_arr[i]);
        }
        
    }

void reduce_array(int arr[] , int ans_arr[]){
    
    int answer = 1;
    for ( int i = 0; i < 5;++i){
        for(int j = 0 ; j < 5;++j){
            if( i == j){
                continue;
            }
            answer *= arr[j];
        }
        ans_arr[i] = answer;
        answer = 1;
    }
}
