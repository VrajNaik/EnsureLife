# EnsureLife - Insurance Management with Premium Prediction

Insurance Management with Premium Prediction is a web application developed using Django framework. It serves as an online platform for managing insurance policies, customer details, and company information. The system also incorporates machine learning for premium prediction, enabling the estimation of insurance premiums based on various factors.

## Features

- **User Authentication**: Users can log in to the system to view their personal details and insurance information.
- **Policy Management**: Admin users can register insured persons with their personal details, residence address, medical history, and policy information.
- **Premium Prediction**: Machine learning models are used to predict insurance premiums based on relevant factors.
- **Search Tools**: Visitors can access insurance awareness articles, guidelines, and illustrations through search tools.
- **Easy Access**: The system provides instant access to insurance records and improves productivity for insurance organizations.

## Installation Steps

1. **Clone the repository**:
   ```bash
   git clone <repository-url>
   ```
   
2. **Navigate to the project directory**:
   ```bash
   cd insurance-management
   ```
   
3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```
   
4. **Apply migrations**:
   ```bash
   python manage.py migrate
   ```

## Running the Application

1. **Start the Django development server**:
   ```bash
   python manage.py runserver
   ```
   
2. **Open a web browser** and go to `http://localhost:8000` to access the application.

## Usage

1. **Register as an admin user** to access full functionalities.
2. **Log in to the system** to manage insurance policies, customer details, and company information.
3. Use the **premium prediction feature** to estimate insurance premiums based on relevant factors.
4. Explore the **search tools** to access insurance awareness articles, guidelines, and illustrations.
5. Do Premium payment.
6. Compare different policies.
7. Customer also get premium alerts.

## Machine Learning for Premium Prediction

The premium prediction feature utilizes machine learning models trained on historical insurance data. These models analyze various factors such as age, medical history, residence address, etc., to predict insurance premiums accurately.

## Insurance Premium Prediction

## Problem Statement :
The goal of this project is to provide individuals with an estimate of their health insurance premium based on their individual health situation. This helps customers focus on the health aspects of an insurance policy rather than being overwhelmed by the financial aspects.

## Dataset :
The dataset is sourced from Kaggle. You can download the dataset from [here](https://www.kaggle.com/noordeen/insurance-premium-prediction).

## Approach :
The solution involves applying machine learning tasks such as Data Exploration, Data Cleaning, Feature Engineering, Model Building, and Model Testing to predict the premium of health insurance for individuals.

- **Data Exploration:** Explore the dataset using pandas, numpy, matplotlib, plotly, and seaborn.
- **Exploratory Data Analysis:** Plot different graphs to gain insights into dependent and independent variables/features.
- **Feature Engineering:** Scale numerical features and encode categorical features.
- **Model Building:** Split the dataset and train models using different Machine Learning Algorithms such as:
    1) Linear Regression
    2) Decision Tree Regressor
    3) Random Forest Regressor
    4) Gradient Boosting Regressor
    5) XGBoost Regressor
    6) KNN
- **Model Selection:** Test all models to check the RMSE & R-squared.
- **Pickle File:** Select the model with the best RMSE score & R-squared and create a pickle file using the pickle library.
- **Webpage & Deployment:** Create a web application that takes necessary inputs from the user and displays the output. Deploy the project on the Heroku Platform.

## Libraries used :
1. Pandas
2. Numpy
3. Matplotlib, Seaborn, Plotly
4. Scikit-Learn

## Technologies Used

- **Django**: Web framework for building the application.
- **Python**: Programming language used for backend development.
- **HTML/CSS/JavaScript**: Frontend development technologies.
- **Machine Learning (ML)**: Used for premium prediction.


## Contributors

- [Vraj Naik](https://github.com/VrajNaik)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
