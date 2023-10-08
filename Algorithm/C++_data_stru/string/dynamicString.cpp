#include <bits/stdc++.h>

using namespace std;

typedef struct {
    char* ch;
    int length;  
} HString;

//初始化字符串
HString* Strinit(HString* str) {
    str -> length = 0;
    str -> ch = new char;
}

//返回字符串的长度，并更新length的属性
HString* StrLength(HString* str) {
    char* chs = str -> ch;
    int length = 0;
    while(chs[length] != '\0') {
        length++;
    }
    str -> length = length;
    return str;
}

//子串匹配
//返回第一个字符的索引，如果无法匹配则返回 -1
int StrIndex(HString* s, HString* p){
    int i = 0, j = 0;
    while(i < s->length && j < p->length){
        if(s->ch[i] == p ->ch[i]){
            //匹配成功
            i++;
            j++;
        } else{
            //未匹配成功
            i = i - j + 1;
            j = 0;
        }
    }
    if( j >= p ->length) return (i - p ->length);
    return -1;
}
int main(void){

    return 0;
}