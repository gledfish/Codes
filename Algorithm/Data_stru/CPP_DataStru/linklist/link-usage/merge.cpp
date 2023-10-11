// 已知两个有序线性表L1和L2，每个线性表中数据元素的值为单调增的正整数（ < 100个），
// 各线性表内部无重复元素。
// 把L2中的元素合并到L1中，
// 要求L1中数据元素的值仍为单调递增，且无重复元素。

#include <stdio.h>
int main()
{
    int n1, n2;
    scanf("%d%d", &n1, &n2);
    int a[200] = {0};
    for (int i = 0; i < (n1 + n2); i++)
        scanf("%d", &a[i]);
    //起泡排序
    int flog, i, j, t;
    for (i = 0; i < (n1 + n2); i++)
    {
        flog = 1;
        for (j = n1 + n2 - 1; j > i; j--)
        {
            if (a[j - 1] > a[j])
            {
                t = a[j];
                a[j] = a[j - 1];
                a[j - 1] = t;
                flog = 0;
            }
        }
        if (flog)
            break;
    }
    printf("%d ", a[0]);
    for (i = 1; i < (n1 + n2); i++)
    {
        if (a[i] == a[i - 1])
            continue;
        else
            printf("%d ", a[i]);
    }
    return 1;
}