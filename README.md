Project Title: Powdery Mildew Detection System for Cherry Leaves

Project Description: The Powdery Mildew Detection System for Cherry Leaves aims to develop an efficient and scalable solution for visually determining the presence of powdery mildew on cherry leaves. Powdery mildew is a common fungal infection that can have detrimental effects on cherry plantations, leading to stunted growth, yellowing leaves, and reduced yields if left untreated. This project focuses on leveraging machine learning and image analysis techniques to differentiate healthy cherry leaves from those infected with powdery mildew. By automating the detection process, the system aims to save time and resources for farmers and ensure the delivery of high-quality cherry products to the market.

Business Requirements:

1. The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one that contains powdery mildew.

2. The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

<!-- #----------------------------------------------------------------- -->

ML Business Case:
We aim to develop a machine learning model that can accurately predict whether a cherry leaf contains powdery mildew based on historical image data. This supervised classification model will have two classes: "Powedery_mildew" and "Healthy."

The primary goal of this project is to provide Marianne McGuineys' team with a faster and more reliable diagnostic tool for identifying powdery mildew on cherry trees. By automating the detection process using machine learning, we aim to significantly reduce the time and effort required for manual inspections.

The success metrics for our model are as follows:

Accuracy: We aim to achieve an accuracy of 95% or higher on the test set. This ensures that the model's predictions align with the ground truth labels and can be relied upon for accurate identification of powdery mildew.
The model output will be a binary flag indicating whether the leaf contains any features indicative of powdery mildew. The staff at the plantation will capture images of cherry leaves and upload them to the application, where the model will make predictions in real-time.

Methodology:
The current manual verification process involves visually inspecting leaf samples to determine powdery mildew infection, taking approximately 30 minutes per tree. Application of a specific compound to eliminate the fungus adds an extra minute. This manual process is time-consuming and lacks scalability across thousands of cherry trees.

To address these challenges, we propose implementing an ML system for instant detection of powdery mildew using leaf images. Success in this project can pave the way for similar initiatives in pest and disease detection across different crops.


The cherry plantation of Farmy & Foods faces challenges due to powdery mildew. Manual verification of cherry trees is inefficient, with each tree requiring 30 minutes of inspection. Scalability becomes a concern given the large number of trees spread across multiple farms.

To address this, the IT team proposes implementing an ML system for instant powdery mildew detection using leaf images. Successful implementation can be extended to other crops, providing an efficient and scalable approach to pest and disease detection.

The dataset consists of cherry leaf images from Farmy & Foods' own crops, totaling 4,208 images. It includes both healthy and powdery mildew-infected leaves.

The ML model we aim to develop is a supervised, two-class, single-label classification model. Its objective is to accurately predict whether a cherry leaf is healthy or infected with powdery mildew based on the provided image data.

Our goal is to deliver a reliable ML model with an accuracy of 97% or above for effective powdery mildew identification. The model's output will include a flag indicating powdery mildew presence and associated probability. It will operate in real-time, accepting leaf images uploaded by plantation staff through the application interface.

## Hypothesis and how to validatiion:pulsex
The Project Hypothesis and Validation page describes the hypothesis and validation approach for the project. The hypothesis is that by utilizing a powdery mildew detection tool specifically designed for cherry leaves, we can accurately differentiate between healthy leaves and those affected by powdery mildew. The validation approach is to employ the powdery mildew detection tool on a sample of cherry leaves suspected of infection and compare the tool's classifications with visual inspections and expert assessments.
## Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We then created a fictitious user story where predictive analytics can be applied in a real project in the workplace.
* The training data, sourced from Kaggle, comprises 2,104 healthy leaf images and 2,104 powdery mildew leaf images. The target variable is infection status, with the images serving as features.

<!-- #---------------------------------------------------------------- -->
Streamlit Dashboard App Interface
This repository contains a Streamlit dashboard app interface for a project focused on visually determining whether a cherry leaf has powdery mildew or not. The app provides various functionalities and visualizations related to powdery mildew detection in cherry leaves.

Page 1: Summary
This project aims to develop a system for visually determining whether a cherry leaf has powdery mildew or not. Powdery mildew is a fungal infection that affects plants and can lead to stunted growth, yellowing leaves, and reduced yields in crops if left untreated. The project focuses on two main business requirements: visually differentiating healthy cherry leaves from those with powdery mildew and predicting whether a cherry leaf is healthy or infected.

Page 2: Cherry Leaf Visualizer
The Cherry Leaf Visualizer page allows you to visualize the data used to train the machine learning model. You can view the average and variability images of healthy and powdery mildew leaves, as well as the differences between the average images. You can also view a gallery of cherry leaf images.

Page 3: Leaves Mildew Detector
The Leaves Mildew Detector page allows you to upload cherry leaf images and have the machine learning model predict whether the leaf contains powdery mildew or not. The model will also generate a report that includes the prediction, the probability of the prediction, and the image of the leaf.

