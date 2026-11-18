# ESE5023\_Assignments\_12632733

1.代码逻辑正确，注释清晰

2.内层循环变量写成j，外层循环也为j,变量重复

建议改为M2 = \[\[0 for j in range(5)] for i in range(10)]

建议分行打印矩阵，便于查看

误用加号，并且直接赋值覆盖结果，没有累加乘积，无法完成矩阵乘法。修改为res\[i]\[j] += A\[i]\[k] \* B\[k]\[j]即可（-2分）

3.代码逻辑正确，思路清晰

4.代码逻辑正确，思路清晰

5\. 代码逻辑正确，但是建议不要多重for循环

建议文档内给出详细解题思路


HW3 Comments from Yali  

Total: 44/50

1.2 You don’t consider weighting by area(or latitude), and the pole area should has smaller weight.  (-2p)

2.1. I think plots may be more clear. Also you don’t print SST monthly climatology and anormalies, I don’t know that is correct or not. (-2p)
2.2 Your plot is wrong, EI NIno and La Nina threshold lines are y=+/- 0.5°C (-3p)

3.Good job. Very detailed explanation! (+1p)