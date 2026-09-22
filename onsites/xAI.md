整理了 19 篇 2026 年的 xAI 相关帖子（11 篇实战面经 + 8 篇流程/包裹补充），外加地里面经题库（43 题，题库页 2026-09-12 更新）。xAI 是几家 AI 公司里面试风格最"野"的：流程快得离谱（面完 24 小时内定下一轮，节假日深夜都排），15 分钟 video screen 是第一道闸，coding 不考 LeetCode 考现场 debug 和从零搭系统，Exceptional SWE 这条线最后要过马斯克本人审"三个最牛逼成就"。11 篇实战帖全部打开全文核验，题面尽量引用楼主原话；帖子没写的细节不脑补。

一、流程概览

- 速度极快：2025 年底过经帖楼主原话："整个流程极快…每一轮面完基本 24 小时内就定下一轮…面试时间完全不分节假日或深夜"。
- 第一道闸是 15 分钟 video screen / tech lead 聊天：自我介绍 + 简历深挖为主，有帖子约 15 分钟聊成 35 分钟，问题包括"过去两年 recent projects""有没有用过 Kerberos""用没用过 go 和 rust""是否 comfortable 申请 security clearance"。
- Exceptional SWE 线（2026 年 8 月流程分享帖，求职讨论版，全文可见）：HR 聊完不直接约技术面，先填表写 Three Most Exceptional Achievements，每条一两句话（楼主原话："每条最好只有一两句话，越短越好"，突出技术复杂度、自己具体负责了什么、impact/ROI）；表格发给两位从 Cursor 跳过来的 lead 初审——原因是马斯克会在 VO 之后审核每一个 pending offer 的成就 list，"马斯克一般看到长篇大论直接就扔了"；初审过后和其中一位 lead 15 分钟聊一下 → project deep dive（自己准备 PPT，前 30 分钟讲一个过去最牛的 project，后 15 分钟提问，相当于店面）→ Palo Alto 实地 onsite 大半天到一天：早上给几个实际项目 prompt，讨论后自己用 AI 写代码，午饭和团队一起吃一起讨论进展，临下班前 casual presentation demo 成品 → offer 阶段简历 + 三个成就放到马斯克台面上，他点头才有 offer call。楼主当时还在等成就 list 审核。评论区有人称 Tesla AI onsite 过了、挂在 exceptional achievement 不够牛逼。
- 创始人轮：最后确认意向 + 卖情怀，直接谈 offer（2025 年底过经帖）。
- NG 线（2026-07-01 挂经帖）：从 2 月到 9 月换了三个 HR，每次都是 general HR screening 唠嗑；然后 30 分钟 technical screen，"没有coding只有system design：URL shortening service"；onsite"跟去年的面经不太一样，不是leetcode，整体的focus还是system design，先是30min whiteboarding（AI not allowed）聊怎么设计，然后1个半小时implement（AI allowed），最后给30min wrap up/demo；具体内容签了NDA没办法分享，但Alex Xu的system design这本书非常全面，建议吃透"；"他们家新的ng pipeline非常注重system design，没有任何手搓coding环节"；面完直接被告知挂了，HR 说冷冻期 6 个月。IPO 前后 HC 动荡是楼主自己的说法。
...
- Recruiter screen 也能直接挂人：有帖子称只和 recruiter 聊了 10 分钟 past project，隔天收到拒信。
- Take-home：Data Engineer 岗是 48 小时 Data Cleaning Pipeline（百万级 parquet 网页爬取文档）；2025 年过经帖 OA 是 4 小时倒计时，楼主原话："题型和地里之前报的一模一样…必须开 Cursor 或者用 AI 辅助生成 boilerplate，纯手敲绝对写不完。Docker 化那一块可以等 4 小时倒计时结束后再搞定"。
- Offer 之后还有马斯克终审（见上），offer call 才算数。

二、高频题（完整题面）


Coding：不考 LeetCode，考现场 debug + 从零手写

1. Multithreaded BankAccount Race-Condition Bug Hunt——题库 phone-screen/tech-screen 题，Frequency: Low，Last asked: 2026-04-04。题库题面：15 分钟 video screen 里，面试官直接贴一段带 buggy deposit 方法的 BankAccount 类（read → sleep(0.1) → write），要求：找出所有并发 bug；给出线程安全版本；不许原地改类，必须用 subclass/wrapper 加锁（copy-paste 类体再改会被拒）；准备好讨论 Go 版本——Go 没有继承，要用 struct embedding + sync.Mutex，且必须在 wrapper 上重新声明方法。两处 bug：read-modify-write race（sleep 只是放大窗口，不是根因），以及全程无同步原语。确定性失败演示：两个线程分别 deposit 500/700 都读到 0，最后余额 700 而不是 1200。正确姿势：class SafeAccount(BankAccount) 重写 deposit，用 with self._lock 包住 super().deposit()。题库备注：面试官全程几乎不给 feedback，把沉默当成"继续讲"的信号，别自我怀疑。

