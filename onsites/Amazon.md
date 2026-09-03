ML Breadth. 面试官是个还挺nice的天竺大哥，这一部分问很多基础的问题，比如：
1)  什么是p-value？
2） 什么是overfitting and underfitting, 怎么解决？
3） 什么是causal inference？有什么方法？
4） 什么是encoding and decoding
5） Explain gradient descent and backpropagation。
6） Explain gradient vanishing/exploding, how to mitigate them?
7） 怎么处理highly imbalanced data问题
8） Describe a scenario that you have a high accuracy 99%  but model performance is still bad, how would you tackle it?
9） 什么是A/B test? 如果A/B test发现异常，可能有哪些原因？

--- 

- Explain the complete RAG architecture. How would you build it from scratch?
- What are embeddings? Which embedding models have you used, and how do you choose one?
- Compare vector databases such as Pinecone, Chroma, FAISS, Milvus, and Weaviate.
- Difference between LangChain, LlamaIndex, LangGraph, and CrewAI. When would you choose each?
Explain AI Agents, multi-agent systems, and supervisor-agent architecture.
What is function calling/tool calling? How is it implemented in OpenAI or LangChain?
What is MCP (Model Context Protocol)? Why is it gaining popularity?
How do you optimize LLM latency and reduce inference costs?
Explain prompt engineering techniques such as Zero-shot, Few-shot, Chain of Thought, Self-Consistency, ReAct, and Tree of Thoughts.
How do you evaluate an LLM application? Explain RAGAS, DeepEval, Precision, Faithfulness, Context Precision, and Answer Relevancy.
How do you prevent hallucinations in a RAG application?
Explain chunking strategies: Fixed, Recursive, Semantic, Parent-Child, and Hybrid Chunking.
What are MMR (Maximum Marginal Relevance) and RRF (Reciprocal Rank Fusion)?
What is KV Cache? Explain speculative decoding and continuous batching.
Difference between synchronous, asynchronous, multithreading, multiprocessing, and parallel processing in Python.
Build a FastAPI endpoint to invoke an LLM asynchronously. Explain GET vs POST methods.
How do you secure an enterprise GenAI application? Discuss PII masking, prompt injection, jailbreak protection, RBAC, guardrails, and content moderation.
Explain LLM fine-tuning, LoRA, QLoRA, PEFT, and RLHF. When would you fine-tune instead of using RAG?
How would you monitor an LLM application in production? Which metrics would you track?


2. Coding 是刷题网幺儿期。这部分只有15分钟左右，没想到出了一道hard题。之前没刷到这道题，而且没想到这是一道graph的题，所以让天竺大哥给点提示，大哥说你就直接暴力解吧。然后我大概讲了下思路，大概只写了1/3的codes，然后就没时间了。

因为coding没做完，以为要挂了，结果过了半小时recruiter通知我pass了。Recruiter说，applied scientist对ML要求比较高，需要raise bar, 但是对coding要求只需要达到SDE 1的水平就行了。Recruiter把天竺大哥给我的comments念给我听了，说ML部分很strong, coding部分能比较好的沟通解题思路。看来没写完codes也不要泄气，跟面试官保持沟通，把解题思路说明白很重要。

手写sigmoid, softmax, attention 
attention/transformer 

code: maze 是否可以从起点走到终点 1 1 0 这样的maze 1 表示能通行，0表示不能通行。我说能用bfs 和dfs

第一轮  
南亚人，考察science depth，问简历上的PEFT相关内容，vLLM inference image text怎么embedding，问得很深入。回答得不是很好，没时间做coding。

第二轮  
国人小哥，考察science breadth，主要是简历上的问题，交流顺畅，几乎每个问题都答得挺好（自我感觉）。30分钟coding，题目是合并间隔，利口能找到，只是没有test case，你也不能run，只能他告诉你对错，有个typo，提示后通过。

Project 1：搜索排序（Search Ranking）
主要围绕以下几个方面展开：
为什么要做这个项目？业务痛点是什么？
你本人承担了哪些职责？哪些决定是你做的？
为什么选择当前模型，而不是其他方案？
如何定义成功？主要 Offline 和 Online Metrics 是什么？
A/B Test 如何设计？
如果线上效果没有达到预期，你会如何排查？
项目中最大的技术挑战是什么？最终如何解决？
如果重新做一次，你会有哪些改进？
整个过程追问比较深，不仅关注模型，也关注业务思考和实验设计。

题目：Morse Code编解码器，4个递进的part：
基础编码：字符→莫斯码
基础解码：莫斯码→字符（带分隔符）
无分隔符解码：给定词汇表约束，从连续莫斯码中恢复单词
无分隔符解码多个单词：用回溯法枚举所有合法的单词组合
关键思路：Part 3和4的核心是先把词汇表预处理成 morse_pattern → set(words) 的mapping，然后用backtracking递归。
楼主4个part都做出来了。面试官Ori全程比较安静，但结束时说"most candidates don't finish Part 4"。
店面第二轮 — Tensor Programming
过了，具体题目记不太清了，主要考GPU相关的概念性问题和简单实现。


Final 面试流程

第一轮  
国人帅气小哥，30分钟简历相关问题，深入问项目细节；30分钟考察亚麻leadership问题。
第二轮  
不确定哪国人，感觉是bar riser，60分钟全是亚麻leadership问题。语言沟通不太顺畅，回答得不是很好。
第三轮  
国人小哥，30分钟science breadth问题，大多数都是MLE相关，涉及bias、variance之类，很简单，再30分钟行为面试（BQ）。
第四轮  
南亚人，他应该是HM，问了很多关于如何用Agentic AI优化他们项目的方案。自我感觉回答很好。
第五轮  
欧洲人，30分钟行为面试（BQ）（感觉也答得不错），30分钟coding。题目似乎不是leetcode上的，是写个code返回经理的员工中平均工资最高的人，这个很简单，我用dict。又问返回一个经理把所有直接下属员工工资的平均值，时间不够，我讲了思路，他提示应该用树结构。

