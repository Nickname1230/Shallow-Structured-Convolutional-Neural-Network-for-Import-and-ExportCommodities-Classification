# Shallow-Structured-Convolutional-Neural-Network-for-Import-and-ExportCommodities-Classification

浅层卷积神经网络，利用Pad浅层卷积操作，避免卷积过程中破坏结构化文本的结构语义信息，并依靠辅助网络提取决定性的分类特征，在真实中国海关商品进出口报关单商品编号分类任务中，结果优于BERT以及RoBERTa。

使用时应确保您的数据是结构化的，具有层次分类的。

您应该首先使用数据的父类进行数据分割，接着利用TextCNN或其他模型进行同一父类下，子类的分类任务，最终得到各个父类下结构化要素针对分类的重要性排序，形如data/loss_record

使用train.py进行最终的分类实验，模型选择SSCNN。

