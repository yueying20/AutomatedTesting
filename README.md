# AutomatedTesting
基于Appium框架对网易云音乐APP进行UI自动化测试
python+appium + adb 安卓调试桥,用于连接和调试安卓设备工具+夜神模拟器
1.adb devices指令
三种状态: device 已连接状态 offline 未连接状态  unknow未识别状态
启动APP时, 首先调用是LaucherActivity 启动APP时,输入指令获取activity
Android手机Monkey对网易云APP进行稳定性测试
1. adb shell monkey的运行机制
实际上是执行手机中/system/bin/monkey这个脚本；
a.指定一个包执行10次：
adb shell monkey -p 包名 10 

adb shell monkey -v --pct-touch 10 20 触摸事件测试等
对网易云音乐UI自动化: 编写自动化测试代码对界面功能实现操作的基本覆盖
