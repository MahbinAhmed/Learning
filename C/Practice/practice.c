// #include <stdio.h>
// #include<stdlib.h>

// int main(void) {
// 	int t;
// 	scanf("%d\n",&t);
//     getchar();
// 	int *ptr;
// 	ptr = (int*) malloc(t*sizeof(int));
// 	int temp_x, temp_y, temp_a;
// 	for(int i=0;i<=t;i++){
// 	    scanf("%d",&temp_x);
//         getchar();
//         scanf("%d",&temp_y);
//         getchar();
//         scanf("%d",&temp_a);
//         getchar();

//         if(temp_x<=temp_a && temp_y>temp_a){
//             ptr[i] = 1;
//         }
//         else{
//             ptr[i] = 0;
//         }
// 	}
//     for(int i=0;i<=t;i++){
//         if(ptr[i]==1){
//             printf("YES\n");
//         }
//         else{
//             printf("NO\n");
//         }
//     }
// 	return 0;
// }
// #include <stdio.h>

// int main(void)
// {
// 	int t;
// 	int x,y,A;
// 	scanf("%d",&t);
// 	while(t>0)
// 	{
// 	    scanf("%d %d %d",&x,&y,&A);
// 	    if((A>=x)&&(A<y))
// 	       printf("YES\n");
// 	    else
// 	       printf("NO\n");
// 	  t--;
// 	}
// 	return 0;
// }

// #include <stdio.h>

// int main(void) {
// 	int t,x;
// 	scanf("%d",&t);
// 	for (int i=0;i<t;i++){
// 	    scanf("%d",&x);
// 	    printf("%d\n",x*15);
// 	}
// 	return 0;
// }

#include <stdio.h>

int main(void) {
	int ttc;
	scanf("%d",&ttc);
	int x;
	for (int i=0;i<ttc;i++){
	    scanf("%d",&x);
	    printf("%d",x*15);
	}
	return 0;
}