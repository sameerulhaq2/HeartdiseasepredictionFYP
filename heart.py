# Import libraries
import streamlit as st
import pickle

# Giving the title of the website
st.title('Web Application for Heart Disease Prediction')

# Loading the XGBoost model
with open('xgboost_best_model.pkl', 'rb') as c:
    model_loaded = pickle.load(c)

# The sidebar with options and logo of heart is created
st.sidebar.image("heart_logo.png")
page_selected = st.sidebar.selectbox("Select Page", ["About", "Educational Information", "Prediction System"])

# Each page option is defined here
if page_selected == "About":
    # The information about the creator is shown
    st.title("About us")
    st.write("I'm Sameer Ul Haq, a final-year student studying Data Analytics at Asia Pacific University. "
             "I conducted a project on predicting heart disease using various computer methods like Decision Trees, "
             "Random Forest, Logistic Regression, Naive Bayes, and XGBoost. After testing them all, I chose to use "
             "XGBoost because it worked best. My project could help doctors detect heart problems earlier and more "
             "accurately, which could save lives in the future.")

elif page_selected == "Educational Information":
    # Showing the information related to heart disease
    st.title("Useful Information")
    # The videos about heart disease are shown
    st.write("Here are some educational resources:")
    st.write("[Video 1: Mayo Clinic Minute: What is heart disease?](https://www.youtube.com/watch?v=Oqt9TgWcrxI)")
    st.write("[Video 2: Heart Disease - Causes, Symptoms and Treatment Options]("
             "https://www.youtube.com/watch?v=aXDaBuPSvJs)")

