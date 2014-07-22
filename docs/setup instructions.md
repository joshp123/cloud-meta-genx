walkthrough of set up procedure
================================

### Prerequesites

* Amazon Web Services (if you want to deploy quickly to the cloud. It will work on a free micro instance.) _Takes 30 mins max, needs only be done once_ 
  * Sign up for [Amazon Web Services](http://aws.amazon.com/).
  * Either create a user or use the default user, and **create an access key**. Download this, and save it somewhere safe for later.
  * Install the AWS [Command Line Tools](http://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-set-up.html). If you have Python and `pip` installed, this is as simple as running `pip install awscli`. (If you don't have `pip` but do have `easy_install`, this can install `pip`.)
  * Once installed, run `aws configure`. It will ask you for the *access key* and *secret access key* you created earlier. Paste these in from the downloaded file. It will also ask for a default region (I suggest `eu-west-1`), and an encoding setting (just hit enter to use the default).
  * The next (slightly tedious two) steps are to set up EC2:
    * First, make a Key Pair by running `aws ec2 create-key-pair --key-name GenXKeyPair --query 'KeyMaterial' --output text > GenXKeyPair.pem `
    * Then make a Security Group [here](https://console.aws.amazon.com/ec2/home?region=eu-west-1#s=SecurityGroups) called GenX or similar.

   You should now be ready to use the AWS Command Line Interface (and thus, scripts written by other people) - to control cloud instances.


* DigitalOcean Account - similar in price to AWS, really easy to use.
 * First run:
 	* Sign up for an account
 	* Create a new droplet (ubuntu I guess unless you like something else
 * Log in to your droplet with `ssh root@<your ip>` from Terminal on Linux/OS X or PuTTY on Windows
 * Config the box (sudo):
 sudo apt-get install python-numpy python-scipy python-matplotlib ipython ipython-notebook python-pandas python-sympy python-nose

 	* apt-get install git
 	* apt-get install python-dev
 	* easy_install numpy
	* pip install scipy
	scipy from source
	**** libatlas-base-dev
 	* git clone <this repo>
 	* cd genx
 	* run our setup script which:
 		*
