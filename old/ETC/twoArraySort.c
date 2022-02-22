

# include <stdio.h>

int main(void){
    int i, j, size=0, sizeA=0, sizeB=0, tmp;
    int *cmp, *cur;

    int a[3] = {1,8,3};
    int b[6] = {9,2,7,4,5,6};

    sizeA = sizeof(a)/sizeof(int);
    sizeB = sizeof(b)/sizeof(int);
    size = sizeA+sizeB;

    for(i=0; i<size-1; i++){
        if(i < sizeA){
            cur = a+i;
            for(j=i+1; j<size; j++){
                if(j < sizeA){
                    cmp = a+j;
                }else{
                    cmp = b+(j-sizeA);
                }
                if(*cur < *cmp)
                    cur = cmp;
            }
        }else{
            cur = b+(i-sizeA);
            for(j=i+1; j<size; j++){
                cmp = b+(j-sizeA);
                if(*cur > *cmp)
                    cur = cmp;
            }
        }
        if(i < sizeA){
            tmp = *(a+i);
            *(a+i) = *cur;
            *cur = tmp;
        }else{
            tmp = *(b+(i-sizeA));
            *(b+(i-sizeA)) = *cur;
            *cur = tmp;
        }
    }

    for(i=0; i<3; i++){
        printf("%d ", a[i]);
    }
    puts("");

    for(i=0; i<6; i++){
        printf("%d ", b[i]);
    }
    puts("");

    return 0;
}
/*
 # include <stdio.h>

 int main(void){
     int i, j, temp, size=0, sizeA=0, sizeB=0;
     int *front, *behind;
     int a[3] = {7,8,9};
     int b[6] = {1,2,3,4,5,6};
     
     sizeA = sizeof(a)/sizeof(int);
     sizeB = sizeof(b)/sizeof(int);
     size = sizeA+sizeB;

     // A+B: ASC
     for(i=size-1; i>0; i--){
         for(j=0; j<i; j++){
             if(j < sizeB-1){        // j < 5
                 front = b+j;
                 behind = b+(j+1);
             }else if(j == sizeB-1){     // j == 5
                 front = b+j;
                 behind = a+(j+1);
             }
             else{                   // j > 5
                 front = a+(j-sizeB);
                 behind = a+(j-sizeB+1);
             }
             
             if(front > behind){
                 temp = *front;
                 *front = *behind;
                 *behind = temp;
             }
         }
     }
     
     // A: DESC
     for(i=sizeA-1; i>0; i--){
         for(j=0; j<i; j++){
             front = a+j;
             behind = a+(j+1);
             if(front < behind){
                 temp = *front;
                 *front = *behind;
                 *behind = temp;
             }
         }
     }
     
     for(i=0; i<6; i++){
         printf("%d ", b[i]);
     }
     puts("");
     for(i=0; i<3; i++){
         printf("%d ", a[i]);
     }
     puts("");
     
     return 0;
 }

*/
