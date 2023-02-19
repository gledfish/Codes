// 标题
// huffman编码
//         时间限制 2 S
//             内存限制 10000 Kb
//                 问题描述
//                     假设用于通信的电文由ｎ（4 < n < 30）个字符组成，字符在电文中出现的频度（权值）为w1w2…wn，试根据该权值序列构造哈夫曼树，并计算该树的带权路径长度。 问题输入
//                                                         一组数据，第１行为ｎ的值，第２行为ｎ个整数，表示字符的出现频度。
//                                                             问题输出
//                                                                 输出一个整数，表示所构造哈夫曼树的带权路径长度。
//                                                                     输入样例 8 7 19 2 6 32 3 21 10

//     输出样例 261

#include <bits/stdc++.h>
    using namespace std;

typedef struct
{
    int weight;
    int parent, lchild, rchild;
} HTNOTE, *HuffmanTree;
// typedef char** HuffmanCode;

void Select(HuffmanTree HT, int n, int *s1, int *s2);

void CreatHuffmanTree(HuffmanTree *HT, int *w, int n)
{
    int i = 0, s1 = 0, s2 = 0;
    if (n <= 1)
        return;
    int m = 2 * n - 1;
    *HT = (HuffmanTree)malloc(sizeof(HTNOTE) * (m + 1));
    if (!*HT)
        exit(-1);
    HuffmanTree adjust = NULL;
    for (adjust = *HT + 1, i = 1; i <= n; i++, adjust++, w++)
    {
        adjust->weight = *w;
        adjust->parent = 0;
        adjust->rchild = 0;
        adjust->lchild = 0;
    }
    for (; i <= m; i++, adjust++)
    {
        adjust->weight = 0;
        adjust->parent = 0;
        adjust->rchild = 0;
        adjust->lchild = 0;
    }
    for (i = n + 1; i <= m; i++)
    {
        Select(*HT, i - 1, &s1, &s2);
        (*HT + s1)->parent = (*HT + s2)->parent = i;
        (*HT + i)->lchild = s1;
        (*HT + i)->rchild = s2;
        (*HT + i)->weight = (*HT + s1)->weight + (*HT + s2)->weight;
    }
}
int Min(HuffmanTree HT, int n)
{
    int min = 1000;
    int flag;
    for (int i = 1; i <= n; i++)
    {
        if ((HT + i)->weight < min && (HT + i)->parent == 0)
        {
            flag = i;
            min = (HT + i)->weight;
        }
    }
    (HT + flag)->parent = 1;
    return flag;
}
void Select(HuffmanTree HT, int n, int *s1, int *s2)
{
    *s1 = Min(HT, n);
    *s2 = Min(HT, n);
}
int FindWay(HuffmanTree HT, int n, int *w)
{
    int sum = 0;
    for (int i = 1; i <= n; i++)
    {
        HuffmanTree q = HT + i;
        int m = 0;
        while (q->parent != 0)
        {
            q = HT + q->parent;
            m++;
        }
        sum += m * w[i - 1];
    }
    return sum;
}

int main()
{
    int n;
    scanf("%d", &n);
    int w[n];
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &w[i]);
    }
    HuffmanTree HT;
    CreatHuffmanTree(&HT, w, n);
    int sum = FindWay(HT, n, w);
    printf("%d", sum);
    /*for(int i=1;i<=2*n-1;i++){
        printf("%d ",(HT+i)->weight);
    }*/
}
