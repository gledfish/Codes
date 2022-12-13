/*
  name:rank.c
  author:gled fish
  time:2021/11/5
*/
#include <stdio.h>
#include <string.h>

int main() {
	int N, M, G;//N:考试人数M:考题数G:分数线
	int i, j, k, temp;//指示变量，中间量
	int n_1 = 0;
	char *tem;
	scanf("%d %d %d", &N, &M, &G);//考试数据
	char *cand_num[1000];//学号
	int cross_num[1000] = {0};//过线人数
	int sum[1000] = {0};//一个学生的成绩
	if (N == 0)
		return 0;
	if (N != 0) {
		int score[10];//每道题的分数
		int nums[10];//答对的题的数量
		for (i = 0; i < M; i++) {
			scanf("%d", &score[i]);//输入每道题的得分
		}
		int scores[1000];//答对题的题号
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
				cross_num[j] = i;//记录合格学生的序号
				j++;
			}
		}
		printf("%d\n", n_1);//输出合格学生的数量
		for (i = 0; i < n_1 - 1; i++) {
			for (j = 0; j <= n_1 - 1 - i; j++) {
				if (sum[cross_num[j]] < sum[cross_num[j + 1]]) { //冒泡排序从小到大
					temp = sum[cross_num[j]];
					sum[cross_num[j]] = sum[cross_num[j + 1]];
					sum[cross_num[j + 1]] = temp;
				}
				if (sum[cross_num[j]] == sum[cross_num[j + 1]]) { //特判分数相同
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