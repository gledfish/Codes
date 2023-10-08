// ����˳���
#include <bits/stdc++.h>
#define MaxSize 100

using namespace std;

typedef int Status;
typedef int ElemType;

typedef struct
{
    ElemType data[MaxSize];
    int length;
} SqList;

// ����յ�˳���
SqList *initList(SqList *s)
{
    memset(s->data, 0, sizeof(s));
    s->length = 0;
    return s;
}

// ����˳�����,��ʼ��ǰn�����ݡ�
SqList *CreateList(SqList *s, int n)
{
    if (n < 0 || n >= MaxSize)
    {
        cout << "��ʼ��δ�ɹ�" << endl;
        return s;
    }
    printf("�������ݣ�\n");
    for (int i = 0; i < n; i++)
    {
        scanf("%d", &s->data[i]);
        s->length++;
    }
    printf("������ɣ�");
    return s;
}

// ���뺯������λ��i����Ԫ��
SqList* InsertList(SqList *s, int i, ElemType e)
{
    if (i < 1 || i > s->length)
    {
        cout << "λ����Ч" << endl;
        return s;
    }
    if (s->length >= MaxSize)
    {
        cout << "�洢�ռ�����" << endl;
        return s;
    }
    int num = i;
    for (int j= s->length; j >= i; j--)
    {
        s->data[j] = s->data[j - 1];
    }
    s->data[i - 1] = e;
    s->length++;
    return s;
}

// ���Һ�������λ�ò���Ԫ��e��������λ��
int LocateElem(SqList *s, ElemType e)
{
    for (int i = 0; i < s->length; i++)
    {
        if (s->data[i] == e)
            return i + 1;
    }
    cout << "û�ҵ�" << endl;
    return 0;
}

// ���ú�������ԭ˳�����
SqList *ReverseList(SqList *s)
{
    if (s->length)
    {
        for (int i = 0; i < s->length - 1 - i; i++)
        {
            int temp = s->data[i];
            s->data[i] = s->data[s->length - 1 - i];
            s->data[s->length - 1 - i] = temp;
        }
    }
    return s;
}

// ��ż�ֿ�������
//  ���˳���
SqList *ClearList(SqList *s)
{
    s->length = 0;
    return s;
}

// ������ܺ���
void PrintSqList(SqList *s)
{
    cout << "��ǰ˳�������Ԫ�أ�";
    for (int i = 0; i < s->length; i++)
    {
        cout << s->data[i] << "\t";
    }
    cout << "\n";
}

int main(void)
{
    SqList *s = new SqList;
    s = initList(s);
    int num = 5;
    s = CreateList(s, num);
    PrintSqList(s);
    s = InsertList(s, 1, 10);
    PrintSqList(s);
    delete s;
    return 0;
}