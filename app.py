#from flask import Flask, render_template

#app = Flask(__name__)

# Define route for the app's one and only page
#@app.route("/")
#def index():
#    return render_template("index.html")

import os, base64  
from flask import Flask, render_template, request, flash

#from azure.cognitiveservices.vision.computervision import ComputerVisionClient
#from azure.cognitiveservices.vision.computervision.models import ComputerVisionErrorException
#from msrest.authentication import CognitiveServicesCredentials

# Create a ComputerVisionClient instance for calling the Computer Vision API
#vision_key = os.environ["VISION_KEY"]
#vision_endpoint = os.environ["VISION_ENDPOINT"]
#vision_credentials = CognitiveServicesCredentials(vision_key)
#vision_client = ComputerVisionClient(vision_endpoint, vision_credentials)


from azure.cognitiveservices.vision.customvision.prediction import CustomVisionPredictionClient
from msrest.authentication import ApiKeyCredentials


#Create a CUSTOMVISION instance for calling the Computer Vision API

prediction_key = "4abd418beedc45f7a5e2ed9b760445f2"
publish_iteration_name = "classifyModel"
ENDPOINT = "https://sneakerschoose.cognitiveservices.azure.com/"
projectId = "de6aeebf-25be-45f9-9c98-990a0fe7f4b2"


# Create a ComputerVisionClient instance for calling the Computer Vision API
#prediction_key = os.environ["prediction_key"]
#ENDPOINT = os.environ["ENDPOINT"]

prediction_credentials = ApiKeyCredentials(in_headers={"Prediction-key": prediction_key})
predictor = CustomVisionPredictionClient(ENDPOINT, prediction_credentials)



app = Flask(__name__)
app.secret_key = os.urandom(24)


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":

        # Display the image that was uploaded
        image = request.files["file"]
        uri = "data:image/jpg;base64," + base64.b64encode(image.read()).decode("utf-8")
        image.seek(0)

        # Use the Computer Vision API to extract text from the image
        #lines = extract_text_from_image(image, vision_client)
        lines = classification_from_image(image, predictor)

        # Flash the extracted text
        for line in lines:
            flash(line)

    else:
        # Display a placeholder image
        uri = "/static/placeholder.png"

    return render_template("index.html", image_uri=uri)



# Function that extracts text from images
#def extract_text_from_image(image, client):
#    try:
#        result = client.recognize_printed_text_in_stream(image=image)
#        lines=[]

#        if len(result.regions) == 0:
#            lines.append("Photo contains no text to translate")

#        else:
#            for line in result.regions[0].lines:
#                text = " ".join([word.text for word in line.words])
#                lines.append(text)

#        return lines

#    except ComputerVisionErrorException as e:
#        return ["Computer Vision API error: " + e.message]

#    except:
#        return ["Error calling the Computer Vision API"]
    
    
# Function that extracts text from images
def classification_from_image(image, predictor):
    results = predictor.classify_image(projectId, publish_iteration_name, image.read())
    lines=''

    for prediction in results.predictions:
        lines += "\t\t\n" + prediction.tag_name + " : {0:.2f}% ".format(prediction.probability * 100)
        
        #type string=> mettre en format list pour que la mise en forme soit correcte sur le site
        list_lines=[lines]
    return list_lines
    

