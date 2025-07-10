# pytestApiFramework
# Pytest API Testing Framework 🧪

This is a **modular, scalable end-to-end test automation framework** built using **Playwright with Python and Pytest**.  
It follows the **Page Object Model (POM)** design pattern and integrates with **CI tools like GitHub Actions** for continuous testing.

The framework is designed to **automatically trigger tests via GitHub Actions** on every `push` or `pull request` to the repository.

---

## 📁 Folder Structure

---

## 🚀 Features

- 🔐 Token-based authentication
- ✅ End-to-end booking flow: Create → Update → Get → Validate
- 🔁 Data verification after updates
- 📦 Organized structure for scalability
- 📄 Config-driven (using `config.json`)
- 🧪 Pytest-compatible test suite
- 📂 Fixtures and reusable utilities (optional)

---

## 📂 Project Structure
pythonapiframework/
├── github/workflows/                # GitHub Actions CI/CD workflows
├── tests/
│   └── test_booking_flow.py         # Test class for booking API
├── utils/
│   └── api_client.py                # Custom API client wrapper over requests
│   └── auth_helper.py               # Authentication helpers
├── conftest.py                      # Common fixtures and test setup
├── config.yaml                      # Configuration (base URL, credentials, etc.)
├── pytest.ini                       # Pytest config
└── requirements.txt                 # Python dependencies


---

## ⚙️ Setup Instructions

### 1. 📥 Clone the repository
```bash
git clone https://github.com/your-username/pythonapiframework.git
cd pythonapiframework
