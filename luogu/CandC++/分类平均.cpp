# include <bits/stdc++.h>

using namespace std;

int n, k, sum;

int main () {
	cin >> n >> k;
	for (int i = k; i <= n; i += k)
		sum += i;
	printf ("%.1lf ", (double) sum/ (n / k)); // ��ȷ��С����� 1 λ��ֱ�� %.1f ����
	sum = (1 + n) * n / 2 - sum;
	printf ("%.1lf\n", (double) sum / (n - n / k));
	return 0;
}