---

Round 1: Coding — Schema Validation
60分钟。题目是实现一个schema validation系统，给一个JSON-like的数据结构和一个schema定义，验证数据是否符合schema。需要递归处理嵌套结构。
楼主用了dataclass来建模schema，花了不少时间在设计上，核心递归逻辑写对了但边界情况没全部cover完。面试官是个Principal SDE，全程比较严肃。
Round 2: Project Deep Dive + Behavioral（HM轮）
和HM聊了做过的项目，主要讲了agent runtime和eval pipeline的经历。HM问了是否有distributed systems经验——坦白说没有太多，这可能是减分项。Amazon LP相关的BQ也穿插在里面。
Round 3: Paper Read — DeepSeek-V3 Technical Report
这轮很有意思。提前48小时给了论文，面试时做30-35分钟的技术讨论 + 20-25分钟behavioral。
楼主准备了7点框架：Problem → Key Idea → Architecture → Why These Choices → Evidence → Limitations → Production Translation。
讨论了MLA（Multi-head Latent Attention）、Aux-Loss-Free MoE、MTP（Multi-Token Prediction）、DualPipe等核心创新。面试官主要追问"为什么这么设计"和"在生产环境中怎么用"。
Round 4: System Design — 分布式数据处理Pipeline
设计一个用于训练数据预处理的分布式pipeline。楼主画了比较完整的架构图（S3 → Kafka → tokenizer → dedup → quality filter → output），但被追问时在tradeoff justification上不够深。面试官是Principal SDE，期望听到"哪里会break at scale"和"为什么选Kafka而不是X"这类深度分析。
最终结果：挂了。 没有给具体feedback。猜测原因：coding轮不够强 + 缺少distributed systems经验 + system design没有足够展示Staff级别的depth。

欧洲人，30分钟行为面试（BQ）（感觉也答得不错），30分钟coding。题目似乎不是leetcode上的，是写个code返回经理的员工中平均工资最高的人，这个很简单，我用dict。又问返回一个经理把所有直接下属员工工资的平均值，时间不够，我讲了思路，他提示应该用树结构。
coding。 1. merge intervals 2. Top K Frequent Element

science depth：
问了之前的实习项目，然后问 LLM 的基础八股，BQ。
transformer, attention, diffusion, image generation, LLM
case study: how would you evaluate generation quality (image or text), if the image is for brand ads, how do you make sure the brand name is right in the image, etc.
1 LP question: Dive Deep ; Think Big

science application：
全程 LLM 八股（比较有深度，个人认为如果不是NLP背景的很难答好），BQ。
问了flashattn, lora, RNN, RLHF, 面的很细比如GRPO/GSPO区别
问了很多关于如何用Agentic AI优化他们项目的方案。自我感觉回答很好。
第一轮是 Statistics Application。现在有两组用户数据，一组是北美用户，一组是欧洲用户，每个用户都有多维连续特征（比如停留时长、点击率、购买转化率等等），问你怎么判断这两个群体在“整体分布”上有没有显著差异。

science breadth：
ML system design/case study，与 search/ranking/experimentation 相关，BQ。
Traditional ML (CNN, logistic regression, etc.)
1 LP question: Invent and Simplify
国人小哥，30分钟science breadth问题，大多数都是MLE相关，涉及bias、variance之类，很简单，再30分钟行为面试（BQ）。

---

It's more on statistics (precision & recall, AUC, ROC)

手写sigmoid, softmax, attention, transformer

flash attn, lora, RNN, RLHF, 面的很细比如GRPO/GSPO区别，

transformer, attention, diffusion, image generation, LLM

LoRA及各种变体
RL相关的一些
KV cache
positional encoding
Flash attention等等

LLM 八股, 比如为什么要做tokenization 能不能用26个字母做tokenization之类的，SFT里能不能加KL 怎么加之类的。

---

第一轮  
南亚人，考察science depth，问简历上的PEFT相关内容，vLLM inference image text怎么embedding，问得很深入。回答得不是很好，没时间做coding。

第二轮  
国人小哥，考察science breadth，主要是简历上的问题，交流顺畅，几乎每个问题都答得挺好（自我感觉）。30分钟coding，题目是合并间隔，利口能找到，只是没有test case，你也不能run，只能他告诉你对错，有个typo，提示后通过。

---

Audiable

we want to detect "abusive books" in a stream of user read event.
event looks like this: <user_id, book_id, current_pos_in_sec, book_duration_sec>
an event is abusive if:
# (1) user reached the last 5% of book_duration_sec (e.g. only consider​ those who almost complete the ntent)
# (2) when (1) happens, same user hasn't completed 10% of book_duration_sec (e.g. abusive books is ring, so people skip ahead)
a book is considered "abusive" if abusive_event_ratio > 20%
given stream of event:
readBook(user_id, book_id, current_pos_sec, book_duration_sec>
write a solution to detect "abusive books"
感觉理解了题意，一半时间也过去了。。。 大致思路是用global cache来存<(user_id, book_id): progress_sec>, <book_id: (abusive_event_cnt, total_event_cnt)>, 有聊到top k，被告知不用考虑；问了如何event可以重复么，答可以假设不重复，因为没有时间了；聊了atom counter，写了个pseudo function，没有implement lock 或者 atomic incrementer


