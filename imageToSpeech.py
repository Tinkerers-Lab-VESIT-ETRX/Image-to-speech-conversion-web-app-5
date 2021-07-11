from flask import Flask, render_template, request
from pytesseract import pytesseract
import cv2, os
from gtts import gTTS
#from playsound import playsound

pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

app = Flask(__name__)
UPLOAD_FOLDER = os.path.basename('.')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':
        if 'image' not in request.files:
            return 'there is no image in the form'
        image = request.files['image']
        f = os.path.join(app.config['UPLOAD_FOLDER'], image.filename)
        image.save(f)
        dang = cv2.imread(UPLOAD_FOLDER+"/"+image.filename)
        os.remove(UPLOAD_FOLDER+"/"+image.filename)
        myText = pytesseract.image_to_string(dang)
        print(myText)
        language = 'en'
        output = gTTS(text=myText, lang=language, slow=False)
        output.save("output.mp3")
        os.system("start output.mp3")
        #playsound("output.mp3")
        return myText
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)