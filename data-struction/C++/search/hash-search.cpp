#include <bits/stdc++.h>
#define HASHSIZE 7 //定义散列表为数组的长度
#define NULLKEY -1
typedef struct {
    int* elem;
    int count;  
} HashTable;  

//初始化哈希表
void Init(HashTable* hashtable){
    hashtable->elem = new int;
    hashtable->count = HASHSIZE;
    for(int i = 0; i < HASHSIZE; i++){
        hashtable->elem[i] = NULLKEY;
    }
}

//哈希函数
int Hash(int data){
    return data%HASHSIZE;
}

//将元素映射到哈希表
void Insert(HashTable* hashtable, int data){
    int hashAddress = Hash(data);
    while(hashtable->elem[hashAddress] != NULLKEY){
        //解决冲突
        hashAddress=(++hashAddress) % HASHSIZE;
    }
    hashtable->elem[hashAddress] = data;
}

//查找数据data，返回对应的下标
int SearchHash(HashTable *hashtable, int data){
    int hashAddress = Hash(data);
    while(hashtable->elem[hashAddress] != data){
        //解决冲突
        hashAddress=(++hashAddress)%HASHSIZE;
        if(hashtable->elem[hashAddress] == NULLKEY || hashAddress == Hash(data)){
            return -1;
        }
    }
    return hashAddress;
}
using namespace std;


int main(void){
    int i, result;
    HashTable hashTable;
    int arr[HASHSIZE] = {13, 29, 27, 28, 26, 30, 38};
    Init(&hashTable);
    //初始化
    for(int i = 0; i < HASHSIZE; i++){
        Insert(&hashTable, arr[i]);
    }
    //查找
    result = SearchHash(&hashTable, 29);
    if(result == -1)
        printf("查找失败");
    else 
        printf("已找到");
    return 0;
}