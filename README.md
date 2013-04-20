mymedia
=======

**Go here for a video walkthrough of the steps below: http://youtu.be/QgHu_O3SgxQ **

MyMedia is a simple REST API implemented with Django REST Framework - http://django-rest-framework.org/.

The following end points are available from this API:
	/
	/users
	/media

To get started with this basic Django app, please follow along.

1. Clone the repository to your local machine.
	<pre><code>git clone https://github.com/aalittle/mymedia.git</code></pre>

2. Change directories into the cloned repository.
    <pre><code>cd mymedia</code></pre>

3. The first thing you will need to do is install pip. If you have setuptools installed, which you most likely will with most modern platforms, you can install pip through easy_install:
    <pre><code>easy_install pip</code></pre>
	
4. Next, you'll need to install virtualenv with pip:
    <pre><code>pip install virtualenv</code></pre>

5. Before we do anything else we'll create a new virtual environment, using virtualenv. This will make sure our package configuration is kept nicely isolated from any other projects we're working on.

	<pre><code>mkdir /env
	virtualenv /env/mymedia
	source /env/mymedia/bin/activate</pre></code>


6. And finally, you can use the requirements.txt file so that your environment is completely and easily replicable:
    <pre><code>$ pip install -r requirements.txt</code></pre>
	
	
7. Now run the syncdb command which will initialize part of the local database file. Also, take the time to create a super user for the database, since you'll be prompted to do so.
    <pre><code>python mymedia/manage.py syncdb</code></pre>
	
8. Now run the migrate command which will complete the database setup by running the migration scripts.
    <pre><code>python mymedia/manage.py migrate</code></pre>

9. Now run the python server
	<pre><code>python mymedia/manage.py runserver 8080</code></pre>

10. Now start a browser and navigate to localhost:8080/