Page 4: Project Hypothesis and Validation
The Project Hypothesis and Validation page describes the hypothesis and validation approach for the project. The hypothesis is that by utilizing a powdery mildew detection tool specifically designed for cherry leaves, we can accurately differentiate between healthy leaves and those affected by powdery mildew. The validation approach is to employ the powdery mildew detection tool on a sample of cherry leaves suspected of infection and compare the tool's classifications with visual inspections and expert assessments.

Page 5: ML Performance Metrics
The ML Performance Metrics page shows the performance metrics of the machine learning model. The metrics include the accuracy, loss, and confusion matrix.

Conclusion
The project has successfully developed a system for visually determining whether a cherry leaf has powdery mildew or not. The system achieves an accuracy of 95% on the test set. The system can be used to visually differentiate healthy cherry leaves from those with powdery mildew. The system can also be used to predict whether a cherry leaf is healthy or contains powdery mildew with high accuracy. The project has the following limitations: it only uses a single dataset of cherry leaves and it only uses a single machine learning model. The project could be improved in the following ways: it could use more datasets of cherry leaves, it could use more machine learning models, and it could be extended to other types of plants.

<!-- #------------------------------------------------------------------ -->
## Deployment: Heroku

The Streamlit Dashboard App Interface has been deployed to Heroku. You can access the live app using the following link: [Leaf Mildew Detection App](https://.herokuapp.com/)

To deploy the app on Heroku, the following steps were followed:

1. Log in to Heroku and create a new app.
2. In the Deploy tab of the Heroku dashboard, select GitHub as the deployment method.
3. Search for your repository name and click Connect to link the Heroku app with your GitHub repository.
4. Choose the branch you want to deploy and click Deploy Branch to start the deployment process.
5. Heroku will automatically build and deploy the app based on the files and dependencies in your repository.
6. Once the deployment is successful, you can click the Open App button at the top of the Heroku page to access your app.
7. If the slug size exceeds the limit, you can optimize it by adding large files that are not required for the app to the .slugignore file. This helps reduce the size of the deployment package.

Please note that the deployment process may vary depending on your specific project setup and requirements. Make sure to configure the necessary environment variables and dependencies as per your project's needs.

Feel free to explore and interact with the deployed app through the provided link.

<!-- #------------------------------------------------------------------ -->
Main Data Analysis and Machine Learning Libraries
The following libraries were used for this project:

NumPy: Used for calculating the mean and variability of images per label, converting images into arrays, and working with data inside arrays.

Pandas: Used for data manipulation and analysis, creating data frames, and plotting data.

Matplotlib: Used for creating static visualizations, plotting images, generating plots for data analysis, and saving plots as PNG images.

Seaborn: Used for creating attractive and informative statistical graphics, enhancing the visual appearance of plots created with Matplotlib.

Plotly: Used for interactive and dynamic visualizations, particularly for plotting the prediction probability results.

TensorFlow: An open-source library for deep learning applications, used for processing images, generating data for model fitting, and performing machine learning tasks.

Keras: A high-level deep learning API built on top of TensorFlow, used for implementing neural networks and simplifying the implementation of deep learning models.

PIL (Python Imaging Library): Used for opening, manipulating, and saving different image file formats, particularly for loading images in the project.

Streamlit: An open-source library for creating and sharing custom web apps for machine learning and data science. Used to build and deploy the Streamlit Dashboard App Interface, providing a user interface for accessing various parts of the project.

These libraries were instrumental in performing data analysis, visualization, image processing, and machine learning tasks in the project. They provided the necessary tools and functionalities to handle data, plot visualizations, process images, create and train machine learning models, and build the interactive dashboard app.

<!-- #------------------------------------------------------------------ -->
Bugs:
Heroku deployment:
Failed due to not supporting the python version 3.8.16 - Updated runtime.txt to supported version 3.11.3 https://devcenter.heroku.com/articles/python-support

<!-- #------------------------------------------------------------------ -->


<!-- #------------------------------------------------------------------ -->
Credits:

- Code and dashboard design: The initial code and design of the dashboard were adapted from the walkthrough project "Malaria Detector" of the Code Institute course, with minor modifications made to deepen my understanding of machine learning and data science. The original repository can be found at [https://github.com/1](https://github.com/).

- Garden Tech webpage: Valuable information about powdery mildew was obtained from the Garden Tech webpage, which enhanced my knowledge of the topic and influenced the project.

- Streamlit: The Streamlit website provided resources and a custom theme feature, allowing me to create an appealing and user-friendly dashboard interface.

- Code Institute resources: The Code Institute recommended template served as the starting point for the project, incorporating the fictional company and its requirements. The repository for the template can be found at [https://github.com/Code-Institute-Solutions/milestone-project-mildew-detection-in-cherry-leaves](https://github.com/Code-Institute-Solutions/milestone-project-mildew-detection-in-cherry-leaves). The Code Institute project handbook provided additional information and guidance.

- Matplotlib documentation: The Matplotlib documentation was referenced for creating pie charts.

- Mentor: Rohit Sharma.
