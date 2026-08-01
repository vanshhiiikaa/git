# Python Data Storage

A simple Python project that demonstrates how to store and manage data using different file formats.

## Features

* Store data in **CSV** files
* Store data in **JSON** files
* Store data in **Excel (.xlsx)** files
* Read data from files
* Update and save data

## Technologies Used

* Python 3
* pandas
* openpyxl
* json (built-in module)

## Project Structure

```text
python-data-storage/
│
├── main.py
├── students.csv
├── students.json
├── students.xlsx
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/python-data-storage.git
```

2. Move to the project folder:

```bash
cd python-data-storage
```

3. Install the required packages:

```bash
pip install pandas openpyxl
```

## Running the Project

Run the Python file:

```bash
python main.py
```

## Sample Data

| Name    | Age | City    |
| ------- | --: | ------- |
| Alice   |  25 | Delhi   |
| Bob     |  30 | Mumbai  |
| Charlie |  22 | Lucknow |

## Learning Objectives

This project demonstrates how to:

* Create CSV files
* Read CSV files
* Create JSON files
* Read JSON files
* Create Excel files
* Read Excel files
* Store structured data using Python

## Author

vanshika

## License

This project is created for learning and educational purposes.



# 📘 Learning Pandas with Python

## 📌 Overview

This repository contains my practice programs and notes while learning the **Pandas** library in Python.

The goal of this repository is to understand the basics of data analysis, data manipulation, and working with datasets using Pandas. As I continue learning, I will add more examples and mini-projects.

## 🎯 Learning Objectives

* Understand Pandas fundamentals
* Create and work with Series and DataFrames
* Read and write CSV files
* Explore and analyze datasets
* Filter, sort, and manipulate data
* Handle missing values
* Perform basic data analysis

## 🛠️ Technologies Used

* Python 3
* Pandas
* Jupyter Notebook / VS Code

## 📂 Repository Structure

```text
pandas-learning/
│── basics.py
│── series.py
│── dataframe.py
│── csv_operations.py
│── practice/
│── datasets/
│── README.md
```

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/pandas-learning.git
```

### 2. Navigate to the Project Folder

```bash
cd pandas-learning
```

### 3. Install Pandas

```bash
pip install pandas
```

### 4. Run a Python File

```bash
python basics.py
```

## 📚 Topics Covered

* Introduction to Pandas
* Series
* DataFrames
* Reading CSV files
* Writing CSV files
* Selecting rows and columns
* Filtering data
* Sorting data
* Handling missing values
* Descriptive statistics
* GroupBy operations
* Data cleaning

## 📖 Sample Code

```python
import pandas as pd

data = {
    "Name": ["Alice", "Bob", "Charlie"],
    "Marks": [85, 92, 78]
}

df = pd.DataFrame(data)

print(df)
```

## 🎯 Future Goals

* Learn data visualization with Matplotlib and Seaborn
* Explore NumPy integration with Pandas
* Work with larger datasets
* Build beginner-friendly data analysis projects
* Learn data preprocessing for machine learning

## 📈 Progress

* ✅ Python Basics
* ✅ NumPy Basics
* 🔄 Learning Pandas
* ⏳ Data Visualization
* ⏳ Machine Learning

## 🤝 Contributing

This repository is primarily for my personal learning journey, but suggestions and improvements are always welcome.

## 📄 License

This project is open source and available under the MIT License.

