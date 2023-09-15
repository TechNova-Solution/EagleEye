EagleEye Project

Benford's Law is an observation about the leading digits of the numbers found in real-world data sets. Intuitively, one might expect that the leading digits of these numbers would be uniformly distributed, so that each of the digits from 1 to 9 are equally likely to appear. In fact, it is often the case that 1 occurs more frequently than 2, 2 more frequently than 3, and so on. This observation is a simplified version of Benford's law. More precisely, the law gives a prediction of frequency of leading digits using base-10 logarithms that predicts specific frequencies which decrease as the digits increase from 1 to 9.

This phenomenon occurs generally in many different instances of real-world data. It becomes more pronounced and more likely when more data is combined together from different sources. Not every data set satisfies Benford's law, and it is surprisingly difficult to explain the law's occurrence in the data sets it does describe, but nevertheless it does occur consistently in well-understood circumstances. Scientists have even begun to use versions of the law to detect potential fraud in published data (tax returns, election results) that are expected to satisfy the law.

The process for running the app locally 
- Flask is a small and lightweight Python web framework that provides useful tools and features that make creating web applications in Python easier. It gives developers flexibility and is a more accessible framework for new developers since you can build a web application quickly using only a single Python file. Flask is also extensible and doesn’t force a particular directory structure or require complicated boilerplate code before getting started.
#step 1 You'll activate your Python environment and install Flask using the #pip package installer.
If you haven’t already activated your programming environment, make sure you’re in your project directory (simple_flask_app) and use the following command to activate the environment source venv/Scripts/activate
Once your programing environment is activated, your prompt will now have an #venv prefix that may look as follows: (venv)ary@localhost:$
this prefix is an indication that the environment venv is currently active, which might have another name depending on how you named it during creation 
Now you’ll install Python packages and isolate your project code away from the main Python system installation. You’ll do this using pip and python.

To install Flask, run the following command:
(venv)ary@localhost:$ pip install flask
Once the installation is complete, run the following command to confirm the installation
(venv)ary@localhost:$ python -c "import flask; print(flask.__version__)"

Step 2- Creating a base application 
Now that you have your programming environment set up, you’ll start using Flask. In this step, you’ll make a small web application inside a Python file and run it to start the server, which will display some information on the browser.

In your simple_flask_app directory, open a file named hello.py for editing
(venv)ary@localhost:$ python hello.py
This hello.py file will serve as a minimal example of how to handle HTTP requests. Inside it, you’ll import the Flask object, and create a function that returns an HTTP response. Write the following code inside hello.py:
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'
    Save and close the file.
    