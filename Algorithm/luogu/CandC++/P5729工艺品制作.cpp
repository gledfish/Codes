#include <iostream>
using namespace std;

int w, x, h, ans, q;
int array[21][21][21];//立方体模型
int main()
{
    cin >> w >> x >> h >> q;
    while(q--)
    {
        int x1, y1, z1, x2, y2, z2;
        cin >> x1 >> y1 >> z1 >> x2 >> y2 >> z2;//输入
        for(int i = min(x1,x2); i <= max(x1,x2); i++)
        {
            for(int j = min(y1,y2); j <= max(y1,y2); j++)
            {
                for(int k=min(z1,z2); k<=max(z1,z2); k++)
                {
                    array[i][j][k] = 1; //标记每个已经被切割过的点
                }
            }
        }
    }
    for(int i = 1; i <= w; i++)
    {
        for(int j = 1; j <= x; j++)
        {
            for(int k = 1; k <= h; k++)
            {
                if(array[i][j][k]==0)
                {
                    ans++;//判断是否切割
                }
            }
        }
    }
    cout << ans <<endl;//输出
    return 0;//完结撒花
}