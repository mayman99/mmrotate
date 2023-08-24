import io
from flask import Flask, render_template, request, send_from_directory, send_file, jsonify
from PIL import Image
import requests
import os
from flask_cors import CORS, cross_origin
import logging
import base64
import numpy as np

# detector imports
from mmdet.apis import inference_detector, init_detector
import mmrotate  # noqa: F401


app = Flask(__name__)
cors = CORS(app, resources={r"/*": {"origins": "*"}})

# run inference using detectron2
def run_inference(img_path = 'debug_image.jpg'):
    # build the model from a config file and a checkpoint file
    model = init_detector('work_dirs/oriented_rcnn_r50_fpn_1x_dota_le90/oriented_rcnn_r50_fpn_1x_dota_le90.py', 'work_dirs/oriented_rcnn_r50_fpn_1x_dota_le90/epoch_4.pth', device='cuda:0')
    # test a single image
    result = inference_detector(model, args.img)
    return result

@app.route("/")
def index():
	return render_template('index.html')

@app.route("/detect", methods=['POST', 'GET'])
@cross_origin()
def upload():
	content = request.json
	imagebase64 = content['image']
	rgb_im = None
	if request.method == 'POST':
		try:
			imagebase64 = imagebase64.split(";")[1].split(",")[1]
			file = Image.open(io.BytesIO(base64.b64decode(imagebase64)))
			# remove alpha channel
			rgb_im = file.convert('RGB')
			rgb_im = rgb_im.resize((512, 512))
			rgb_im.save('debug_image.jpg')

		# failure
		except:
			return render_template("failure.html")

	if rgb_im:
		result = run_inference(np.array(rgb_im))
        print(result)

	else:
		return render_template("failure.html")

	data = {
		"image": result,
	}

	return data


if __name__ == "__main__":
	logging.getLogger('flask_cors').level = logging.DEBUG
	# get port. Default to 8080
	port = int(os.environ.get('PORT', 8080))

	# run app
	app.run(host='0.0.0.0', port=port)
