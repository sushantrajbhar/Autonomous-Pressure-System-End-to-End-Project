
# APS Failure Classification System

The **Air Pressure System (APS)** is critical in heavy-duty vehicles, primarily responsible for generating compressed air to power essential functions like braking. This project provides a **binary classification model** to predict whether an APS failure is caused by its specific components (positive class) or due to other unrelated issues (negative class). By accurately identifying APS-related issues, this system aims to **minimize repair costs** and **focus maintenance efforts on relevant components**.

## Table of Contents
1. [Project Overview](#project-overview)
2. [Dataset and Database Integration](#dataset-and-database-integration)
3. [Solution Architecture](#solution-architecture)
4. [Key Features](#key-features)
5. [Project Pipelines](#project-pipelines)
6. [Model Selection and Evaluation](#model-selection-and-evaluation)
7. [User Interface](#user-interface)
8. [Continuous Integration and Deployment](#continuous-integration-and-deployment)
9. [Installation and Setup](#installation-and-setup)
10. [Usage](#usage)
11. [Contributing](#contributing)
12. [License](#license)

---

### Project Overview

In this project, we build a **machine learning system** capable of distinguishing between component-specific APS failures and general vehicle issues. Our goal is to reduce unnecessary repairs and improve the efficiency of maintenance by focusing on APS-related failures.

### Dataset and Database Integration

- The dataset is stored and managed in **MongoDB**, ensuring efficient data retrieval for model training and testing.
- All data operations, including ingestion and validation, are structured in a dynamic, object-oriented approach using Python.

### Solution Architecture

The project leverages multiple classification algorithms to maximize model performance. The model with the best performance metrics is selected for deployment, ensuring accuracy and reliability in failure prediction.

### Key Features

- **Dynamic Programming**: Object-oriented programming structures make the project scalable and easy to maintain.
- **Classification Model Development**: Various classification algorithms (e.g., Logistic Regression, Decision Trees, Random Forest, etc.) are tested. Performance metrics for each are computed, and the highest-performing model is selected.
- **Database Integration**: The dataset is stored and managed in MongoDB, enabling easy retrieval for training.
- **AWS Deployment**: The final model is deployed on AWS to enable scalable predictions.
- **FastAPI UI**: A **FastAPI-based UI** allows users to interact with the model, input new data, and visualize predictions.
- **CI/CD Integration**: Automated CI/CD pipeline with GitHub Actions for seamless development and deployment.

### Project Pipelines

The project is designed as a series of modular pipelines, each handling a specific stage in the model lifecycle:

1. **Data Ingestion**: Fetches and loads data from MongoDB.
2. **Data Validation**: Ensures data integrity and consistency.
3. **Data Transformation**: Preprocesses data for model readiness.
4. **Model Trainer**: Trains multiple classification models.
5. **Model Evaluation**: Evaluates and compares model performance.
6. **Model Pusher**: Deploys the best-performing model.
7. **Prediction**: Provides real-time predictions for incoming data.

### Model Selection and Evaluation

To ensure robust performance, multiple classification algorithms are evaluated, and the one yielding the best performance metrics is selected. The following metrics are considered:
- **Accuracy**
- **Precision**
- **Recall**
- **F1 Score**

### User Interface

The project includes a **FastAPI-based UI** for user interaction:
- Allows users to input new data for failure prediction.
- Displays prediction results (APS-related or non-APS-related failure).
- Provides visualization of model metrics and other information.



### Continuous Integration and Deployment

The project is integrated with **GitHub Actions** for continuous integration and deployment, automating testing, building, and deployment stages. Once validated, the model is automatically deployed to AWS.

### Installation and Setup

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/sushantrajbhar/Autonomous-pressure-system-End-to-End-project.git
   ```

2. **Set up the Environment**:
   - Install Python dependencies:
     ```bash
     pip install -r requirements.txt
     ```

3. **Database Setup**:
   - Ensure MongoDB is installed and running.
   - Populate the dataset in MongoDB.

4. **Configure AWS and GitHub Actions**:
   - Set up AWS for deployment.
   - Configure GitHub Actions for CI/CD integration.

### Usage

Once set up, the following commands can be used to run different stages of the project:



- **Run Prediction**:
  ```bash
  python main.py 
  ```


### Contributing

We welcome contributions to enhance the project! Please fork this repository and submit a pull request.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---