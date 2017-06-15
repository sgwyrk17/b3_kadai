# B3課題3  

0. 事前準備   
0-1. opencv2をインストール    　 
0-2. ダウンロードからレポジトリをダウンロード・解凍    

## 1. glassesフォルダのの画像の平均を計算し、画像形式で保存しなさい。 
ヒント：画像のパスを一気にもってくるには、globというパッケージがおすすめ  
ヒント2：読み込んだ配列はnumpy配列に変換しよう   
出力結果  
![glasses_output.jpg](https://bitbucket.org/repo/Kyk97r/images/1592354380-glasses_output.jpg)
## 2. people.jpg画像に対して顔検出を行い、検出した領域を矩形で書き込みなさい。
ヒント：カスケード分類器というものを使います  
出力結果  
![5745463107785.jpg](https://bitbucket.org/repo/Kyk97r/images/4026527045-5745463107785.jpg)
## 3. エッジ検出を用いてdish1.jpg画像内の円を検出しなさい。
ヒント：HoughCircle
###3-1. 検出した領域を書き込みなさい。  
出力結果:  
![out1_dish1.jpg](https://bitbucket.org/repo/Kyk97r/images/4245899692-out1_dish1.jpg)  
###3-2. 検出した領域を矩形で切り取りなさい。  
出力結果：  
![out2_dish1.jpg](https://bitbucket.org/repo/Kyk97r/images/2017652888-out2_dish1.jpg)  
###3-3. 検出した領域以外を0埋めしなさい。 
出力結果：  
![out3_dish1.jpg](https://bitbucket.org/repo/Kyk97r/images/2124959070-out3_dish1.jpg)  

##4. dark.jpgのヒストグラムをRGBそれぞれで計算し、ヒストグラム平坦化を行いなさい。 
ヒント：RGBチャンネルそれぞれで平坦化！  
出力結果：画像のRGBヒストグラム
![histogram1.jpg](https://bitbucket.org/repo/Kyk97r/images/754416630-histogram1.jpg)
出力結果：平坦化を行った画像のRGBヒストグラム  
![histogram2.jpg](https://bitbucket.org/repo/Kyk97r/images/69333887-histogram2.jpg)
出力結果：平坦化を行った画像  
![dark_flat.jpg](https://bitbucket.org/repo/Kyk97r/images/3301152948-dark_flat.jpg)
