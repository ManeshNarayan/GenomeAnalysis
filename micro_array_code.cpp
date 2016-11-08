#include<iostream>
#include<cstdio>
#include<cstring>
#include "libxl.h"
#include<vector>
#include<string>
#include<map>
#include<algorithm>
#include<cmath>
#include<utility>
#include<sstream>
#include<cstdlib>
#include<fstream>
#include<cstring>
using namespace libxl;

long long n;
char * x,* p,* m, *x2, *m2;
char fin1[50];
std::map<std::string,int> fin;

int main()
{
    char gene_id[20];
     Book* book = xlCreateBook(); // xlCreateXMLBook() for xlsx
    if(book)
    {
        Sheet* sheet = book->addSheet("Sheet1");
        if(sheet)
        {
        sheet->writeStr(2, 1, "Gene Id");
        for (int i=2;i<=32;i++){
            std::cout<<i<<" ";
            sheet->writeNum(2, i, (i-2))

        }
        sheet->writeStr(2, 33, "Total");
        }
FILE * fp;
x=(char*)malloc(125000000);
 fp=fopen("osmotic_cinerea_downreg.txt","r");
 p=x;

FILE * fp1=fopen("osmotic_cinerea_downreg_acgt-tgac.txt","w");
 for(int gen_no=1;;gen_no++){
if(feof(fp)) break;
fscanf(fp,"%s",gene_id);

fscanf(fp,"%s",gene_id);
p=x;
gene_id[strlen(gene_id)-1]='\0';
 for(p=x;(p<=x+125000000) && (!feof(fp));p=p+1){ fscanf(fp,"%c",p);if(*p=='>') break;
 if(*p=='\n') p=p-1; } m=p-1;
int cond=0;
int ans1=0;
for(int val=0;val<=30;val++){
fin.clear();
int ans=0;
std::map<std::string,int>::iterator iii;
 int noos=0;
for(p=x;(p+val+7)<=m;p=p+1){
    if(*p=='A' && *(p+1)=='C' && *(p+2)=='G' &&*(p+3)=='T' && *(p+4+val)=='T' && *(p+5+val)=='G' && *(p+val+6)=='A' && *(p+val+7)=='C' ){
        char aaa[2];
        strcpy(fin1,"");
    int bol=0;
    for(int i=0;i<=val+7;i++){
        if(*(p+i)-'0'>=0&&*(p+i)-'0'<=9) bol=1;
        aaa[0]=*(p+i);aaa[1]='\0';
        strcat(fin1,aaa);
    }
if(bol) continue;

    std::string temp(fin1);
      if((iii=fin.find(temp))!=fin.end())
        iii->second++;
       else
        fin[temp]=1;
       ans++;

}}

ans1+=ans;int cnnt=0;

sheet->writeStr(gen_no+2, 1, gene_id);
sheet->writeNum(gen_no+2, val+2, ans);

for(iii=fin.begin();iii!=fin.end();iii++){
   fprintf(fp1,"%s: %s %d\n",gene_id,iii->first.c_str(),iii->second);
}
ans=0;
}
sheet->writeNum(gen_no+2, 33, ans1);

}
free(x);
fclose(fp);
book->save("osmotic_cinerea_downreg_acgt-tgac.xls");
        book->release();
}
}
