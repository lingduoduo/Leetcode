整理了 4 篇 2026 年 NVIDIA 实战面经 + 4 篇补充资料（约面慢、C++ 吐槽、双 offer 选择、Day1 CPT 被撤 offer），以及地里面经题库 NVIDIA 专区（68 题 + 48 OJ，题库页 2026-09-12 更新）。先说结论：NVIDIA 2026 年的面经材料偏薄（实战帖只有 4 篇），但题库很实在——免费预览的 hot 题就是"FP32 转 Int8 量化"（含 5 个 follow-up），OJ 里全是 C++/系统/推理基本功。8 篇全部登录打开核验，无积分墙，题面引用楼主原话。

一、流程概览

- 网申（Workday 系统）/ 内推 → recruiter（给的背景信息很少，经常不说一共几轮、每轮考什么）→ 技术店面/电面（1–2 轮）→ panel VO → offer。
- 流程慢是共识：有楼主"三天了都还没约好初面时间"，投简历是两个月前；有人"两轮店面隔了一个月"，"从 hiring manager 面完到通知下一轮 45 分钟的面试，隔了一个月"；还有人面完两轮后石沉大海，最后在 Candidate Center 看到职位被填满。
- 面试风格 team-specific：有楼主称"他们组的面试对每个人面试内容并没有固定框架，更多是让组里的不同成员和候选人聊聊，看看感觉如何"；题库页也写"highly team-specific and much less LeetCode-bank-driven"。
- 语言：C++ 是主流（AV 组全程 C++，含 smart ptr、inheritance debug）。
- 注意：2026-9-18 有楼主称 NVIDIA HR 说公司"最近几周才开始不支持 CPT，之前都是可以的"——Day1 CPT 身份的要提前和 HR 确认签证政策。

二、高频题

1. FP32 Tensor to Int8 Quantization——题库 hot 题（免费预览，Coding 60 分钟，phone-screen，medium，tags SWE/MLE/Perf Eng/numpy/inference/numerical-stability，Last asked 2026-02-12）。Base：实现 def quantize_fp32_to_int8(x: np.ndarray, scale: float) -> np.ndarray——FP32 tensor 任意 shape，每个值除以 scale，四舍五入后 cast 到 int8 范围 [-128, 127]，返回同 shape tensor。5 个 follow-up（题库全部列出）：(1) 加 zero_point 参数做 asymmetric quantization；(2) 解释 symmetric quantization 什么时候不够用；(3) 推导 scale 和 zero_point 如何配合使用；(4) 讨论值超出 [-128, 127] 时的 clipping/saturation；(5) 解释输入分布 skewed 或有 outlier 时 error 会怎样。公式：q = clamp(round(x / scale) + zero_point, qmin, qmax)；x_hat = scale * (q - zero_point)。题库备考建议：用 NumPy 实现 base，再加 zero_point、clipping、dequantization；手算 x=[-1.0, 0.0, 1.0]、scale=0.1；per-tensor vs per-channel scale；activations 通常比 weights 更难量化。

2. Merge 2 sorted lists + 分布式 follow-up——"女大店面"（2026-8-11，匿名，硕士，内推，在职跳槽，Pass）：楼主原话"easy 题： 类似merge 2 sorted lists，2 pointers秒了。followup很多 都是distributed system知识 乱答一通 很多答案其实不确定 也不知道怎么就过了。

...

OJ 含 "Implement a Reference-Counted Smart Pointer"、"Top K Frequent Elements in a Data Stream"、"Merge Two Sorted Files with Bounded Memory"、"Implement a Decoder KV Cache"、"Linux Shell Scripting Task (Text/Log Processing)"、"Graph API: Insert/Configure/Validate with Cycle Detection"、"Computation Graph Pruning to Keep the Optimal Path" 等

...

量化题原题页：

五、备考建议

1. 量化基本功：FP32→Int8 手写到熟（NumPy 实现 + zero_point + clipping + dequantization），5 个 follow-up 全准备；per-tensor vs per-channel；activations 更难量化。
2. C++：smart ptr 手写、inheritance debug、多线程/指针输出预测；AV 组全程 C++。
3. 系统基本功：超大文件 merge（bounded memory）、streaming top K（堆 vs 桶 O(1)）、decoder KV cache、computation graph pruning。
4. Linux/shell：文本/日志处理脚本；SQL 表设计（伪代码也可能考）。
5. SD：camera pipeline、perception system（AV 组）；distributed system follow-up（大文件排序与存储）。
6. 流程心理准备：NVIDIA 流程慢是常态，约面和等反馈都可能以月计；recruiter 经常不透露轮次和内容；面完没消息不一定是挂，也可能是 headcount filled——多线并行。


