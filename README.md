### 🎯 Project Mission 
The aim of this project is to identify gaps in the current social media posting cycle via data analysis. Moreover, we will create a predictive model and feed our social media data into the model which will then give us recommendations of what to post and when in the future.
We aim to:

1. Identify the optimal types of posts for the foundation's audience.

2. Highlight account for the lack of posts and account for this in the model.

3. Generate many LLMs that provide the posts that produce the highest engagement and when we should post this (time of year in addition to day and time). 

### 📊 Project Overview
This project provides a predictive analytics suite for The Shannon B. Jones Passion Pursuit Foundation. By leveraging historical social media metadata from Facebook and Instagram, the system utilizes a Linear Regression model (and eventually a PyTorch Neural Network) to analyze and predict post engagement.

The core objective is to identify the "Engagement Delta"—quantifying the impact of specific post attributes (such as the presence of recipients) on overall reach and interaction.

### 🏗️ Architectural Design
To ensure scalability and maintainability, this project moves away from procedural scripting in favor of Object-Oriented Programming (OOP) and SOLID principles.

### Design Patterns Implemented:
Factory Method: Used to instantiate platform-specific data parsers (Facebook vs. Instagram). This ensures the core analytics engine is loosely coupled with the data source.

Singleton: Applied to the DatabaseManager and Configuration modules to ensure consistent state and efficient resource management across the application.

Strategy Pattern (Planned): To allow for interchangeable predictive models (e.g., swapping a Scikit-Learn Linear Regression for a PyTorch Deep Learning model) without modifying the ingestion pipeline.

### 🧠 Technical Stack
Language: Python 3.x

Data Science: NumPy, Pandas (Data Transformation)

Machine Learning: PyTorch / Scikit-Learn (Predictive Modeling)

Architecture: Abstract Base Classes (ABCs) for interface definition.

Version Control: Managed via GitLab, adhering to semantic commit messaging.

### 🛠️ Performance & Scalability
By adhering to the Dependency Inversion Principle, this dashboard is designed to be "Platform Agnostic." Adding a new data source (e.g., LinkedIn or TikTok) requires zero changes to the predictive logic—simply the addition of a new concrete Parser class.

### 📜 Licensing
This project is licensed under the GNU AGPLv3. This ensures that the foundation's intellectual property is protected while remaining open to community contribution, preventing commercial "siloing" of the predictive logic.
