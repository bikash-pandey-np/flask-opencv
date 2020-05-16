from flask import Flask, render_template, Response, request, url_for, redirect
import cv2

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get_camera_content', methods = ['POST'])
def get_camera():
	if request.method == "POST":
		
		capture = cv2.VideoCapture(0)

		while True:
			ret, frame = capture.read()

			cv2.imshow('frame',frame)
			if cv2.waitKey(1) & 0xFF==ord('q'):
				break

		capture.release()

		cv2.destroyAllWindows()

		
		return redirect(url_for('index'))
	



if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)
