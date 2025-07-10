# pytestApiFramework
# Pytest API Testing Framework 🧪

This project is a clean and modular API automation testing framework built using **Python**, **Pytest**, and **Requests**. It covers real-world API testing scenarios including **authentication**, **create/update booking**, and **data validation**.

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
