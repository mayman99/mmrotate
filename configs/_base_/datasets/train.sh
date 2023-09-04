pip install -U openmim
mim install mmcv-full
mim install mmdet\<3.0.0
apt-get install ffmpeg libsm6 libxext6  -y
git clone https://github.com/mayman99/mmrotate.git
cd mmrotate
pip install -v -e .
mim download mmrotate --config oriented_rcnn_r50_fpn_1x_dota_le90 --dest .
python demo/image_demo.py demo/demo.jpg oriented_rcnn_r50_fpn_1x_dota_le90.py oriented_rcnn_r50_fpn_1x_dota_le90-6d2b2ce0.pth --out-file result.jpg
python tools/train.py configs/oriented_rcnn/oriented_rcnn_r50_fpn_1x_dota_le90.py
python demo/image_demo.py data/blender_proc_sample/trainval/images/4.png work_dirs/oriented_rcnn_r50_fpn_1x_dota_le90/oriented_rcnn_r50_fpn_1x_dota_le90.py work_dirs/oriented_rcnn_r50_fpn_1x_dota_le90/epoch_30.pth --out-file result.jpg
python demo/image_demo.py data/oobb_cones_dota/trainval/images/15.png work_dirs/oriented_rcnn_r50_fpn_1x_dota_le90/oriented_rcnn_r50_fpn_1x_dota_le90.py work_dirs/oriented_rcnn_r50_fpn_1x_dota_le90/epoch_8.pth --out-file result.jpg