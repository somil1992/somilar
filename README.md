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




Troubleshooting
	1) Python package - virtualenv installation
https://stackoverflow.com/questions/25981703/pip-install-fails-with-connection-error-ssl-certificate-verify-failed-certi
	1) Ssl issue
https://github.com/ContinuumIO/anaconda-issues/issues/11994


$ pip install --trusted-host pypi.org --trusted-host pypi.python.org --trusted-host files.pythonhosted.org <package_name>




# Twitter Scrapping

	1) SNS package
	https://betterprogramming.pub/how-to-scrape-tweets-with-snscrape-90124ed006af
	
	https://github.com/MartinBeckUT/TwitterScraper/tree/master/snscrape
	
https://github.com/JustAnotherArchivist/snscrape/tree/master/snscrape/modules




# Topic Modelling

LDA
https://www.machinelearningplus.com/nlp/topic-modeling-gensim-python/

BERT
https://towardsdatascience.com/topic-modeling-with-bert-779f7db187e6
https://towardsdatascience.com/interactive-topic-modeling-with-bertopic-1ea55e7d73d8
https://pypi.org/project/bertopic/
-> bert notebook (topic visuals)
https://colab.research.google.com/drive/1FieRA9fLdkQEGDIMYl0I3MCjSUKVF8C-?usp=sharing#scrollTo=ltmLFRR56a4X
-> bert github
https://github.com/MaartenGr/BERTopic
-> Topic modelling on tweets sample
https://medium.com/atoti/topic-modeling-on-twitter-using-sentence-bert-8acdad958eb1




Why LDA Fails and Why BERT:
https://blog.insightdatascience.com/contextual-topic-identification-4291d256a032
LDA : Bag-of-words based (disregarding grammar and word order), it loses contextual information and suffers from the data being incoherent and unstructured.
	• It has a hard time handling short texts when there is not much text to model
	• The reviews usually don’t coherently discuss a single topic (making it hard for LDA to identify the main topics of the documents)
	• The actual meaning of reviews is largely context-based, so word co-occurrence based methods like LDA might fail.
When LDA words:
Bag-of-words information (LDA or TF-IDF) is effective for identifying topics by finding frequent words when texts are coherent within themselves. On the other hand, when texts are incoherent (in terms of word choice or sentence meaning), extra contextual information is needed to comprehensively represent the idea of the texts.


	1) API Based Interest : - Monkeylearn
	https://blog.twitter.com/developer/en_us/a/2015/guest-post-understanding-users-through-twitter-data-and-machine-learning
	
	https://blog.twitter.com/developer/en_us/a/2015/guest-post-understanding-users-through-twitter-data-and-machine-learning
	
	https://app.monkeyl	earn.com/main/classifiers/cl_o46qggZq/tab/api/
	
	
	Twitter Campaign - https://ads.twitter.com/campaign_form/18ce55fat4p/campaign/new?ref=BTC
	


# Python Basics
PANDAS : All Functions
https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.html
https://jakevdp.github.io/PythonDataScienceHandbook/ (handbook)


Pandas Tutorial Notebook:
	1. https://github.com/justmarkham/pandas-videos
	2. https://trenton3983.github.io/files/projects/2019-02-04_manipulating_dataframes_with_pandas/2019-02-04_manipulating_dataframes_with_pandas.html
	3. https://www.w3resource.com/python-exercises/pandas/index-dataframe.php


Auto Import Libraries in python
	1. https://towardsdatascience.com/import-all-python-libraries-in-one-line-of-code-86e54f6f0108
	2. https://pypi.org/project/pyforest/




# NER
Name Entity Recognition:

	1) NLTK & SPCY
https://towardsdatascience.com/named-entity-recognition-with-nltk-and-spacy-8c4a7d88e7da
	2) Custom entities addition to NER
Custom Named Entity Recognition using Python

	3) Spacy Application
https://www.analyticsvidhya.com/blog/2021/06/nlp-application-named-entity-recognition-ner-in-python-with-spacy/


	3) BERT approach
https://towardsdatascience.com/named-entity-recognition-ner-with-bert-in-spark-nlp-874df20d1d77
Train Custom NAMED ENTITY RECOGNITION (NER) model using BERT.

	4) BERT NER unsupervised approach
https://towardsdatascience.com/unsupervised-ner-using-bert-2d7af5f90b8a



# Sentiment

Bert Approach

SENTIMENT ANALYSIS USING BERT WITH CODE IMPLEMENTATION


Working NLP approach for unsupervised sentiment analysis
Sentiment Analysis with BERT Neural Network and Python



# BERT

Basics of BERT:

