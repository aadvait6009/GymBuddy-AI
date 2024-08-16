Bicep Curl Counter: Your New Workout Buddy
Hey! 👋

So, I put together this cool little project that I thought you might like. It’s an AI-powered Bicep Curl Counter that uses your webcam to count your reps as you work out. Yep, no more trying to keep track in your head—let the computer do it for you!

What’s the Deal?
Imagine this: you’re doing your bicep curls, and as you move, the app is right there with you, counting each rep and even showing you the angle of your elbow. It’s super simple but also kinda neat. Perfect if you’re into fitness and tech like me.

What You’ll Need
Before you get started, here’s what you’ll need:

Python 3.7 or higher: This is the programming language we’re using. If you don’t have it, no worries—it’s easy to install.
A webcam: You’ll need this so the app can "see" you. If you’re on a laptop, you probably already have one. If not, any basic external webcam will do.
Getting Set Up
Grab the Code:
First things first, you need to download the project. If you know how to use Git, run this:

bash
Copy code
git clone https://github.com/aadvait6009/GymBuddy-AI.git
cd GymBuddy-AI
Set Up a Virtual Environment (Optional but Handy):
This step isn’t required, but it’s a good idea if you want to keep things tidy, especially if you have other Python projects. Here’s how:

bash
Copy code
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install the Goodies:
Now, you’ll want to install all the necessary libraries. It’s super easy—just run:

bash
Copy code
pip install -r requirements.txt
How to Use It
Fire It Up:
Time to get things rolling. Just run the main script:

bash
Copy code
python bicep_curl_counter.py
Pick Your Arm:
A little window will pop up asking whether you’re working out your left or right arm. Click your choice, and you’re all set.

Start Curling:
Now, just do your thing! As you curl, the app will count your reps and show you the angle of your elbow. It’s like having a little coach in your computer.

Finish Up:
When you’re done, just press the ` key (backtick) on your keyboard to close the app. Easy peasy.

What’s Inside?
Here’s a quick rundown of what’s in the project:

bicep_curl_counter.py: This is the main script that makes everything work.
requirements.txt: This file lists all the Python libraries you need to install.
Background.png: The background image for the loading screen.
load.gif: A fun GIF that plays while the app is loading.
Want to Help Make It Better?
Got some cool ideas or found a bug? I’d love to hear from you! Feel free to fork the project, make your changes, and send over a pull request. Let’s make this even better together.

License
By the way, this project is under the MIT License, which means you can do pretty much whatever you want with it. Just remember to give me a shoutout if you end up using it in something cool!
