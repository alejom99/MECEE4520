# Leacture 4 - Data Pipelines For ML 1

## Setup Instructions

We're going to work on some exercises during the class. So, follow the instructions
below to setup your laptop.

1. Terminal setup
   
   Make sure to familiarize yourself with a terminal.
   - Linux: you already have one...
   - Mac: `Terminal` comes pre-installed, you can certainly use that.
   - Windows: `cmd` should come pre-installed. Powershell is another popular option.

3. Install Git

    - Linux (Ubuntu):

            $ sudo apt-get update 
            $ sudo apt-get install -y git

    - Mac: 
  
        Install homebrew

            $ ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
            $ brew doctor

        Install Git:
        
            $ brew install git

    - Windows:
        [Git for Windows](https://gitforwindows.org/)

4. Install python 3

   - Linux: 

        This instructions are for Ubuntu. You can find instructions for other
        Linux distributions on the web

            $ sudo apt-get update
            $ sudo apt-get install -y python3 python3-pip

    - Mac:
        [Installing Python 3 on Mac OS X](https://docs.python-guide.org/starting/install3/osx/)

    - Windows:
        [Installing Python 3 on Windows](https://docs.python-guide.org/starting/install3/win/)

5. Install virtualenv

        $ pip install virtualenv

6. Clone repository from Github

        $ git clone https://github.com/alejom99/MECEE4520.git

7. Create virtual environment for lecture 4
   
        $ cd MECEE4520/lecture_4
        $ virtualenv --python=python3 env

8. Install requirements

        $ . ./env/bin/activate
        $ pip install -r requirements.txt

9. Install Docker https://docs.docker.com/install/

   - Install the "Docker Desktop" clients
   - On Mac: https://docs.docker.com/docker-for-mac/install/
   - On Windows: https://docs.docker.com/docker-for-windows/install/
   - On Linux: If you're using linux you'll know how to get Docker running...

10. Download doccano image 

        $ docker pull chakkiworks/doccano
    