elif page_selected == "Prediction System":
    # Creating function to categorize age
    def categorize_age(age):
        if age <= 9:
            return 1
        elif 10 <= age <= 19:  # 10-19
            return 2
        elif 20 <= age <= 29:  # 20-29
            return 3
        elif 30 <= age <= 39:  # 30-39
            return 4
        elif 40 <= age <= 49:  # 40-49
            return 5
        elif 50 <= age <= 59:  # 50-59
            return 6
        elif 60 <= age <= 69:  # 60-69
            return 7
        elif 70 <= age <= 79:  # 70-79
            return 8
        elif 80 <= age <= 89:  # 80-89
            return 9
        elif 90 <= age <= 99:  # 90-99
            return 10
        elif 100 <= age <= 109:  # 100-109
            return 11
        elif 110 <= age <= 119:  # 110-119
            return 12
        else:
            return 13  # For age 120 and above

    # Function to categorize income
    def categorize_income(income):
        if income < 10000:
            return 1
        elif 10000 <= income <= 14999:
            return 2
        elif 15000 <= income <= 19999:
            return 3
        elif 20000 <= income <= 24999:
            return 4
        elif 25000 <= income <= 34999:
            return 5
        elif 35000 <= income <= 49999:
            return 6
        elif 50000 <= income <= 74999:
            return 7
        else:
            return 8  # 75000 and above

    # Giving options for language English and Malay
    language = st.selectbox('Select Language:', ['English', 'Malay'])

    # Define the steps of the prediction process
    working_steps = [
        'Columns Description:',
        'Enter your Symptoms:',
        'Prediction Result'
    ]

    # Step indicator
    step = st.progress(0)

    # Function to update the step
    def update_step(current_step):
        step.progress(current_step / (len(working_steps) - 1))

    # Malay translations for column descriptions
    malay_column_translations = {
        '1.Sex: Male/Female': '1.Jantina: Lelaki/Perempuan',
        '2.High Blood Pressure: Do you have High Blood Pressure (No/Yes)?': '2.Tekanan Darah Tinggi: '
                                                                            'Adakah anda mempunyai Tekanan Darah '
                                                                            'Tinggi (Tidak/Ya)?',
        '3.High Cholesterol: Do you have High Cholesterol (No/Yes)?': '3.Kolesterol Tinggi: Adakah anda '
                                                                      'mempunyai Kolesterol Tinggi (Tidak/Ya)?',
        '4.Smoker: Are you a smoker (No/Yes)?': '4.Perokok: Adakah anda perokok (Tidak/Ya)?',
        '5.Stroke: Did you ever suffer a stroke (No/Yes)?': '5.Strok: Adakah anda pernah mengalami '
                                                            'strok (Tidak/Ya)?',
        '6.Difficulty Walking: Do you have difficulty in Walking (No/Yes)?': '6.Kesukaran Berjalan: '
                                                                             'Adakah anda mengalami kesukaran dalam '
                                                                             'berjalan (Tidak/Ya)?',
        '7.Diabetes: Diabetes Type (0 for No Diabetes, 1 for Type 1 Diabetes, 2 for Type 2 Diabetes)': '7.Kencing '
                                                                                                       'Manis: Jenis '
                                                                                                       'Kencing Manis '
                                                                                                       '(0 untuk Tiada '
                                                                                                       'Kencing Manis, '
                                                                                                       '1 untuk '
                                                                                                       'Kencing '
                                                                                                       'Manis Jenis 1, '
                                                                                                       '2 untuk '
                                                                                                       'Kencing '
                                                                                                       'Manis Jenis 2)',
        '8.Physical Activity: Do you engage in any physical activities or exercises such as running, '
        'callisthenics, golf, gardening, or walking for exercise?': '8.Aktiviti Fizikal: Adakah anda terlibat dalam '
                                                                    'sebarang aktiviti fizikal atau senaman seperti '
                                                                    'berlari, senaman callisthenics, golf, berkebun, '
                                                                    'atau berjalan untuk bersenam?',
        '9.General Health: How would you rate your general health? (Excellent to Fair)': '9.Kesihatan Am: Bagaimana '
                                                                                         'anda menilai kesihatan am '
                                                                                         'anda? (Cemerlang hingga '
                                                                                         'Sederhana)',
        '10.Physical Health: How many days during the past 30 days was your physical health not good (e.g., '
        'due to pain, discomfort)?': '10.Kesihatan Fizikal: Berapa banyak hari semasa 30 hari yang lalu kesihatan '
                                     'fizikal anda tidak baik (contohnya, disebabkan oleh sakit, ketidakselesaan)?',
        '11.Age: What\'s your age?': '11.Umur: Berapakah umur anda?',
        '12.Education: What\'s your education level?': '12.Pendidikan: Tahap pendidikan anda?',
        '13.Income: What\'s your annual income?': '13.Pendapatan: Berapakah pendapatan tahunan '
                                                  'anda?'
    }

    # Malay translations for input labels
    malay_input_translations = {
        'Sex': 'Jantina',
        'Male': 'Lelaki',
        'Female': 'Perempuan',
        'High Blood Pressure': 'Tekanan Darah Tinggi',
        'High Cholesterol': 'Kolesterol Tinggi',
        'Smoker': 'Perokok',
        'Stroke': 'Strok',
        'Difficulty Walking': 'Kesukaran Berjalan',
        'Diabetes Type': 'Jenis Kencing Manis',
        'No Diabetes': 'Tiada Kencing Manis',
        'Type 1 Diabetes': 'Kencing Manis Jenis 1',
        'Type 2 Diabetes': 'Kencing Manis Jenis 2',
        'Excellent': 'Cemerlang',
        'Very Good': 'Sangat Baik',
        'Good': 'Baik',
        'Fair': 'Sederhana',
        'Poor': 'Buruk',
        'No education': 'Tiada pendidikan',
        'Elementary': 'Sekolah Rendah',
        'High School Diploma': 'Diploma Sekolah Menengah',
        'Bachelors': 'Ijazah Sarjana Muda',
        'Masters': 'Ijazah Sarjana',
        'PhDs and above': 'PhD dan ke atas',
        'General Health': 'Kesihatan Am',
        'Physical Health': 'Kesihatan Fizikal',
        'Age': 'Umur',
        'Physical Activity': 'Aktiviti Fizikal',
        'No': 'Tidak',
        'Yes': 'Ya',
        'Education': 'Pendidikan',
        'Income': 'Pendapatan',
        'Person has Heart Disease': 'Individu mempunyai Penyakit Jantung',
        'Person does not have Heart Disease': 'Individu tidak mempunyai Penyakit Jantung'
    }

    # Function to translate text based on the selected language
    def translate_text(text, language):
        if language == 'Malay':
            return malay_column_translations.get(text, text)
        return text

    # Function to translate input labels based on the selected language
    def translate_input(text, language):
        if language == 'Malay':
            return malay_input_translations.get(text, text)
        return text

    # Function to determine the general health category based on selected checkboxes
    def determine_gen_hlth(high_bp, high_chol, smoker, stroke, diff_walk):
        options = []
        if high_bp and high_chol and smoker:
            # If High Blood Pressure, High Cholesterol, and Smoker are selected, show only "Good," "Fair," and "Poor"
            options.extend([
                translate_input("Good", language),
                translate_input("Fair", language),
                translate_input("Poor", language)
            ])
        elif smoker and high_chol and diff_walk:
            # If all three checkboxes are selected, show only "Good," "Fair," and "Poor"
            options.extend([
                translate_input("Good", language),
                translate_input("Fair", language),
                translate_input("Poor", language)
            ])
        elif stroke and smoker and high_bp:
            # If stroke, smoker, and high bp are selected, show only "Good," "Fair," and "Poor"
            options.extend([
                translate_input("Good", language),
                translate_input("Fair", language),
                translate_input("Poor", language)
            ])
        elif high_bp and high_chol and smoker and stroke and diff_walk:
            # If any of the checkboxes are selected, show "Fair" and "Poor"
            options.extend([
                translate_input("Fair", language),
                translate_input("Poor", language)
            ])
        else:
            # If none of the checkboxes are selected, show "Excellent," "Very Good," "Good," "Fair," and "Poor"
            options.extend([
                translate_input("Excellent", language),
                translate_input("Very Good", language),
                translate_input("Good", language),
                translate_input("Fair", language),
                translate_input("Poor", language)
            ])
        return options

    # Function to determine the maximum allowable value for Physical Health
    def determine_max_phys_hlth(high_bp, high_chol, smoker, stroke, diff_walk):
        # If all checkboxes are selected, limit to 10 days
        if high_bp and high_chol and smoker and stroke and diff_walk:
            return 10
        else:
            # If any checkbox is not selected or a random combination is selected, allow up to 30 days
            return 30

    # Information for the variables to help users understand better
    update_step(0)
    st.subheader(translate_text(working_steps[0], language))
    st.write(translate_text('1.Sex: Male/Female', language))
    st.write(translate_text('2.High Blood Pressure: Do you have High Blood Pressure (No/Yes)?', language))
    st.write(translate_text('3.High Cholesterol: Do you have High Cholesterol (No/Yes)?', language))
    st.write(translate_text('4.Smoker: Are you a smoker (No/Yes)?', language))
    st.write(translate_text('5.Stroke: Did you ever suffer a stroke (No/Yes)?', language))
    st.write(translate_text('6.Difficulty Walking: Do you have difficulty in Walking (No/Yes)?', language))
    st.write(
        translate_text("7.Diabetes: Diabetes Type (0 for No Diabetes, 1 for Type 1 Diabetes, 2 for Type 2 Diabetes)",
                       language))
    st.write(
        translate_text("8.Physical Activity: Do you engage in any physical activities or exercises such as running, "
                       "callisthenics, golf, gardening, or walking for exercise?", language))
    st.write(translate_text("9.General Health: How would you rate your general health? (Excellent to Fair)", language))
    st.write(translate_text(
        "10.Physical Health: How many days during the past 30 days was your physical health not good (e.g., "
        "due to pain, discomfort)?", language))
    st.write(translate_text("11.Age: What's your age?", language))
    st.write(translate_text("12.Education: What's your education level?", language))
    st.write(translate_text("13.Income: What's your annual income?", language))

    # Asking the user for input to make a prediction
    update_step(1)
    st.subheader(translate_text(working_steps[1], language))
    sex = st.radio(translate_input('Sex', language),
                   [translate_input('Male', language), translate_input('Female', language)])
    high_bp = st.checkbox(translate_input('High Blood Pressure', language))
    high_chol = st.checkbox(translate_input('High Cholesterol', language))
    smoker = st.checkbox(translate_input('Smoker', language))
    stroke = st.checkbox(translate_input('Stroke', language))
    diff_walk = st.checkbox(translate_input('Difficulty Walking', language))
    diabetes_type = st.selectbox(translate_input('Diabetes Type', language),
                                 [translate_input('No Diabetes', language),
                                  translate_input('Type 1 Diabetes', language),
                                  translate_input('Type 2 Diabetes', language)])
    gen_hlth = st.selectbox(translate_input('General Health', language),
                            determine_gen_hlth(high_bp, high_chol, smoker, stroke, diff_walk))

    # Calculate the maximum allowable value for Physical Health
    max_phys_hlth = determine_max_phys_hlth(high_bp, high_chol, smoker, stroke, diff_walk)

    phys_hlth = st.slider(translate_input('Physical Health', language), 0, max_phys_hlth)
    age = st.number_input(translate_input('Age', language), min_value=0, max_value=125)
    phys_activity = st.selectbox(translate_input('Physical Activity', language),
                                 [translate_input('No', language), translate_input('Yes', language)])
    education = st.selectbox(translate_input('Education', language),
                             [translate_input('No education', language), translate_input('Elementary', language),
                              translate_input('High School Diploma', language), translate_input('Bachelors', language),
                              translate_input('Masters', language), translate_input('PhDs and above', language)])

    # Replace the income input section with a dropdown
    income_range = st.selectbox(translate_input('Income', language), [
        'Less than RM10000',
        'RM10000-14999',
        'RM15000-19999',
        'RM20000-24999',
        'RM25000-34999',
        'RM35000-49999',
        'RM50000-74999',
        'RM75000 and above'
    ])

    # Map the selected income range to a numerical category
    income_value_mapping = {
        'Less than RM10000': 1,
        'RM10000-14999': 2,
        'RM15000-19999': 3,
        'RM20000-24999': 4,
        'RM25000-34999': 5,
        'RM35000-49999': 6,
        'RM50000-74999': 7,
        'RM75000 and above': 8
    }

    income_value = income_value_mapping.get(income_range, 1)  # Default to 1 if not in the mapping

    # Convert the user's age input to age category
    age_category = categorize_age(age)

    # Map sex to numerical values
    sex_mapping = {translate_input('Male', language): 0, translate_input('Female', language): 1}
    sex = sex_mapping.get(sex, 0)  # Default to "Male" if not in the mapping

    # Map diabetes type to numerical values
    if diabetes_type == translate_input("No Diabetes", language):
        diabetes_type = 0
    elif diabetes_type == translate_input("Type 1 Diabetes", language):
        diabetes_type = 1
    elif diabetes_type == translate_input("Type 2 Diabetes", language):
        diabetes_type = 2

    # Map general health to numerical values
    gen_hlth_mapping = {
        translate_input("Excellent", language): 1,
        translate_input("Very Good", language): 2,
        translate_input("Good", language): 3,
        translate_input("Fair", language): 4,
        translate_input("Poor", language): 5
    }
    gen_hlth = gen_hlth_mapping.get(gen_hlth, 3)  # Default to "Good" if not in the mapping

    # Map education to numerical values
    education_mapping = {
        translate_input("No education", language): 1,
        translate_input("Elementary", language): 2,
        translate_input("High School Diploma", language): 3,
        translate_input("Bachelors", language): 4,
        translate_input("Masters", language): 5,
        translate_input("PhDs and above", language): 6
    }
    education = education_mapping.get(education, 1)  # Default to "No education" if not in the mapping

    # Categorize income
    income_category = categorize_income(income_value)

    # Convert "Yes/No" checkboxes to numerical inputs (0 for No, 1 for Yes)
    high_bp = 1 if high_bp else 0
    high_chol = 1 if high_chol else 0
    smoker = 1 if smoker else 0
    stroke = 1 if stroke else 0
    diff_walk = 1 if diff_walk else 0
    phys_activity = 1 if phys_activity == translate_input('Yes', language) else 0

    # Create a feature vector from user inputs
    user_input = [sex, high_bp, high_chol, smoker, stroke, diff_walk, diabetes_type, phys_activity, gen_hlth, phys_hlth,
                  age_category, education, income_category]

    # Predicting the result based on the loaded model
    if st.button(translate_text('Predict', language)):
        update_step(2)
        st.subheader(translate_text(working_steps[2], language))
        prediction = model_loaded.predict([user_input])[0]
        if prediction == 0:
            result_text = translate_input("Person does not have Heart Disease", language)
            st.markdown(f'<h3 style="color:red;">{result_text}</h3>', unsafe_allow_html=True)
        else:
            result_text = translate_input("Person has Heart Disease", language)
            st.markdown(f'<h3 style="color:green;">{result_text}</h3>', unsafe_allow_html=True)
