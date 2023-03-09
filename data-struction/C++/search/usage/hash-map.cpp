#include <bits/stdc++.h>
// #include <iostream>
#define HASHSIZE 100// 定义散列表为数组的长度
#define NULLKEY -1
typedef struct
{
    int elem[HASHSIZE];
    int count;
} HashTable;

// 初始化哈希表
void Init(HashTable *hashtable, int l)
{
    hashtable->count = 0;
    for (int i = 0; i < HASHSIZE; i++)
    {
        hashtable->elem[i] = NULLKEY;
    }
}

// 哈希函数
int Hash(int data, int d)
{
    return data % d;
}

// 将元素映射到哈希表
void Insert(HashTable* hashtable, int data, int d, int l)
{
    int hashAddress = Hash(data, d);
    while (hashtable->elem[hashAddress] != NULLKEY)
    {
        // 解决冲突
        hashAddress += 1;
    }
    hashtable->elem[hashAddress] = data;
    printf("%d\n", hashAddress);
    hashtable -> count++;
}

// 查找数据data，返回对应的下表
int SearchHash(HashTable *hashtable, int data, int divisor, int length)
{
    int hashAddress = Hash(data, divisor);
    while (hashtable->elem[hashAddress] != data)
    { 
        // 解决冲突
        hashAddress += 1;
        if (hashtable->elem[hashAddress] == NULLKEY || hashAddress == Hash(data, divisor))
        // 出现了NULLKEY值或者经过了一个周期都说明找不到了
        {
            return -1;
        }
    }
    return hashAddress;
}
using namespace std;

int main(void)
{
    int length, divisor; 
    printf("请输入表长和除数：");
    scanf("%d %d", &length, &divisor);
    if(length >= 100 || divisor > length)
        return 0;

    HashTable hashTable;
    Init(&hashTable, length);
    //初始化为-1


    int temp;
    for(;;){
        printf("请输入关键字：");
        scanf("%d", &temp);
        if(temp == -1)
            break;
        int result = SearchHash(&hashTable, temp, divisor, length);
        if(result != -1){
            printf("%d\n", result);
        } else {
            if(hashTable.count == length - 1){
                printf("Table full\n");
                break;
            } else 
                Insert(&hashTable, temp, divisor, length);
        }
    }

    return 0;
}
