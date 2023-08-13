#include <bits/stdc++.h>
#define Max 10
using namespace std;
//定义栈
typedef struct Stack{
    int items[Max];
    int top;//指向最高的元素
}myStack, * stackPoint;

//创造空栈
stackPoint createEmpty(stackPoint sp){
    sp->top = -1;
    return  sp;
}

//判断栈空
bool isEmpty(stackPoint sp){
    int temp = sp->top;
    if(temp == -1)
        return true;
    else
        return false;
}

//判断栈满
bool isFull(stackPoint sp)
{
    int temp = sp->top;
    if (temp == Max - 1)
        return true;
    else
        return false;
}

//往栈中添加元素
bool push(stackPoint sp, int num){
    if(!isFull(sp)){
        sp->top++;
        sp->items[sp->top] = num;
        return true;
    }
    return false;
}
//从栈中删除元素
bool pop(stackPoint sp, int num){
    if(!isEmpty(sp)){
        int flag;
        for(int i = 0; i < Max;i++){
            if(sp->items[i] == num)
                flag = i;
                break;
        }
        for(int i = flag + 1; i < Max; i++){
            sp->items[i-1] = sp->items[i];
        }
        sp->top--;
        return true;
    }
    return false;
}
//输出栈中所有元素
void stackPrint(stackPoint sp){
    if(!isEmpty(sp)){
        for(int i = 0;i <= sp->top;i++){
            cout << sp->items[i] << endl;
        }
    }
}

int main(void){
   //demo
   stackPoint sp = new myStack;
   createEmpty(sp);
   cout << isEmpty(sp) << endl;
   push(sp, 43);
   push(sp, 34);
   cout << isFull(sp) << endl;
   stackPrint(sp);
   cout << endl;
   pop(sp, 43);
   stackPrint(sp);
   delete sp;
   return 0;
}