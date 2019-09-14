# Markov
*******************
* tans_pro.py 是6ma_Markov的实现，其中包含10-fold交叉验证。
* Transition_probability_feature.py 是将转移概率当特征。
* Transition_probability_total.py 是类似转移概率计算的特征，实验效果要比完全的转移概率略好。
### 使用方法
*********************
python tans_pro.py  -trainfasta XXX.fasta -trainpos posnum -trainneg negnum -testfasta XXX.fasta -testpos num -testneg num -cv cv
