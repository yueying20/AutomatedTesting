# AutomatedTesting
基于Appium框架对网易云音乐APP进行UI自动化测试
python+appium + adb 安卓调试桥,用于连接和调试安卓设备工具+夜神模拟器
1.adb devices指令
三种状态: device 已连接状态 offline 未连接状态  unknow未识别状态
启动APP时, 首先调用是LaucherActivity 启动APP时,输入指令获取activity
Android手机Monkey对网易云APP进行稳定性测试
adb shell monkey的运行机制
实际上是执行手机中/system/bin/monkey这个脚本；
a.指定一个包执行10次：
adb shell monkey -p 包名 10 
adb shell monkey -v --pct-touch 10 20 触摸事件测试等对事件进行相关测试

对网易云音乐UI自动化: 编写自动化测试代码对界面功能实现操作的基本覆盖
•	测试模块: (1)邮箱登录 (2)每日推荐、获取歌曲、添加/删除收藏夹、添加每日推荐的前三首歌曲、删除歌曲 (3) 播放音乐、停止播放、下一首、上一首、点击评论、发送评论
