# somilar

# New Env Setup
#Creating new environment p3
conda create -n p3 python=3.6 anaconda


#calling p3 env
conda activate p3

conda install tensorflow

import tensorflow




# Virtual Env Setup
New Virtual Env setup

	1) Python - m venv AzureVision
	2) Cd AzureVision
	3) Scripts\activate
	4) Pip install ipykernel
	5) ipython kernel install --user --name=AzureVision (for jupyter notebook)
![image](https://user-images.githubusercontent.com/33191690/161816593-c62fad43-0774-4a21-abec-f1b76d17fb31.png)



Video Tutorial
Virtual Environment & Requirements.txt | Python Tutorials For Absolute Beginners In Hindi #43

Creation : virtualenv check1

Activation : ch1\Scripts\activate

Deactivation : deactivate

Getting requirements : pip freeze > requirements.txt

Installing requirements : pip install -r requirements.txt
![image](https://user-images.githubusercontent.com/33191690/161816614-b95f3453-0dfb-4d4c-ac28-cdcf76107086.png)



Troubleshooting
	1) Python package - virtualenv installation
https://stackoverflow.com/questions/25981703/pip-install-fails-with-connection-error-ssl-certificate-verify-failed-certi
	1) Ssl issue
https://github.com/ContinuumIO/anaconda-issues/issues/11994


$ pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org <package_name>


![image](https://user-images.githubusercontent.com/33191690/161816658-7afa0c73-eb96-4fc3-957c-01c4774cd353.png)