https://www.analyticsvidhya.com/blog/2019/09/demystifying-bert-groundbreaking-nlp-framework/

	1) Sentence Similarity - tokens using bert and cosine similarity
https://towardsdatascience.com/bert-for-measuring-text-similarity-eec91c6bf9e1





	2) Text Classification
Kaggle Natural Language Processing with Disaster Tweets – Top 14% Solution with BERT (TensorFlow)


	3) Embeddings applications
https://medium.com/spark-nlp/1-line-to-bert-word-embeddings-with-nlu-f50d2b08cddc


# FLASK API

REST API & RESTFUL API
https://www.youtube.com/watch?v=s_ht4AKnWZg&ab_channel=MelvinL


Sample sentiment analysis deployment using Flask-RESTful
https://towardsdatascience.com/deploying-a-machine-learning-model-as-a-rest-api-4a03b865c166


Flask+ Flaskgr - Krish Naik
Docker Tutorial 2- Building A Flask App For A Bank Note Authentication

Docker Tutorial 3-Deploying Machine Learning Models Using Flask And Flasgger


Flask Restful + swagger UI code
https://towardsdatascience.com/working-with-apis-using-flask-flask-restplus-and-swagger-ui-7cf447deda7f


Flask request modes:
https://www.programcreek.com/python/example/51530/flask.request.args


Making Curl request
https://davidwalsh.name/curl-post-file

Making curl request using python
https://stackoverflow.com/questions/25491090/how-to-use-python-to-execute-a-curl-command


Input types
https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask

# Docker

Docker Hub Credentials:
Username - somilrast
Password - somilrast



Docker Deployment : 
Docker 101: Automated Docker Builds with DockerHub and GitHub, learn docker for beginners tutorial


Workshop: ML Model Deployment using Flask and Docker


https://github.com/shreyas219/breast_cancer_classification


Learn to Deploy your Flask REST API on Docker  in 12 Minutes


End to End :
Docker For Data Scientists

Docker commands documents
https://docs.docker.com/engine/reference/commandline/start/



CI CD Pipeline - 2 Approaches

https://davelms.medium.com/build-your-docker-images-automatically-when-pushing-new-code-to-github-394f4c1679cc


Automated Workflow
https://docs.github.com/en/actions/publishing-packages/publishing-docker-images

Copyfile files from docker filesystem
Docker Container Tutorial #7 Copy Files From A Container
Docker exec -it <container> /bin/bash
docker cp naughty_volhard:/app/Colorized.png
	

	
# git
	
	1) Creating local repository + Comit changes + Pushing code to github
How to Push Code to Github




Useful git commands
	1) Cloning github repo to local
	Git clone <repo link>
	
	2) Cloning a specific branch
	git clone --single-branch --branch workflow_v2 <repo link>
	git clone --single-branch --branch deployment_user1 https://github.com/PrezSeah/modelapi.git
	
	3) Initialize local repo as git repo
	Go to specific folder path
	cd <folder path>
	
	4) Pushing changes from local to github
		a. To check the changes
		Git status
		b. To add all changes
		Git add.
		c. To commit changes
		Git commit -m "comment"
		d. Adding origin (if not added)
		Git remote add origin <repo link>
		e. Pushing codes to branch
		Git push -u origin workflow_v2
		
		
		
GitHub Workflows: - Git Action Commands
https://docs.github.com/en/actions/managing-workflow-runs/manually-running-a-workflow

Automating Github
EASY Python Project AUTOMATION **Create new repos using GITHUB API
	
	
	
# RAI
	
What is Responsible AI:
Responsible AI
RAI Microsoft Tools:
https://www.microsoft.com/en-us/ai/responsible-ai-resources#:~:text=The%20Responsible%20AI%20Toolbox%20is,%2C%20and%20causal%20decision%2Dmaking.

Microsoft Tool Kit:
https://github.com/microsoft/machine-learning-collection#responsible-ai


Fairlearn:
How to Test Models for Fairness with Fairlearn Deep-Dive
https://www.persistent.com/blogs/fairness-in-ai-systems/


Lime Overview:
KDD2016 paper 573
Lime Handson:
How To Interpret The ML  Model? Is Your Model Black Box? Lime Library


Shap:
https://towardsdatascience.com/explain-your-model-with-the-shap-values-bc36aac4de3d
https://www.analyticsvidhya.com/blog/2019/11/shapley-value-machine-learning-interpretability-game-theory/


Interpret ML
Interpreting Machine Learning Models with InterpretML Python
How to Explain Models with IntepretML Deep Dive


Error Analysis Toolkit:
Build Responsible AI using Error Analysis toolkit

Designing RAI practises - examples
https://ai.google/responsibilities/responsible-ai-practices/?category=fairness









