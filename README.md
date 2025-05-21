<h1>
  <img src="logo.png" alt="Logo" width="80" height="70" align="center">
  Student Insights Suite
</h1>

**Student Insights Suite** is an interactive Streamlit web application designed to help students and educators analyze academic scores, estimate college admission percentiles, and predict student dropout risks using machine learning.

This intuitive, modular tool offers a unified dashboard experience to visualize and interpret student data meaningfully.

---

##  Features

###  Score Analyzer :
This module allows you to upload a CSV file containing subject-wise scores of multiple students. It helps in:

- **Previewing the Dataset:**  
Instantly view the uploaded dataset in a clean tabular format.

- **Descriptive Statistics:**  
Automatically generates essential metrics like mean, median, standard deviation, minimum, and maximum for each subject to provide a quick statistical overview.

- **Histograms:**  
Visualizes the distribution of scores for each subject to identify trends, performance variation, and outliers.

- **Correlation Heatmap (optional extension):**  
Shows relationships between subjects—useful for understanding which subjects students tend to perform similarly in.

---

###  Admission Estimator :
This module helps students estimate how competitive their entrance exam score is:

- **Percentile Calculator:**  
Enter your individual entrance exam score and upload a dataset containing the scores of all applicants.

- **Percentile Ranking Output:**  
Calculates the percentage of students you’ve outperformed, helping you understand your standing among peers.

- **Quick Feedback:**  
Displays your result in an easy-to-read message showing how your score compares to others.

---

###  Dropout Predictor : 
A machine learning-based module that predicts whether a student might drop out based on their profile:

- **Training the Model:**  
Upload a CSV with student details and a Dropout column (1 for dropout, 0 for continue). The system uses a Decision Tree Classifier for training.

- **Interactive Prediction:**  
After training, enter values for each student feature (e.g., attendance, grades, parental education, etc.) to get a real-time prediction.

- **Visual Explanation:**  
The app displays the trained decision tree to help understand which features influenced the prediction most.

- **Educational Insight:**  
Helps institutions and counselors preemptively identify at-risk students using data-driven predictions.

---

##  Usage

- Navigate between the three tools using the sidebar.  
- Upload the required CSV files as prompted by each tool.  
- For the Dropout Predictor, ensure the training dataset includes a Dropout column to train the model correctly.  
- Enter any additional input values when requested to get predictions or analyses.

---

##  Dependencies

The application leverages several key Python libraries to provide its functionality:

- **streamlit:**  
The main framework used to create the interactive web app interface, handle file uploads, and display data, charts, and user inputs seamlessly.

- **pandas:**  
Used for data manipulation and analysis, including reading CSV files and computing descriptive statistics on student scores.

- **matplotlib:**  
Utilized for plotting histograms and visualizations such as correlation heatmaps to help users better understand score distributions and relationships.

- **scikit-learn:**  
Provides the machine learning tools for training the decision tree model in the Dropout Predictor, enabling prediction of student dropout risks.

- **pillow:**  
Used for image processing tasks, such as loading and displaying the app’s logo within the interface.

---

###  Install Dependencies

```bash
pip install streamlit pandas matplotlib scikit-learn pillow
