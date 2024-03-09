# model settings
model = dict(
    type='ImageClassifier',  # 所有的“type”都可以在mmpretrain中找到源码定义的类
    backbone=dict(
        type='ResNet',
        depth=18,
        num_stages=4,
        out_indices=(3, ),  # 输出第几层的特征图，数字越大特征图越小，从0开始，可以人为设定组成金字塔等
        style='pytorch'),
    neck=dict(type='GlobalAveragePooling'),
    head=dict(
        type='LinearClsHead',
        num_classes=1000,
        in_channels=512,
        loss=dict(type='CrossEntropyLoss', loss_weight=1.0),
        topk=(1, 5),  # 评估方法
    ))
