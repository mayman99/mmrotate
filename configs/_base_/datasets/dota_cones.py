# dataset settings
dataset_type = 'DOTADataset'
data_root = 'data/blender_proc_sample/'

img_norm_cfg = dict(
    mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True)
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations', with_bbox=True),
    dict(type='RResize', img_scale=(512, 512)),
    dict(type='RRandomFlip', flip_ratio=0.0),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='Pad', size_divisor=2),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_bboxes', 'gt_labels'])
]
test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(
        type='MultiScaleFlipAug',
        img_scale=(512, 512),
        flip=False,
        transforms=[
            dict(type='RResize'),
            dict(type='Normalize', **img_norm_cfg),
            dict(type='Pad', size_divisor=2),
            dict(type='DefaultFormatBundle'),
            dict(type='Collect', keys=['img'])
        ])
]
data = dict(
    samples_per_gpu=1,
    workers_per_gpu=1,
    train=dict(
        type=dataset_type,
        ann_file=data_root + 'trainval/annfiles/',
        img_prefix=data_root + 'trainval/images/',
        pipeline=train_pipeline,
        classes=('void', 'smartcustomizedceiling', 'cabinet/lightband', 'tea table', 'cornice', 'sewerpipe', 'children cabinet', 'hole', 'ceiling lamp', 'chaise longue sofa', 'lazy sofa', 'appliance', 'round end table', 'build element', 'dining chair', 'others', 'armchair', 'bed', 'two-seat sofa', 'lighting', 'kids bed', 'pocket', 'storage unit', 'media unit', 'slabside', 'footstool / sofastool / bed end stool / stool', '300 - on top of others', 'customizedplatform', 'sideboard / side cabinet / console', 'plants', 'ceiling', 'slabtop', 'pendant lamp', 'lightband', 'electric', 'pier/stool', 'table', 'extrusioncustomizedceilingmodel', 'baseboard', 'front', 'wallinner', 'basin', 'bath', 'customizedpersonalizedmodel', 'baywindow', 'customizedfurniture', 'sofa', 'kitchen cabinet', 'cabinet', 'walltop', 'chair', 'floor', 'customizedceiling', '500 - attach to ceiling', 'customizedbackgroundmodel', 'drawer chest / corner cabinet', 'tv stand', '400 - attach to wall', 'window', 'art', 'back', 'accessory', '200 - on the floor', 'beam', 'stair', 'wine cooler', 'outdoor furniture', 'double bed', 'dining table', 'cabinet/shelf/desk', 'single bed', 'classic chinese chair', 'corner/side table', 'flue', 'shelf', 'customizedfeaturewall', 'nightstand', 'recreation', 'lounge chair / book-chair / computer chair', 'slabbottom', 'dressing table', 'desk', 'column', 'dressing chair', 'wardrobe', 'extrusioncustomizedbackgroundwall', 'electronics', 'bunk bed', 'bed frame', 'three-seat / multi-person sofa', 'customizedfixedfurniture', 'bookcase / jewelry armoire', 'mirror', 'wallbottom', 'barstool', 'wallouter', 'l-shaped sofa', 'customized_wainscot', 'door', 'lounge chair / cafe chair / office chair', 'coffee table', 'king-size bed', 'three-seat / multi-seat sofa', 'sideboard / side cabinet / console table', 'loveseat sofa', 'wine cabinet', 'bar', 'shoe cabinet', 'couch bed', 'hanging chair', 'folding chair', 'u-shaped sofa', 'floor lamp', 'wall lamp')
        ),
    val=dict(
        type=dataset_type,
        ann_file=data_root + 'trainval/annfiles/',
        img_prefix=data_root + 'trainval/images/',
        pipeline=test_pipeline,
        classes=('void', 'smartcustomizedceiling', 'cabinet/lightband', 'tea table', 'cornice', 'sewerpipe', 'children cabinet', 'hole', 'ceiling lamp', 'chaise longue sofa', 'lazy sofa', 'appliance', 'round end table', 'build element', 'dining chair', 'others', 'armchair', 'bed', 'two-seat sofa', 'lighting', 'kids bed', 'pocket', 'storage unit', 'media unit', 'slabside', 'footstool / sofastool / bed end stool / stool', '300 - on top of others', 'customizedplatform', 'sideboard / side cabinet / console', 'plants', 'ceiling', 'slabtop', 'pendant lamp', 'lightband', 'electric', 'pier/stool', 'table', 'extrusioncustomizedceilingmodel', 'baseboard', 'front', 'wallinner', 'basin', 'bath', 'customizedpersonalizedmodel', 'baywindow', 'customizedfurniture', 'sofa', 'kitchen cabinet', 'cabinet', 'walltop', 'chair', 'floor', 'customizedceiling', '500 - attach to ceiling', 'customizedbackgroundmodel', 'drawer chest / corner cabinet', 'tv stand', '400 - attach to wall', 'window', 'art', 'back', 'accessory', '200 - on the floor', 'beam', 'stair', 'wine cooler', 'outdoor furniture', 'double bed', 'dining table', 'cabinet/shelf/desk', 'single bed', 'classic chinese chair', 'corner/side table', 'flue', 'shelf', 'customizedfeaturewall', 'nightstand', 'recreation', 'lounge chair / book-chair / computer chair', 'slabbottom', 'dressing table', 'desk', 'column', 'dressing chair', 'wardrobe', 'extrusioncustomizedbackgroundwall', 'electronics', 'bunk bed', 'bed frame', 'three-seat / multi-person sofa', 'customizedfixedfurniture', 'bookcase / jewelry armoire', 'mirror', 'wallbottom', 'barstool', 'wallouter', 'l-shaped sofa', 'customized_wainscot', 'door', 'lounge chair / cafe chair / office chair', 'coffee table', 'king-size bed', 'three-seat / multi-seat sofa', 'sideboard / side cabinet / console table', 'loveseat sofa', 'wine cabinet', 'bar', 'shoe cabinet', 'couch bed', 'hanging chair', 'folding chair', 'u-shaped sofa', 'floor lamp', 'wall lamp')
        ),
    test=dict(
        type=dataset_type,
        ann_file=data_root + 'test/images/',
        img_prefix=data_root + 'test/images/',
        pipeline=test_pipeline,
        classes=('void', 'smartcustomizedceiling', 'cabinet/lightband', 'tea table', 'cornice', 'sewerpipe', 'children cabinet', 'hole', 'ceiling lamp', 'chaise longue sofa', 'lazy sofa', 'appliance', 'round end table', 'build element', 'dining chair', 'others', 'armchair', 'bed', 'two-seat sofa', 'lighting', 'kids bed', 'pocket', 'storage unit', 'media unit', 'slabside', 'footstool / sofastool / bed end stool / stool', '300 - on top of others', 'customizedplatform', 'sideboard / side cabinet / console', 'plants', 'ceiling', 'slabtop', 'pendant lamp', 'lightband', 'electric', 'pier/stool', 'table', 'extrusioncustomizedceilingmodel', 'baseboard', 'front', 'wallinner', 'basin', 'bath', 'customizedpersonalizedmodel', 'baywindow', 'customizedfurniture', 'sofa', 'kitchen cabinet', 'cabinet', 'walltop', 'chair', 'floor', 'customizedceiling', '500 - attach to ceiling', 'customizedbackgroundmodel', 'drawer chest / corner cabinet', 'tv stand', '400 - attach to wall', 'window', 'art', 'back', 'accessory', '200 - on the floor', 'beam', 'stair', 'wine cooler', 'outdoor furniture', 'double bed', 'dining table', 'cabinet/shelf/desk', 'single bed', 'classic chinese chair', 'corner/side table', 'flue', 'shelf', 'customizedfeaturewall', 'nightstand', 'recreation', 'lounge chair / book-chair / computer chair', 'slabbottom', 'dressing table', 'desk', 'column', 'dressing chair', 'wardrobe', 'extrusioncustomizedbackgroundwall', 'electronics', 'bunk bed', 'bed frame', 'three-seat / multi-person sofa', 'customizedfixedfurniture', 'bookcase / jewelry armoire', 'mirror', 'wallbottom', 'barstool', 'wallouter', 'l-shaped sofa', 'customized_wainscot', 'door', 'lounge chair / cafe chair / office chair', 'coffee table', 'king-size bed', 'three-seat / multi-seat sofa', 'sideboard / side cabinet / console table', 'loveseat sofa', 'wine cabinet', 'bar', 'shoe cabinet', 'couch bed', 'hanging chair', 'folding chair', 'u-shaped sofa', 'floor lamp', 'wall lamp')
        )
    )