2. 现场 Debug（1179868，2026-06-10 电面帖）：楼主原话："白人小哥，45分钟的面试，30分钟coding，15分钟qa"；"coderpad上，share screen，然后选了python现场debug。不是leetcode 题目，就是跑unit test，然后debug 为啥不对。难度是easy。我挂在了最后exception没写好"。15 分钟 QA 问的是怎么做 roadmapping、产品有没有 oncall（对方说还没 deploy 到 prod所以没有 oncall）、刚入职最 shocking 的地方（"不要assume很多都是对的很多是现成的…内部没啥轮子，都要手搓"）。楼主另称"他们的recruiter feedback非常快，每一轮面试协调都是当天回复"。

3. Token Limiter（OJ 题）：ALLOW key cost
...
25 年 10–12 月面试，工程类硕士，内推，Onsite，结果 Pass，全文可见）：流程极快（每轮 24 小时内定下一轮，节假日深夜都排）；Recruiter Call 纯走流程；OA 4 小时倒计时（题型和地里之前报的一模一样，必须开 Cursor 或用 AI 辅助生成 boilerplate，纯手敲写不完；Docker 化那块可以等倒计时结束后再搞）；Coding 手写 parallelized sort；HM 极速深挖简历（盯着最牛的 exceptional project 问技术细节）；Founder/Sell Call 最后确认意向并直接谈 offer

- XAI 全套面经（2025 年 7–9 月面试，MLE 博士，应届，结果 Pass，全文可见）：15 分钟 screen（自我介绍 + 讲简历项目的 data collection 和处理 + 数据 vs 下游任务影响的理解，聊了约 25 分钟，结束 10 分钟后收到过了，不到一小时约好第二天第三天的三轮 tech）；三轮 tech 各 45 分钟：2 轮 coding（动态批处理解码流程、group test gpu 节点找坏节点）+ 1 轮 research；20 分钟 research talk；挂在 offer 阶段；楼主称面试官坦诚"会比较累，80h+"


地里面经题库：43 题（24 hot + 19 OJ，2026-09-12 更新）；hot 首位 Multithreaded BankAccount Race-Condition Bug Hunt（Frequency Low，2026-04-04 还在考，phone-screen/tech-screen）；另有 Token Limiter、Rate Limiter Design、KV Store Design、In-Memory Database Implementation、Design a Restorable (Checkpointable) Iterator、Code Review: Find Issues in an Input Field Implementation、Minimum Time to Produce a Goal Dataset in a Data Pipeline、Twitter Insight Platform with Rate Limiting and Dockerization、Handwrite parallelized sort、Multithread Sorting 等


五、备考建议

1. 15 分钟 screen：准备 2 分钟版 recent projects（覆盖过去两年），go/rust 基础、Kerberos 这类 infra 关键词别被问住；recruiter 那轮聊 past project 也能直接挂人，别水；security clearance 相关问题（是否 comfortable、是否 US citizen）提前想好。
2. 并发是必考：BankAccount race 手写 wrapper/subclass 修法（with lock 包 super().deposit()），Lock vs RLock，Go 的 embedding + sync.Mutex 讲清楚；再练 handwrite parallelized sort。
3. 现场 debug：找陌生代码 + 跑不过的 unit test 限时练，别只刷 LeetCode；exception 处理这种"最后一步"别丢分（6-10 挂经教训）。
4. 从零搭系统：rate limiter / token limiter、KV store、in-memory DB、checkpointable iterator——都要写出能跑的代码，讲清取舍；NG 线现在重 system design（whiteboarding 不许用 AI + implement 可用 AI）。
5. Take-home：DE 岗是 48 小时 pipeline + 15 分钟 live walk-through；OA 4 小时倒计时默认可用 AI 编程工具，把"用 AI 干活"本身练成肌肉记忆。
6. 成就叙事：提前写好 3 条一两句话的 exceptional achievements（技术复杂度/你的职责/impact），这是从 HR 表格一路用到马斯克终审的同一份材料。
7. Project deep dive：30 分钟 PPT + 现场 demo，故事线和演示都要排练；onsite 是和团队一起干大半天，当成"试用期一天"准备。
8. 心态：面试官少 feedback 是常态，沉默时继续讲；流程快但 HC 据称不稳定（NG 帖说法），别在一棵树上吊死。

