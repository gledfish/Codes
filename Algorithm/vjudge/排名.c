/*
  name:rank.c
  author:gled fish
  time:2021/11/5
*/
#include <stdio.h>
#include <string.h>

int main() {
	int N, M, G;//N:��������M:������G:������
	int i, j, k, temp;//ָʾ�������м���
	int n_1 = 0;
	char *tem;
	scanf("%d %d %d", &N, &M, &G);//��������
	char *cand_num[1000];//ѧ��
	int cross_num[1000] = {0};//��������
	int sum[1000] = {0};//һ��ѧ���ĳɼ�
	if (N == 0)
		return 0;
	if (N != 0) {
		int score[10];//ÿ����ķ���
		int nums[10];//��Ե��������
		for (i = 0; i < M; i++) {
			scanf("%d", &score[i]);//����ÿ����ĵ÷�
		}
		int scores[1000];//���������
		for (i = 0; i < N; i++) {
			scanf("%s", &*cand_num[i]);
			scanf("%d", &nums[i]);
			for (j = 0; j < nums[i]; j++) {
				scanf("%d", &scores[j]);
				for (k = 1; k <= M; k++) {
					if (scores[j] == k)
						sum[i] = sum[i] + score[k - 1];
				}
			}
		}
		j = 0;
		for (i = 0; i < N; i++) {
			if (sum[i] >= G) {
				n_1 ++;
				cross_num[j] = i;//��¼�ϸ�ѧ�������
				j++;
			}
		}
		printf("%d\n", n_1);//����ϸ�ѧ��������
		for (i = 0; i < n_1 - 1; i++) {
			for (j = 0; j <= n_1 - 1 - i; j++) {
				if (sum[cross_num[j]] < sum[cross_num[j + 1]]) { //ð�������С����
					temp = sum[cross_num[j]];
					sum[cross_num[j]] = sum[cross_num[j + 1]];
					sum[cross_num[j + 1]] = temp;
				}
				if (sum[cross_num[j]] == sum[cross_num[j + 1]]) { //���з�����ͬ
					if (strcmp(cand_num[cross_num[j]], cand_num[cross_num[j + 1]]) > 0) {
						/**tem = *cand_num[j];*/strcpy(tem, cand_num[j]);
						/**cand_num[j] = *cand_num[j+1];*/strcpy(cand_num[j], cand_num[j + 1]);
						/**cand_num[j+1] = *tem;*/strcpy(cand_num[j + 1], tem);
					}
				}
			}
		}
	}
	for (j = 0; j < n_1; j++) {
		printf("%s %d", cand_num[cross_num[j]], sum[cross_num[j]]);
	}
	return 0;
}