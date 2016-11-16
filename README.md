# Theano in Mac OS

## Requirements
1. Xcode (install from App Store)
2. Anaconda
	1.  Download Anaconda at https://www.continuum.io/downloads#osx Python 2.7 version, COMMAND-LINE INSTALLER,  (346M)
	2. In your terminal window, type  `bash Anaconda2-4.2.0-MacOSX-x86_64.sh` to install Anaconda, ref: [Full installation — Conda   documentation](http://conda.pydata.org/docs/install/full.html#install-instructions)
	3. Logout terminal, Login terminal
	4. Anaconda update, type  `conda update conda`
	5. Create an environment, type `conda create --name theano`  ref: http://conda.pydata.org/docs/test-drive.html
	6. Activate the new environment, type `source activate theano`
  
## Installing Theano in Anaconda
Reference: [Installing Theano — Theano 0.8.2 documentation](http://deeplearning.net/software/theano/install.html#mac-os) . Test on Mac OS X 10.12.1
The following steps are in the created _theano_ environment.

1. Install Theano in the environment, type `conda install theano`
2. Install nose in the environment, type `conda install nose`
3. Install nose-parameterized in the environment, type `pip install nose_parameterized`
4. Test Theano, type `python -c "import theano; theano.test()"`

## Other common commands for Anaconda
Reference: [Test drive — Conda   documentation](http://conda.pydata.org/docs/test-drive.html)

1. Deactivate the new environment, type `source deactivate theano`
2. Delete an environment, type `conda remove --name theano --all`
3. List all environments, type `conda info --envs`

## Installation of Theano on other systems
1. Linux (CentOS or Ubuntu)
	1. Install Anaconda [Download Anaconda Now! | Continuum](https://www.continuum.io/downloads#osx)
	2. Similar with steps in Mac OS
2. Windows [Installation of Theano on Windows — Theano 0.8.2 documentation](http://deeplearning.net/software/theano/install_windows.html#install-windows) 
	
