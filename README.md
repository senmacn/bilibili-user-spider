# bilibili-user-spider
 - b站爬虫
 目标url：'https://space.bilibili.com/ajax/member/GetInfo' 获取个人信息
          'https://api.bilibili.com/x/relation/stat?' 获取粉丝数量
 
 > import agent为自定义模块，引入的是agent.txt文件里面的user-agent列表，用于模拟浏览器，可自行换为读取文件的方法
 
方法 ：requests，多线程

数据库 ：mysql

爬取速度：80~100个/mins

注意：两个url，headers不同，具体请参照目标网站
