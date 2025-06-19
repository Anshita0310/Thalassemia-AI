# 🧬 Thalassemia AI Screening & Donor Matching

An AI-powered web application that performs thalassemia risk screening based on basic health data, and helps match suitable blood donors with patients.

---

## 🚀 Features

- 🤖 **AI-Based Risk Prediction**  
  Predicts the risk of thalassemia based on age, gender, symptoms, and family history using a trained ML model (Logistic Regression).

- 📊 **Prediction Confidence**  
  Displays confidence percentage for each prediction.

- 📈 **Risk Distribution Chart**  
  Live pie chart showing how many users were classified as high risk vs low risk.

- 🩸 **Donor & Patient Management**  
  Register, edit, delete, and view lists of donors and patients with filters.

- 🔗 **Donor-Patient Matching**  
  Match patients with donors based on compatible blood types.

- 🗺 **Route Info with OpenRouteService**  
  View estimated travel distance/time between donor and patient (text-based, no Google billing).

---

## 🛠 Tech Stack

| Part       | Tech Used                     |
|------------|-------------------------------|
| Frontend   | React.js                      |
| Backend    | Flask (Python)                |
| ML Model   | scikit-learn                  |
| Database   | SQLite                        |
| Maps       | OpenRouteService API          |
| Charts     | Recharts (React)              |

---

## 📦 Installation

### 1. Clone the repo

```bash
git clone https://github.com/Anshita0310/Thalassemia-AI.git
cd Thalassemia-AI
```

### 2. Setup Backend (Flask)

```bash
cd thalassemia-server
python -m venv venv
venv\Scripts\activate    # On Windows
pip install -r requirements.txt
python app.py
```

Make sure to place your trained model files:

model.pkl, le_gender.pkl, le_symptoms.pkl, le_family.pkl
in the thalassemia-server/ folder.

### 3. Setup Frontend (React)

```bash
cd ../thalassemia-client
npm install
npm start
```

## 📸 Screenshots

🧪 Screening form & 📊 Pie chart

![image](https://github.com/user-attachments/assets/772c3d93-0450-4ffb-af49-a9572d058b01)

🩸 Donor/patient list

![image](https://github.com/user-attachments/assets/7d22f86c-3cc4-45c9-aded-62c5d38e6d16)
![image](https://github.com/user-attachments/assets/ada83e3f-454c-4277-a226-2e374ad3c04a)

🔗 Match result + route info

![image](https://github.com/user-attachments/assets/cbd71fae-d77b-498b-b133-96fe419b1c64)

📚 Donor & Patient Registration  

![image](https://github.com/user-attachments/assets/b75cd0b9-e3f2-4c72-9fc1-84f493fbf240)
![image](https://github.com/user-attachments/assets/53cd7032-5531-45cc-8294-1212e81b0db1)

## 🧠 AI Model Info

Model: Logistic Regression

Inputs: age, gender, symptoms, family history

Output: Binary classification (High Risk / Low Risk)

Confidence: Calculated via predict_proba()


## View API Collection
Tested via Postman: 
https://anshitajain-187606.postman.co/workspace/Anshita-Jain's-Workspace~d0654ce3-6bca-4fde-86b2-9b79336103c2/collection/45291998-053de3ba-c67a-43be-9581-c31a86de43b9?action=share&creator=45291998

## 🤝Contributing
welcome contributions! Follow these steps:

Fork the repository.

Create a new branch: git checkout -b feature-name

Commit your changes: git commit -m "Added new feature"

Push to the branch: git push origin feature-name

Open a pull request

## 📧Contact
For any questions or suggestions:

Email: anshitajain0310@gmail.com

LinkedIn: https://www.linkedin.com/in/anshita-jain-0b7100263/

GitHub: https://github.com/Anshita0310


## 📜 License
This project is open source and free to use under the MIT License.

### Thank you for visiting! Happy Coding! 🧑‍💻
