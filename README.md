# MM-6mAPred

* tans_pro.py 是MM-6mAPred的实现，其中包含交叉验证和独立测试。
#### 序列必须等长 !!！
### 参数设置
*******************

|参数|取值|
|:-:|:-|  
|-trainfasta|xxx.fasta|    
-trainpos|    	正例数  
-trainneg|       	反例数  
-testfasta  | 	 xxx.fasta
-testpos   | 	正例数  
-testneg  |		反例数  
-cv   |		交叉验证折数默认10  
### 必须设置的参数
* -trainfasta
* -trainpos
* -trainneg
### 使用方法
*********************
* 交叉验证用法：
```py
python tans_pro.py  -trainfasta XXX.fasta -trainpos posnum -trainneg negnum -cv cv
```
* 独立测试用法：
```py
python tans_pro.py  -trainfasta XXX.fasta -trainpos posnum -trainneg negnum -testfasta XXX.fasta -testpos num -testneg num 
```
