python 版本2.7及以上 将获取到的中文文章生成唯一的hash标识符，用来判断文章之间的相似度。
原理是分词，词权重，词出现的频率，词的顺序。通过md5生成唯一字符串，经过计算统一生成一个32位的hash值。分词用到的的是结巴分词。
文章相似度判断 对比两个文章的唯一hash值 得到海明距离值，海明距离最小为0，最大32.距离越小代表文章相似度越高。
运用场景，用来平台处理类型文章，文章查重。