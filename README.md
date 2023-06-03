# Powdery Mildew Detection System for Cherry Leaves

https://otis-project-5.herokuapp.com/ 

(Refresh the page if you receive an error "set_page_config() can only be called once per app".)


![Home page](https://res.cloudinary.com/dbqkng7cd/image/upload/v1685702149/Project%205/page_0_xs57da.png)

## Project Description

The Powdery Mildew Detection System for Cherry Leaves aims to develop an efficient and scalable solution for visually determining the presence of powdery mildew on cherry leaves. Powdery mildew is a common fungal infection that can have detrimental effects on cherry plantations, leading to stunted growth, yellowing leaves, and reduced yields if left untreated. 

This project focuses on leveraging machine learning and image analysis techniques to differentiate healthy cherry leaves from those infected with powdery mildew. By automating the detection process, the system aims to save time and resources for farmers and ensure the delivery of high-quality cherry products to the market.


## Business Requirements

- 1 The client is interested in conducting a study to visually differentiate a healthy cherry leaf from one that contains powdery mildew.

- 2 The client is interested in predicting if a cherry leaf is healthy or contains powdery mildew.

## Business Case

- We aim to develop a machine learning model that can accurately predict whether a cherry leaf contains powdery mildew based on historical image data. This supervised classification model will have two classes: "Powdery Mildew" and "Healthy."

- The primary goal of this project is to provide an efficient and reliable diagnostic tool for identifying powdery mildew on cherry trees. By automating the detection process using machine learning, we aim to significantly reduce the time and effort required for manual inspections.

The success metrics for our model are as follows:

- Accuracy: We aim to achieve an accuracy of 95% or higher on the test set. This ensures that the model's predictions align with the ground truth labels and can be relied upon for accurate identification of powdery mildew.

- The model output will be a binary flag indicating whether the leaf contains any features indicative of powdery mildew. The staff at the plantation will capture images of cherry leaves and upload them to the application, where the model will make predictions in real-time.

## Methodology, Hypothesis & Validation

- The current manual verification process involves visually inspecting leaf samples to determine powdery mildew infection, taking approximately 30 minutes per tree. Application of a specific compound to eliminate the fungus adds an extra minute. This manual process is time-consuming and lacks scalability across thousands of cherry trees.

- To address these challenges, we propose implementing an ML system for instant detection of powdery mildew using leaf images. Success in this project can pave the way for similar initiatives in pest and disease detection across different crops.

- The cherry plantation of Farmy & Foods faces challenges due to powdery mildew. Manual verification of cherry trees is inefficient, with each tree requiring 30 minutes of inspection. Scalability becomes a concern given the large number of trees spread across multiple farms.

- To address this, the IT team proposes implementing an ML system for instant powdery mildew detection using leaf images. Successful implementation can be extended to other crops, providing an efficient and scalable approach to pest and disease detection.

- The dataset consists of cherry leaf images from Farmy & Foods' own crops, totaling 4,208 images. It includes both healthy and powdery mildew-infected leaves.

- The ML model we aim to develop is a supervised, two-class, single-label classification model. Its objective is to accurately predict whether a cherry leaf is healthy or infected with powdery mildew based on the provided image data.

- Our goal is to deliver a reliable ML model with an accuracy of 97% or above for effective powdery mildew identification. The model's output will include a flag indicating powdery mildew presence and associated probability. It will operate in real-time, accepting leaf images uploaded by plantation staff through the application interface.

## Hypothesis and Validation

- The Project Hypothesis and Validation page describes the hypothesis and validation approach for the project. The hypothesis is that by utilizing a powdery mildew detection tool specifically designed for cherry leaves, we can accurately differentiate between healthy leaves and those affected by powdery mildew. The validation approach is to employ the powdery mildew detection tool on a sample of cherry leaves suspected of infection and compare the tool's classifications with visual inspections and expert assessments.

## Dataset

- The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We then used the user story where predictive analytics can be applied in a real project in the workplace.


# Dashboard Design (Streamlit App User Interface)

## Page 1: Project Overview
This project focuses on the detection of powdery mildew, a parasitic fungal disease caused by Podosphaera clandestina in cherry trees. The disease adversely affects the plant's growth and can result in significant crop loss. The primary objective is to develop a visual differentiation system for identifying infected and uninfected cherry leaves.
![Home page](https://res.cloudinary.com/dbqkng7cd/image/upload/v1685702149/Project%205/page_0_xs57da.png)

Powdery mildew manifests as light-green, circular lesions on the leaf surface, which eventually develop into a white cotton-like growth. The dataset provided by Farmy & Foody consists of 4208 high-quality photos of single cherry leaves, categorized as either healthy or infested by powdery mildew.

**Business Requirements:**
- Visual differentiation between infected and uninfected leaves.
- Detection of powdery mildew presence in a given leaf.
- Generation of comprehensive prediction reports for examined leaves.


## Page 2: Leaves Visualizer
This page is for addressing the first business requirement.
![Page 2](https://res.cloudinary.com/dbqkng7cd/image/upload/v1685699850/Project%205/page_2_czp5oa.png)

- expander 1: Visualization of the difference between average and variability images.
- expander 2: Comparising  average parasitized and average healthy leaves.
- expander 3: Displaying an image gallery.

## Page 3: Powdery Mildew Detector
This page addresses the second requirement. It allows users to determine whether a given leaf is infected or not.

![Page 3](https://res.cloudinary.com/dbqkng7cd/image/upload/v1685699850/Project%205/page_3_ljexqt.png)

- Users can upload multiple cherry leaf images using the file uploader widget.
- The interface displays the uploaded image, a barplot representing the prediction, and a statement indicating whether the leaf is infected with powdery mildew or not, along with the associated probability.
- The table presents the image name and prediction results.

To download a set of parasite-contained and uninfected leaf images for live prediction on Kaggle, please visit [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves).


## Page 4: Project Hypothesis and Validation
Describes the validation approach, which involves using the detection tool on a sample of cherry leaves suspected of infection.

![Page 4](https://res.cloudinary.com/dbqkng7cd/image/upload/v1685699850/Project%205/page_4_akaosh.png)

## Page 5: ML Performance Metrics
This page presents various ML performance metrics:
![Page 5](https://res.cloudinary.com/dbqkng7cd/image/upload/v1685699850/Project%205/page_5_1_zrkiom.png)
![Page 5](https://res.cloudinary.com/dbqkng7cd/image/upload/v1685699850/Project%205/page_5_2_i1or1e.png)
- Label frequencies for the train, validation, and test sets.
- Percentage distribution of the dataset across the three sets.
- Model accuracy displayed through the confusion matrix.
- Model history showing accuracy and losses of the model.

### Model Development

The model development process involves several steps, including data preprocessing, model selection, training, and evaluation. Here is an overview of the steps involved:

1. **Data Preprocessing**: The raw image data needs to be preprocessed before feeding it into the model. This includes tasks such as resizing the images, normalizing pixel values, and splitting the dataset into training and testing sets.


2. **Model Selection**: We will explore various machine learning models suitable for image classification tasks. Some potential models include Convolutional Neural Networks (CNNs) such as VGG, ResNet, or MobileNet. The choice of the model will be based on its performance and suitability for our specific task.

3. **Model Training**: Once the model architecture is selected, we will train the model using the training dataset. This involves feeding the preprocessed images to the model, adjusting the model's weights based on the loss function, and optimizing the model's parameters using an optimization algorithm such as stochastic gradient descent (SGD).

4. **Model Evaluation**: After training, we will evaluate the model's performance using the testing dataset. The evaluation metrics will include accuracy, precision, recall, and F1-score. We will also visualize the model's predictions and analyze any misclassifications.

5. **Model Deployment**: Once the model is trained and evaluated, we will deploy it on the Heroku platform. This will involve creating a web application where users can upload cherry leaf images for prediction. The deployed model will make real-time predictions on the uploaded images and display the results to the user.

## Bugs
Bugs were documented in the [Project Dashboard](https://github.com/users/passportpowell/projects/6/views/1?layout=table)

## Deployment

Heroku
- The App live link is: https://otis-project-5.herokuapp.com/ (Refresh the page if you receive an error.)
- Set the runtime.txt Python version to a Heroku-20 stack currently supported version.
- The project was deployed to Heroku using the following steps.
- Log in to Heroku and create an App
- At the Deploy tab, select GitHub as the deployment method.
- Select your repository name and click Search. Once it is found, click Connect.
- Select the branch you want to deploy, then click Deploy Branch.
- The deployment process should happen smoothly if all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.
- If the slug size is too large then add large files not required for the app to the .slugignore file.

## Libraries used
- numpy: I used NumPy for efficient numerical computations and array handling.

- matplotlib: I utilized matplotlib for data visualization purposes, creating various types of plots.

- seaborn: I used seaborn for statistical data visualization, generating attractive and informative plots.

- plotly: I employed plotly to create interactive visualizations and dashboards for my data.

- streamlit: I used Streamlit to convert my code into interactive web applications for data science and machine learning.

- scikit-learn: I used scikit-learn for various machine learning tasks, including data preprocessing, feature selection, and model training.

- tensorflow-cpu and keras: I utilized TensorFlow and Keras to build and train deep learning models.

- protobuf: I used protobuf for efficient serialization and deserialization of structured data.

- pandas: I used pandas for versatile data manipulation and analysis, working with structured data in a tabular form.

- pandas-profiling: I used pandas-profiling to automatically generate detailed exploratory data analysis reports for my data.

These libraries provided me with powerful tools and functionalities to efficiently analyze data, create visualizations, build machine learning models, and deploy interactive applications.

## Acknowledgements


- Code and dashboard design: The initial code and design of the dashboard were adapted from the walkthrough project "Malaria Detector" of the Code Institute course, with changes.

- Code Institute resources: 
    - The Code Institute recommended template served as the starting point for the project. The template can be found at https://github.com/Code-Institute-Solutions/milestone-project-mildew-detection-in-cherry-leaves. The Code Institute project handbook provided additional information and guidance.
    - Code institue Slack Group.

- Mentor: Rohit Sharma.