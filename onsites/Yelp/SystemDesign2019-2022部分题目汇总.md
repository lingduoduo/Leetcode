

## Yelp 2019-2022 大部分System Design汇总

+ Design Twitter

+ design yelp user service(review + account + check-in + photo)

  +  着重问了database design，distributed system，还有如何设计API

+ Yelp news feed system

  + design review system
    message system

+ Design tiny URL

+ 考了一个offline 就是如果没网的时候用户搜索怎么办

+ 设计一个推送通知的系统，怎么设计数据库/限制同一用户被推送的次数/如果中间失败了怎么办？

+ 可以让Users随时下载自己的data

+ 设计一个加载用户个人中心的界面,  pull用户信息，有个人info还有视频照片以及po

+ ```tsx
  如何实现后端服务 个人中心有用户的核心信息和他的评论 还有他上传的照片 我的思路是核心信息存在关系型数据库里 图片存在AWS S3这种地方 评论可以存在非关系型数据库或者类似于Neo4j或者Dynamo更好一些。
  ```

+ 设计Yelp

  + ```tsx
    设计一个简单的 Yelp
    只可以匿名上传图片和 post review
    还有就是 read review
    可以让用户下载他在yelp上的所有评论，上传的图片，视频等。
    
    
    看似简单
    要设计上来有很多考量
    例如 replica/backup strategy
    database 的选择 (给经纬要可以快速找回附近的 review)
    data model 的设计
    database sharding
    CDN
    geolocation DNS
    image encoding
    ```

+ 设计一个log tracking system

  + ```TSX
    说是给yelp里面所有services用的，帮助debug和检查performance bottleneck在哪。这道题地里有，我事先准备过，就把我准备的大概说了一下。
    后来面试官追问我为什么用NoSQL数据库，index结构应该长什么样，log里都要记录什么信息才能满足requirement，最后有了exception怎么及时通知用户（alerting）。
    但是没有特别问scaling的问题。总体来说不难
    ```

+ 上传和下载文件

+ 拿数据和存储数据

  + ```tsx
    第一轮：SD，设计怎么去3rd party拿一个全新的数据和储存这些数据
    ```

+ 从第三方拿餐厅评分数据，能在用户端看到。

  + ```tsx
    头到尾面试官带着我，一个一个问题，要我做决定，每个决定说完，都会问有什么缺点，怎么提高。
                   问：怎么选、如何设计数据库
                          怎么从第三方拿数据，多久一次
                          etc
                   心得：只需要了解初级的系统设计知识。问题和答案都是开放性的，没有错对，但要知道优缺点。
    ```

+ 设计一个系统，支持添加好友，创建群聊，在群里发布餐馆投票，通知群聊中的人投票结果

  + ```tsx
    设计DB schema
    follow up:
    bottleneck 咋解决
    写个query 获取餐馆投票结果
    如果设计监控，监控哪些内容
    ```

+ 是从3rd party 拿一个类似Health score的数据 然后储存下来。Design a health score system for yelp

  + ```tsx
    需要从government获得health score，然后就开始问，类似于
    --通过什么方式获得信息(restAPI get)
    --是在user每次进入界面的时候都要去gov那里取一次吗(自定义周期，比如说一周一次)
    --取到的信息是什么格式的(file, like excel?)
    --怎么处理得到的信息并且放入db，db长什么样子，
    
    是一个全新的数据，系统里面本来没有的数据。
    需要自己考虑是sql vs nosql。我选的是sql，就跟进问了一些问题。
    怎么从第三方拿数据，多久一次？
    这些问题是你到时候需要跟面试官确定的。
    我也问了，面试官说API, SFTP啥啥的都行，3rd party 很flexible，你想怎么拿就怎么拿（看你的设计）
    因为这个“健康指数”这个数据不是很需要经常update，所以我选择了daily。不过这些也是我在clarify了很多问题之后做出的选择
    ```

+ 设计系统下载用户全部信息

  + ```tsx
    先讲了下如何触发这个功能，然后怎么设计的数据库，schema什么样子，图片存哪，然后怎么生成的report， 有什么方法提高速度，有什么trade off，权衡
    ```

+ 设计一个yelp新的feature，就是获得用户所有contribution，例如review

+ 设计notification的backend。要求支持实时发送和scheduled发送。怎么scale。这块之前准备的时候，schedule没有准备好，被问了好多。可以参考job scheduler去做

  + https://leetcode.com/discuss/general-discussion/1082786/System-Design%3A-Designing-a-distributed-Job-Scheduler-or-Many-interesting-concepts-to-learn

+ 要写data structure 模版。大概就是有很多services，互相传数据，要怎样trace，其它的就是常规的怎么储存数据，怎么monitoring了。

+ Time Tracking

  + ```tsx
    设计一个 Time Tracking 的Service用来记录每一个Micro Service所花费的时间。注意要简单写一下Class Structure, API，读写分开等等。一边聊一边设计，感觉不是很难。
    ```





## Sources

+ [2019年年初至今 药铺电面总结及思路（按照频率排序）+ 8/9新鲜面经|一亩三分地海外面经版 (1point3acres.com)](https://www.1point3acres.com/bbs/forum.php?mod=viewthread&tid=542585&ctid=229046)
+ [Yelp 電面|一亩三分地海外面经版 (1point3acres.com)](https://www.1point3acres.com/bbs/thread-511141-1-1.html)

