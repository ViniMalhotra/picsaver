# Picsaver
Link to my web app:
http://ec2-13-58-251-156.us-east-2.compute.amazonaws.com/first/
<br>

This is an application used to save Pictures and details of the tourist places you visited. Add the pictures, store them for later and delete them if 
you want to.
<br>
<b>Technologies used:</b>
<br>
1)Django 2.2.1 
2)Python 3.6
3)nginx
4)gunicorn
5)Ubuntu AMI
6)Bootstrap
7)Github

<br>
<b>Instructions on How to access the app : </b><br>
(1)	This is the index page of website which can be accessed through :<br>
http://ec2-13-58-251-156.us-east-2.compute.amazonaws.com/first/
Hit the “click here to add pictures” button<br>
(2)	It opens the form to take user input. Here 'one' is default value of description, in case you do not want to add description. <br>
(3)	hit The" choose file" button to add any picture from your computer and hit submit button <br>
(4)	Your contents are displayed on screen and saved to database<br>
(5)	Hit "PicSaver" in navbar to view your newly added item.<br>
6)	Hit the delete button to delete the item.<br>
7)	Each item in list is a link which will take you to the details page of the item<br>

<b>References: </b><br>
<b> For building Django project: </b><br>
https://www.youtube.com/watch?v=qgGIqRFvFFk&list=PL6gx4Cwl9DGBlmzzFcLgDhKTTfNLfX1IK
<br>
https://www.youtube.com/watch?v=s0RX_YU9eJM&t=503s
<br>
https://www.youtube.com/watch?v=Kg29bvYyLSM
<br>
<b>Problems faced:</b><br>
Learning Django framework from scratch. I had to refer multiple sources to initially get my app working on local machine,  then deploy it on EC2 instance.
I realized Django makes it easy for the front end developer and backend to work on the same project. The model view template architecture helps to bifurcate the tasks<br>.<br>
<b> For learning Github: </b><br>
https://www.youtube.com/watch?v=6pAXylqATB0&t=148s
Github was a rather easy task but very useful
<br><br>
<b> For using nginx with gunicorn to deploy Django app on ec2 instance</b>
<br>
<br> These links guided me to set up nginx (Nginx is a web server which can also be used as a reverse proxy, load balancer, mail proxy and HTTP cache )and gunicorn(Python WSGI http server)

https://www.youtube.com/watch?v=QjrfUO91wfc
<br>
https://www.youtube.com/watch?v=08yYjLGWzaM&t=46s
<br>
Using nginx was the most difficult tasks. The references I use did not completely help me. There were many changes I had to do. 
<br> 
1)	Primarily, to use ec2 instance, in the Django project ,settings.py file has to be configured. The public dns name should be added to allowed host in settings.py.<br>
2)	Gunicorn and nginx have many dependencies which needed to be downloaded.
Starting up gunicorn the gunocrn.service file needs to be configured. The working directory and execution directory should be set up carefully and correctly else the deamon won’t start. I had not set up the user as Ubuntu which is the AMI I used, took me a lot of errors to figure out that.<br>
3)Inside nginx sites-available file, our server port, server name, proxy needs to be set. 
I ahd to change the configuration file to increase the length of the server name it can store as the public dns name is quite long. This error didn’t allow me to start nginx. It took a lot of resources to figure out how to actually change configuration. <br>
Then, I started  nginx service and everything in backend worked efficiently and I could access my app.<br>





