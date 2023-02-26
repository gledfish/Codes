#include <bits/stdc++.h>
#define MAX_NUM 100

using namespace std;

typedef struct str{
    char ch[MAX_NUM + 1];
    int length;
} * String;
// 字符串初始化
String initString(){
    String s = new str;
    s -> length = 0;
    return s;
}

//判断字符串是否为空
int isEmpty(String s){
    if(s->length == 0)
        return 1;
    else 
        return 0;
}

//输入字符串
String insertString(String s){
    cout << "请输入字符串"<< endl;
    scanf("%s", s->ch);
    s -> length = strlen(s->ch);
    return s;
}
//将str2复制给str1
String strCopy(String s1, String s2){
    for(int i = 0; i < s2->length;i++){
        s1 -> ch[i] = s2 ->ch[i];
    }
    s1 -> length = s2 ->length;
    return s1;
}
//将s1 和 s2连接，返回新的字符串
String strConcat(String s1, String s2){
    if(s1 ->length + s2 ->length > MAX_NUM){
        cout << "数组空间不足";
        exit(0);
    }
    String s3 = initString();
    for(int i = 0; i < s1 ->length; i++){
        s3 -> ch[i] = s1 ->ch[i];
    }
    for(int i = 0; i < s2 ->length; i++){
        s3 -> ch[s1 ->length + i] = s2 -> ch[i];
    }
    s3 -> length = s1 ->length + s2 ->length;
    return s3;
}
// 获取字符串的长度
int getLength(String s){
    return s ->length;
}

//输出字符串
void getString(String s){
    for(int i = 0; i < s->length; i++){
        cout << s->ch[i] << endl;
    }
}
int main(void){
    String s = initString();
    cout << getLength(s) << endl;
    s = insertString(s); 
    getString(s);
    return 0;
}
