// 已知N个人（以编号1，2，3，...，N分别表示）排成一列, 第一轮从编号为1的人开始依次报数，
// 数到2的倍数的人出列；第二轮从头开始依次报数，数到3的倍数的人出列；第三轮再次从头开始依次报数，
// 数到2的倍数的人出列；第四轮从头开始依次报数，数到3的倍数的人出列；
// 依此规律重复下去，直到队列中的人数不超过三个为止。
// 要求输出此时队列中剩下的人在初始队列中的编号。
#include <stdio.h>
#include <iostream>
#include <queue>
using namespace std;

int main()
{
    int n, i, m;
    int num;
    cin >> n;
    queue<int> q;
    for (i = 1; i <= n; i++)
    {
        q.push(i);
    }

    int count;
    int k = 2;
    while (n > 3)
    {
        m = n;
        count = 0;
        for (i = 0; i < m; i++)
        {
            num = q.front();
            count++;
            q.pop();
            if (count % k != 0)
            {
                q.push(num);
            }
            else
            {
                n--;
            }
        }

        if (k == 2)
            k = 3;
        else
            k = 2;
    }
    while (q.front() != 1)
    {
        num = q.front();
        q.pop();
        q.push(num);
    }
    while (!q.empty())
    {
        cout << q.front() << ' ';
        q.pop();
    }
    return 0;
}
