# Logs Analysis Project

## What you will need to view the project:
1. Python 3
2. Virtual Machine using
- VirtualBox
- Vagrant
3. The database file

## Install Python 3
- Windows and Mac: Install it from python.org: https://www.python.org/downloads/
- Mac (with Homebrew): In the terminal, run brew install python3
- Debian/Ubuntu/Mint: In the terminal, run sudo apt-get install python3

## Install the Virtual Machine
In the next part of this course, you'll use a virtual machine (VM) to run an SQL database server and a web app that uses it. The VM is a Linux server system that runs on top of your own computer. You can share files easily between your computer and the VM; and you'll be running a web service inside the VM which you'll be able to access from your regular browser.

We're using tools called Vagrant and VirtualBox to install and manage the VM. You'll need to install these to do some of the exercises. The instructions on this page will help you do this.

### Install VirtualBox
VirtualBox is the software that actually runs the virtual machine. You can download it from [virtualbox.org](https://www.virtualbox.org/wiki/Download_Old_Builds_5_1). Install the platform package for your operating system. You do not need the extension pack or the SDK. You do not need to launch VirtualBox after installing it; Vagrant will do that.

### Install Vagrant
Vagrant is the software that configures the VM and lets you share files between your host computer and the VM's filesystem. Download it from [vagrantup.com](https://www.vagrantup.com/downloads.html). Install the version for your operating system.

Windows users: The Installer may ask you to grant network permissions to Vagrant or make a firewall exception. Be sure to allow this.

Download the VM configuration
There are a couple of different ways you can download the VM configuration.

You can download and unzip this file: FSND-Virtual-Machine.zip This will give you a directory called FSND-Virtual-Machine. It may be located inside your Downloads folder.

Alternately, you can use Github to fork and clone the repository https://github.com/udacity/fullstack-nanodegree-vm.

Either way, you will end up with a new directory containing the VM files. Change to this directory in your terminal with cd. Inside, you will find another directory called vagrant. Change directory to the vagrant directory:

### Start the virtual machine
From your terminal, inside the vagrant subdirectory, run the command vagrant up. This will cause Vagrant to download the Linux operating system and install it. This may take quite a while (many minutes) depending on how fast your Internet connection is.

Starting the Ubuntu Linux installation with `vagrant up`
Starting the Ubuntu Linux installation with vagrant up.
This screenshot shows just the beginning of many, many pages of output in a lot of colors.

When vagrant up is finished running, you will get your shell prompt back. At this point, you can run vagrant ssh to log in to your newly installed Linux VM!

## Accessing the database for this project
Next, download the data here. You will need to unzip this file after downloading it. The file inside is called newsdata.sql. Put this file into the vagrant directory, which is shared with your virtual machine.

To build the reporting tool, you'll need to load the site's data into your local database. Review how to use the psql command in this lesson: (FSND version)

To load the data, cd into the vagrant directory and use the command `psql -d news -f newsdata.sql`.

### The database includes three tables:

- The authors table includes information about the authors of articles.
- The articles table includes the articles themselves.
- The log table includes one entry for each time a user has accessed the site.



Connect to the Virtual Machine via Vagrant then run the python3 file newslogs.py.
