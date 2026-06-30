一、Coding
ACL / 权限系统 高频
grant_access(advertiser, group) / check_access(advertiser, group) / revoke_access(advertiser, group)
有一批 advertiser，和一个层级结构的 group:
  World → Country → City

例:
  World
  ├── US
  │   ├── San Francisco
  │   ├── New York
  │   └── Los Angeles
  └── UK
      ├── London
      └── Manchester

功能:
  grant_access(advertiser, group): 给 advertiser 授权访问 group
  check_access(advertiser, group): 检查 advertiser 是否有权访问 group
  revoke_access(advertiser, group): 撤销 advertiser 对 group 的访问权

关键规则:
  - 授权是继承的: grant_access("Nike", "US") → Nike 可以访问 US 下的所有 city
  - check_access("Nike", "San Francisco") → True (因为 Nike 有 US 的权限)
  - revoke 只撤销精确的那个 grant，不影响上级的 grant

大概是这样，原帖也没有详细说，找ai 重新整理的
LC 815 — Bus Routes 高频
Escape Room 高频
LC 1055 — Shortest Way to Form String 高频
LC 332 — Reconstruct Itinerary 高频
Pixie-like walk
Expression Add Operators 简化版
2+3*2 等效于 (2+3)*2，operator 从左到右结合，算过就定下来
LC 426 — Convert BST to Doubly Linked List
Follow-up: insert a new node
LC 465 — Optimal Account Balancing
字符串前缀题
['a', 'apple', 'appz', 'b'] 和 ['ap'] — find the index of 1st word containing prefix
思路：zip_longest('ap', 'apple', fillvalue='#')
LC 84 — Largest Rectangle in Histogram (monotonic stack, hard)
LC 392 — Is Subsequence (two pointers, easy)
Follow-up: 预计算索引 + 二分（类似 LC 1055）
采样
softmax → categorical distribution → CDF + uniform sampling → 二分查找
LC 3229 和 LC 1526 — Minimum Operations to Make Array Equal
LC 1723 — Find Minimum Time to Finish All Jobs
LC 1564 / 1580 — Put Boxes Into Warehouse I / II