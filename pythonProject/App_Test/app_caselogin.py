from time import sleep
import yaml
from appium import webdriver
# 读取文件数据 r读取文件的内容
from selenium.webdriver.common.by import By
# def appium_login():
stream = open('../data/app_caps.yaml', 'r')
    # 数据读取处理
data = yaml.load(stream, Loader=yaml.FullLoader)
info = {}
info['platformName'] = data['platformName']
info['platformVersion'] = data['platformVersion']
info['deviceName'] = data['deviceName']
info['appPackage'] = data['appPackage']
info['appActivity'] = data['appActivity']
info['noRest'] = data['noRest']
driver = webdriver.Remote('http://' + str(data['ip']) + ':' + str(data['port']) + '/wd/hub', info)
driver.implicitly_wait(3)
driver.find_element(By.ID, 'com.netease.cloudmusic:id/agree').click()
driver.find_element(By.ID, 'com.netease.cloudmusic:id/permissionGrant').click()
driver.find_element(By.ID, 'com.android.packageinstaller:id/permission_allow_button').click()
driver.find_element(By.ID, 'com.android.packageinstaller:id/permission_allow_button').click()
sleep(10)
driver.find_element(By.ID, 'com.netease.cloudmusic:id/agreeCheckbox').click()
driver.find_element(By.ID, 'com.netease.cloudmusic:id/mail').click()
driver.find_element(By.ID, "com.netease.cloudmusic:id/email").send_keys("邮箱名称")
# 登录输入账号和密码
driver.find_element(By.ID, 'com.netease.cloudmusic:id/password').send_keys("密码")
driver.find_element(By.ID, 'com.netease.cloudmusic:id/login').click()
driver.find_element(By.ID, 'com.netease.cloudmusic:id/login').click()
sleep(7)
# 1.进入发现 2.选择每日推荐 3.获取前三首歌曲名
# 点击每日推荐

driver.find_element(By.XPATH, '//*[@text="每日推荐"]').click()
# 获取前三首歌曲
SongList = driver.find_elements(By.ID, 'com.netease.cloudmusic:id/songName')[:3]
for song in SongList:
    print(song.text)
sleep(2)
# driver.find_element(By.CLASS_NAME, 'android.widget.ImageButton').click()
driver.keyevent(4)

# 1.新建收藏夹-每日精选  将每日推荐的前三首歌曲收藏到每日精选
driver.find_element(By.XPATH, '//*[@text="我的"]').click()
# 上下滑动x轴不变 左右滑动y轴不变
sleep(3)
driver.find_element(By.XPATH, '//*[@text="创建歌单"]').click()
driver.find_element(By.ID, 'com.netease.cloudmusic:id/action').click()
# 创建新歌单
driver.find_element(By.XPATH,'//*[@text="创建新歌单"]').click()
# 输入歌单名称
driver.find_element(By.ID, 'com.netease.cloudmusic:id/etPlaylistName').send_keys("song")
# 点击确认
driver.find_element(By.ID,'com.netease.cloudmusic:id/tvCreatePlayListComplete').click()
#  回到主页
sleep(2)
driver.keyevent(4)
# 添加歌单
# 发现
driver.find_element(By.XPATH, '//*[@text="发现"]').click()
# 进入每日推荐
driver.find_element(By.XPATH, '//*[@text="每日推荐"]').click()
#  获取前三首歌曲操作菜单按钮 重复添加到歌单
options = driver.find_elements(By.ID, 'com.netease.cloudmusic:id/actionBtn')[:3]
for option in options:
    option.click()
    #收藏到歌单
    driver.find_element(By.XPATH, '//*[@text="收藏到歌单"]').click()
    # 选择每日精选
    driver.find_element(By.XPATH, '//*[@text="song"]').click()
driver.keyevent(4)
driver.find_element(By.XPATH, '//*[@text="我的"]').click()
# 点击每日精选歌单
driver.find_element(By.XPATH, '//*[@text="song"]').click()
# 获取所有的歌名
songs=driver.find_elements(By.ID, 'com.netease.cloudmusic:id/songName')
for song in songs:
    print(song.text)
# 删除创建的歌单-song
driver.keyevent(4)
driver.find_element(By.XPATH, '//*[@text="创建歌单"]').click()
driver.find_element(By.ID, 'com.netease.cloudmusic:id/action').click()
driver.find_element(By.XPATH,'//*[@text="歌单管理"]').click()
# 全选
driver.find_element(By.ID, 'com.netease.cloudmusic:id/icon_search').click()
# 删除
driver.find_element(By.ID, 'com.netease.cloudmusic:id/delete').click()
driver.find_element(By.ID, 'com.netease.cloudmusic:id/buttonDefaultPositive').click()

#　发现　播放视频　播放音乐
driver.find_element(By.XPATH, '//*[@text="发现"]').click()
driver.find_element(By.ID, 'com.netease.cloudmusic:id/video_img').click()
# 播放音乐
driver.keyevent(4)
driver.find_element(By.ID, 'com.netease.cloudmusic:id/newMusicImg').click()
driver.find_element(By.ID, 'com.netease.cloudmusic:id/newMusicImg').click()
# 下一曲
driver.find_element(By.ID, 'com.netease.cloudmusic:id/nextBtn').click()
# 上一曲
driver.find_element(By.ID, 'com.netease.cloudmusic:id/preBtn').click()
# 单曲播放
driver.find_element(By.ID, 'com.netease.cloudmusic:id/modeBtn').click()
# 停止播放
driver.find_element(By.ID, 'com.netease.cloudmusic:id/playBtn').click()
# 评论按钮
driver.find_element(By.ID, 'com.netease.cloudmusic:id/commentBtn').click()
# 评论和发送
sleep(2)
driver.find_element(By.ID, 'com.netease.cloudmusic:id/edit').send_keys('hello,world')
driver.find_element(By.XPATH, '//*[@text="发送"]').click()
sleep(2)
driver.keyevent(4)
driver.quit()

# return driver
