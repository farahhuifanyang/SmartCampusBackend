## Smart Campus “智慧校园”学者画像系统

本系统对多源数据进行分析，使用实体消歧、数据融合等文本分析方法和社团发现等数据挖掘方法，对学者和机构进行建模，多维度挖掘学者的深层学术信息。系统通过展示学者详细的个人信息、丰富的合作关系、传承的学术谱系、六度搜索路径、关键人物的发现与替代等功能，刻画更真实、更准确、更立体的科研学者，为专家遴选、学术热点分析等提供数据支持。

<img src=".\assets\function.png" style="zoom:80%;" />

### 系统展示

<img src=".\assets\demo.png" style="zoom:65%;" />

<img src=".\assets\demo2.png" style="zoom:65%;" />

### 接口

目前后端部署在`lemon`(`10.112.181.126`)的2333端口。

根据id/名字获取基本信息：

http://lemon:2333/scholar/basic_info?name=汪晓春
或
http://lemon:2333/scholar/basic_info?scholar_id=233
```json
{
    "sid": 233,
    "chinese_name": "汪晓春",
    "gender": "男",
    "department": "数字媒体与设计艺术学院",
    "center": "工业设计教研中心",
    "title": "副教授",
    "degree": "博士",
    "job": "null",
    "field": "老龄设计、信息产品创新设计、技术与设计",
    "organization": "北京邮电大学",
    "introduction": "汪晓春，副教授，硕士生导师，工业设计教研中心教师。于2006年9月-2007年9月，美国辛辛那提大学设计、建筑、艺术与规划学院，设计与创新研究中心访问学者。导师为美国前工业设计师协会（IDSA）主席Craig M Vogel 教授。期间研究方向为设计策略，设计方法。",
    "thanks_paper": "null",
    "mag_paper": "null",
    "co_scholar": "null",
    "keywords": "null"
}
```
根据id/名字获取头像：

http://lemon:2333/scholar/avatar?name=吴斌
或
http://lemon:2333/scholar/avatar?scholar_id=139


根据名字查询学生
http://lemon:2333/scholar/teacherstudents?name=吴斌
```json
{
    "teacher": "吴斌",
    "students": [
        "项汉忠",
        "苏雪峰",
        "张艳秋",
        "索利军"
    ]
}
```

根据名字查询论文
http://lemon:2333/scholar/papers?name=吴斌
```json
{
  "scholar": "吴斌",
  "papers": [
    {
      "url": "https://link.springer.com/chapter/10.1007/978-3-319-25660-3_7/fulltext.html,https://link.springer.com/content/pdf/10.1007%2F978-3-319-25660-3_7.pdf,http://dblp.uni-trier.de/db/conf/pakdd/pakdd2015-w.html#WangWLWW15,http://dl.acm.org/citation.cfm?id=2961609,https://doi.org/10.1007/978-3-319-25660-3_7,http://link.springer.com/chapter/10.1007/978-3-319-25660-3_7/fulltext.html,https://link.springer.com/chapter/10.1007/978-3-319-25660-3_7,http://dl.acm.org/citation.cfm?id=2961601.2961609,http://link.springer.com/chapter/10.1007/978-3-319-25660-3_7,http://link.springer.com/content/pdf/10.1007%2F978-3-319-25660-3_7.pdf,http://dx.doi.org/10.1007/978-3-319-25660-3_7,http://link.springer.com/10.1007/978-3-319-25660-3_7",
      "volume": null,
      "fos": "Computer Science,Data science,Machine learning,Data mining,World Wide Web",
      "issue": null,
      "year": 2015,
      "authors": "Pengsen Wang,Bin Wu,Xiaoming Li,Lin Wang,Bai Wang",
      "lang": "en",
      "doc_type": null,
      "page_end": "90",
      "publisher": "Springer, Cham",
      "n_citation": null,
      "abstract": "Citation matching is to find the cited papers according to only a small amount of information. There have been some works on citation matching. Most of the solutions require expensive model processing to achieve good results. However, when dealing with millions of citations in large digital libraries, these solutions may not be efficient enough. To address this problem, we propose a simhash-based generalized framework in MapReduce for citation matching. In the framework, we use title exact matching and distance-based short text similarity metrics to implement citation matching. Moreover, customizing citation fields, citation field weights and word segmentation weights are used for improving the accuracy. We also design a heuristic algorithm which can automatically calculate the weights of each citation field. For disposing the large-scale datasets, we implement the framework in Hadoop, a popular parallel computation platform. We do our experiments with real datasets from a Chinese Medicine Digital Library, and a comparative experiment with Cora corpus McCallum's citation matching test set. The results of experiments confirm the efficiency and effectiveness of our framework.",
      "venue": "knowledge discovery and data mining",
      "page_start": "78",
      "doi": "10.1007/978-3-319-25660-3_7",
      "title": "A Simhash-Based Generalized Framework for Citation Matching in MapReduce",
      "id": "0411f6fc-f1bc-41d8-b6bb-6e78fb682478",
      "keyword": "citation matching,short text similarity,parallelization,mapreduce"
    }
  ]
}
```