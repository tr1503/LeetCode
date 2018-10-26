#include <stdio.h>
#include <string.h>
#include <algorithm>
const int N = 1000005;
using namespace std;
char t[N],w[N];
int i,j,Next[N],sum,l;
void get_next(char *a,int len){
	Next[0]=-1;
	i=0;j=-1;
	while(i<len){
		if(j==-1||a[i]==a[j]) Next[++i]=++j;
		else j=Next[j];
	}
}
int KMP(char *a,char *b){
	int lena=strlen(a);
	int lenb=strlen(b);
	get_next(b,lenb);
	i=0;j=0;
	while(i<lena&&j<lenb){
		if(j==-1||b[j]==a[i]) i++,j++;
		else j=Next[j];
	}
	return j;
}
int main(){
	int n;
	scanf("%d",&n);
	while(n--){
		scanf("%s%s",&w,&t);
		//w主串
		int a=KMP(w,t);
		//printf("%d\n",a);
		int b=KMP(t,w);
		//printf("%d\n",b);
		printf("%d\n",strlen(w)+strlen(t)-max(a,b));
	}
	return 0;
}
