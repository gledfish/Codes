#include <bits/stdc++.h>

using namespace std;

typedef struct TreeNode{
    int value;
    struct TreeNode *left;
    struct TreeNode *right;
} BiNode;

//创建二叉树
BiNode* Create(){
    int val;
    cout << "请输入val：";
    scanf("%d", &val);
    BiNode* root = new BiNode;
    if(!root){
        cout << "Error:创建失败" << endl;
    }
    root -> value = val;
    root -> left = Create();
    root -> right = Create();

    return root;
}

//先序遍历 中 -> 左 -> 右
void PreOrderTree(TreeNode* root){
    if(root == NULL)
        return;
    cout << root -> value << endl;
    PreOrderTree(root -> left);
    PreOrderTree(root -> right);
}

//中序遍历
void InOrderTree(TreeNode* root){
    if(root == NULL)
        return;
    InOrderTree(root ->left);
    cout << root ->value << endl;
    InOrderTree(root ->right);
}

//后序遍历
void PostOrderTree(TreeNode* root){
    if(root == NULL)
        return;
    PostOrderTree(root ->right);
    cout << root -> value << endl;
    PostOrderTree(root -> left);
}

//返回树的高度
int maxDepth(TreeNode* root){
    if(root == NULL)
        return 0;
    else {
        int maxLeft = maxDepth(root -> left);
        int maxRight = maxDepth(root -> right);
        return 1 + maxLeft > maxRight ? maxLeft:maxRight;
    }
}

//求叶子节点的个数
int leafNodeNum(TreeNode* root){
    if(root == NULL)
        return 0;
    if(root -> left == NULL && root ->right == NULL){
        return 1;
    } else{
        return leafNodeNum(root ->left) + leafNodeNum(root -> right);
    }
}


int main(void)
{
    BiNode* tree = Create();
    PreOrderTree(tree);
    return 0;
}