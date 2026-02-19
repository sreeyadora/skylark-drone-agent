# 🚁 Drone Coordinator Enterprise System

An enterprise-grade Drone Operations Management Platform built using **Streamlit**, **Google Sheets**, and **Python** to manage pilots, drones, and missions with an intelligent command interface.

This system simulates a real-world drone fleet command center used in industries like surveillance, mapping, inspection, and logistics.

---

## 🌐 Live Application

**Streamlit Deployment:**
https://skylark-drone-agent-9hiavt7ijeyhzlcs82nti4.streamlit.app/

---


## 🎥 Demo Video

Watch the Drone Operations Coordinator AI Agent in action:

(https://drive.google.com/file/d/1-RRA9lhLogVFphCOQCCb27bC3xSwIU-o/view?usp=sharing)


## ✨ Features

### 📊 Enterprise Dashboard

* Total pilots, drones, missions overview
* Available resource tracking
* Real-time data from Google Sheets

### 👨‍✈️ Pilot Management

* View all pilots
* Check availability status
* Search pilots by name
* Update pilot availability

### 🚁 Drone Management

* View full drone fleet
* Check maintenance status
* Monitor drone assignments
* Weather resistance and capabilities tracking

### 📦 Mission Management

* View missions
* Track mission priority
* Monitor mission budget
* View required skills and certifications

### 🤖 AI Command Center (Rule-based AI)

Supports intelligent commands like:

```
show pilots
show drones
show missions
mark Arjun as unavailable
mark Arjun as available
recommend pilot
recommend drone
assign mission
```

---

## 🧠 AI Engine (No OpenAI Used)

This system uses a custom-built rule-based AI engine that can:

* Understand natural commands
* Recommend best pilot based on skills
* Recommend best drone based on capabilities
* Update Google Sheets in real time

---

## 🛠️ Tech Stack

| Technology        | Purpose                   |
| ----------------- | ------------------------- |
| Python            | Core backend              |
| Streamlit         | Frontend UI               |
| Google Sheets API | Database                  |
| Pandas            | Data processing           |
| gspread           | Google Sheets integration |
| Plotly            | Analytics charts          |
| GitHub            | Version control           |
| Streamlit Cloud   | Deployment                |

---

## 📁 Project Structure

```
skylark-drone-agent/
│
├── app.py              # Main Streamlit application
├── agent.py           # AI command engine
├── sheets.py          # Google Sheets integration
├── analytics.py      # Dashboard analytics
├── ui.py             # Custom UI components
├── requirements.txt  # Dependencies
├── README.md         # Project documentation
```

---

## ⚙️ Installation (Run Locally)

### Step 1: Clone Repository

```
git clone https://github.com/sreeyadora/skylark-drone-agent.git
cd skylark-drone-agent
```

### Step 2: Install Dependencies

```
pip install -r requirements.txt
```

### Step 3: Setup Google Credentials

Create file:

```
.streamlit/secrets.toml
```

Paste your Google service account credentials:

```
[gcp_service_account]
type = "service_account"
project_id = "your-project-id"
private_key_id = "your-key-id"
private_key = "YOUR_PRIVATE_KEY"
client_email = "your-email"
client_id = "your-client-id"
token_uri = "https://oauth2.googleapis.com/token"
```

---

### Step 4: Run App

```
streamlit run app.py
```

---

## 🌍 Deployment

This project is deployed using:

**Streamlit Cloud**

Steps:

1. Push code to GitHub
2. Go to Streamlit Cloud
3. Connect GitHub repo
4. Add secrets.toml credentials
5. Deploy

---

## 📊 Data Source

Google Sheets used as database:

* pilot_roster
* drone_fleet
* missions

---

## 🧩 Enterprise Use Cases

This system can be used for:

* Drone fleet management
* Logistics coordination
* Surveillance operations
* Inspection scheduling
* Smart resource allocation

---

## 🔒 Security

* Credentials stored in Streamlit Secrets
* No hardcoded API keys
* Secure cloud deployment

---

## 👩‍💻 Author

**Sreeya Dora**

GitHub:
https://github.com/sreeyadora

---

## ⭐ Future Improvements

* Automated mission assignment
* Predictive maintenance alerts
* Authentication system
* Role-based access
* Real-time notifications

---

## 📜 License

MIT License
