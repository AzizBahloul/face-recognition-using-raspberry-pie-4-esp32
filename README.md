# 🔐 Employee Presence Detection & Smart Lock System

An advanced IoT-based presence detection and smart lock system combining facial recognition, real-time monitoring, and secure access control for modern workplace solutions.

![Arduino](https://img.shields.io/badge/Arduino-ESP32-blue.svg)
![Raspberry Pi](https://img.shields.io/badge/Raspberry%20Pi-4B+-green.svg)
![Python](https://img.shields.io/badge/Python-3.7+-yellow.svg)
![Firebase](https://img.shields.io/badge/Firebase-Realtime%20DB-orange.svg)
![License](https://img.shields.io/badge/License-MIT-red.svg)

## 📋 Table of Contents

- [Overview](#overview)
- [System Architecture](#system-architecture)
- [Features](#features)
- [Hardware Requirements](#hardware-requirements)
- [Repository Structure](#repository-structure)
- [Installation Guide](#installation-guide)
- [Configuration](#configuration)
- [Usage](#usage)
- [API Documentation](#api-documentation)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

## 🎯 Overview

This project implements a comprehensive employee presence detection and smart lock system designed for modern workplaces. The system combines facial recognition technology with IoT devices to provide secure, automated access control and accurate attendance tracking.

### Key Components
- **ESP32-CAM**: Captures high-quality images for facial recognition
- **Raspberry Pi**: Processes facial recognition algorithms
- **Firebase**: Cloud database for employee data and access logs
- **Arduino IDE**: Development environment for microcontroller programming

## 🏗️ System Architecture

```
┌─────────────────┐    ┌──────────────────┐    ┌─────────────────┐
│   ESP32-CAM     │    │   Raspberry Pi   │    │    Firebase     │
│                 │    │                  │    │                 │
│ • Image Capture │◄──►│ • Face Recognition│◄──►│ • User Database │
│ • WiFi Module   │    │ • Access Control │    │ • Access Logs   │
│ • LED Indicator │    │ • Model Training │    │ • Real-time Sync│
└─────────────────┘    └──────────────────┘    └─────────────────┘
         │                        │                        │
         └────────────────────────┼────────────────────────┘
                                  │
                        ┌─────────▼─────────┐
                        │   Smart Lock      │
                        │   Control Unit    │
                        └───────────────────┘
```

## ✨ Features

### 🔹 Core Functionality
- **Real-time Facial Recognition**: Advanced face detection and recognition algorithms
- **Automated Access Control**: Smart lock integration with secure authentication
- **Employee Attendance Tracking**: Comprehensive logging and reporting system
- **Cloud Integration**: Firebase real-time database synchronization
- **Multi-device Support**: Seamless integration between ESP32, Raspberry Pi, and cloud services

### 🔹 Advanced Features
- **Live Monitoring**: Real-time surveillance and access monitoring
- **Remote Management**: Cloud-based system administration
- **Scalable Architecture**: Support for multiple access points
- **Data Analytics**: Employee presence patterns and insights
- **Security Alerts**: Unauthorized access attempt notifications
- **Backup Systems**: Multiple authentication fallback methods

## 🛠️ Hardware Requirements

### Essential Components

| Component | Model/Specification | Quantity | Purpose |
|-----------|-------------------|----------|---------|
| **ESP32-CAM** | ESP32-CAM-MB | 1+ | Image capture and processing |
| **Raspberry Pi** | RPi 4B (4GB RAM min.) | 1 | Main processing unit |
| **MicroSD Card** | 32GB+ Class 10 | 2 | Storage for Pi and ESP32 |
| **Power Supply** | 5V 3A (Pi), 5V 2A (ESP32) | 2 | System power |
| **Camera Module** | Built-in ESP32-CAM | 1 | Facial image capture |
| **Smart Lock** | Electronic door lock | 1 | Physical access control |

### Optional Components
- **LED Status Indicators**: Visual feedback system
- **Buzzer/Speaker**: Audio notifications
- **External Antenna**: Enhanced WiFi range
- **Backup Battery**: Uninterrupted power supply
- **Enclosure**: Weather-resistant housing

### Network Requirements
- **WiFi Network**: 2.4GHz/5GHz dual-band
- **Internet Connection**: Minimum 10 Mbps for cloud sync
- **Firebase Account**: Google Cloud Platform access

## 📁 Repository Structure

```
Employee-Presence-Detection-System/
│
├── 📁 Arduino/                          # Arduino ecosystem files
│   └── 📁 ESP32CAM-FIREBASE/           # ESP32-CAM integration
│       ├── ESP32CAM-FIREBASE.ino       # Main ESP32 firmware
│       ├── config.h                    # WiFi and Firebase config
│       ├── camera_handler.cpp          # Camera control functions
│       └── firebase_utils.cpp          # Firebase communication
│
├── 📁 esp32_board/                     # ESP32-specific implementations
│   ├── board_config.json              # Hardware configuration
│   ├── pin_definitions.h               # GPIO pin mappings
│   └── system_diagnostics.ino         # Hardware testing suite
│
├── 📁 raspberry_pi/                    # Raspberry Pi components
│   ├── 📁 dataset/                     # Training data management
│   │   ├── employees/                  # Employee facial images
│   │   ├── visitors/                   # Temporary access images
│   │   └── validation/                 # Model validation data
│   │
│   ├── 📁 models/                      # Machine learning models
│   │   ├── face_recognition.pkl        # Trained recognition model
│   │   └── encodings.pickle            # Facial encoding data
│   │
│   ├── 📁 config/                      # Configuration files
│   │   ├── firebase_config.json        # Firebase credentials
│   │   ├── system_settings.json        # System parameters
│   │   └── camera_config.json          # Camera settings
│   │
│   ├── 📁 logs/                        # System logs
│   │   ├── access_logs.txt             # Access attempt records
│   │   ├── system_errors.log           # Error tracking
│   │   └── performance_metrics.log     # System performance data
│   │
│   ├── 📄 facial_req.py                # Main facial recognition engine
│   ├── 📄 train_model.py               # Model training pipeline
│   ├── 📄 database_manager.py          # Firebase database operations
│   ├── 📄 access_controller.py         # Smart lock control logic
│   ├── 📄 system_monitor.py            # Health monitoring service
│   └── 📄 requirements.txt             # Python dependencies
│
├── 📁 docs/                            # Documentation
│   ├── installation_guide.md           # Step-by-step setup
│   ├── api_reference.md               # API documentation
│   ├── troubleshooting.md             # Common issues and solutions
│   └── hardware_setup.md              # Hardware assembly guide
│
├── 📁 scripts/                         # Utility scripts
│   ├── setup_environment.sh           # Automated setup script
│   ├── backup_system.py               # Data backup utilities
│   └── system_update.sh               # System maintenance script
│
├── 📄 README.md                        # This file
├── 📄 LICENSE                          # MIT License
├── 📄 CHANGELOG.md                     # Version history
└── 📄 requirements.txt                 # Global dependencies
```

## 🚀 Installation Guide

### Prerequisites
- Basic knowledge of Arduino IDE and Python
- Active internet connection
- Google Firebase account
- Administrative access to target devices

### Step 1: Environment Setup

#### 1.1 Clone Repository
```bash
git clone https://github.com/YourUsername/Employee-Presence-Detection-System.git
cd Employee-Presence-Detection-System
```

#### 1.2 Setup Raspberry Pi
```bash
# Update system packages
sudo apt update && sudo apt upgrade -y

# Install system dependencies
sudo apt install -y python3-pip python3-venv cmake build-essential

# Create virtual environment
python3 -m venv smart_lock_env
source smart_lock_env/bin/activate

# Install Python dependencies
cd raspberry_pi/
pip install -r requirements.txt
```

#### 1.3 Arduino IDE Configuration
```bash
# Install Arduino IDE (if not already installed)
# Add ESP32 board manager URL in Arduino IDE:
# https://dl.espressif.com/dl/package_esp32_index.json

# Install required libraries:
# - Firebase ESP32 Client
# - ESP32Servo
# - ArduinoJson
```

### Step 2: Firebase Setup

#### 2.1 Create Firebase Project
1. Go to [Firebase Console](https://console.firebase.google.com/)
2. Create new project: `employee-presence-system`
3. Enable Realtime Database
4. Configure authentication rules
5. Generate service account key

#### 2.2 Database Structure
```json
{
  "employees": {
    "employee_id": {
      "name": "John Doe",
      "email": "john.doe@company.com",
      "department": "Engineering",
      "access_level": "standard",
      "face_encoding": "base64_encoded_string",
      "active": true
    }
  },
  "access_logs": {
    "timestamp": {
      "employee_id": "emp_001",
      "access_granted": true,
      "location": "main_entrance",
      "timestamp": "2025-01-15T10:30:00Z"
    }
  }
}
```

### Step 3: Hardware Configuration

#### 3.1 ESP32-CAM Setup
```cpp
// Update config.h with your credentials
#define WIFI_SSID "Your_WiFi_Network"
#define WIFI_PASSWORD "Your_WiFi_Password"
#define FIREBASE_HOST "your-project.firebaseio.com"
#define FIREBASE_AUTH "your-database-secret"
```

#### 3.2 Raspberry Pi Configuration
```json
// Update raspberry_pi/config/system_settings.json
{
  "camera": {
    "resolution": [640, 480],
    "fps": 30,
    "flip_horizontal": false,
    "flip_vertical": false
  },
  "recognition": {
    "confidence_threshold": 0.6,
    "face_detection_model": "hog",
    "max_faces_per_frame": 5
  },
  "access_control": {
    "lock_duration": 5,
    "max_attempts": 3,
    "lockout_time": 300
  }
}
```

## ⚙️ Configuration

### Firebase Configuration
```python
# raspberry_pi/config/firebase_config.json
{
  "type": "service_account",
  "project_id": "your-project-id",
  "private_key_id": "your-private-key-id",
  "private_key": "-----BEGIN PRIVATE KEY-----\n...\n-----END PRIVATE KEY-----\n",
  "client_email": "firebase-adminsdk-xxxxx@your-project.iam.gserviceaccount.com",
  "client_id": "your-client-id",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token"
}
```

### System Settings
```python
# raspberry_pi/config/system_settings.json
{
  "system": {
    "debug_mode": false,
    "log_level": "INFO",
    "auto_backup": true,
    "backup_interval": 3600
  },
  "security": {
    "encryption_enabled": true,
    "session_timeout": 1800,
    "max_login_attempts": 5
  }
}
```

## 🖥️ Usage

### Starting the System

#### 1. Initialize Raspberry Pi Service
```bash
cd raspberry_pi/
source smart_lock_env/bin/activate
python facial_req.py --config config/system_settings.json
```

#### 2. Deploy ESP32 Firmware
```bash
# Open Arduino IDE
# Load ESP32CAM-FIREBASE.ino
# Select ESP32-CAM board
# Upload firmware
```

#### 3. System Status Check
```bash
# Check system health
python system_monitor.py --status

# View real-time logs
tail -f logs/access_logs.txt
```

### Adding New Employees

#### 1. Capture Training Images
```bash
python train_model.py --add-employee --name "John Doe" --id "emp_001"
# Follow on-screen instructions to capture multiple face angles
```

#### 2. Train Recognition Model
```bash
python train_model.py --retrain
# System will automatically update the recognition model
```

#### 3. Sync with Firebase
```bash
python database_manager.py --sync-employees
# Uploads employee data to Firebase
```

### Monitoring System

#### Real-time Dashboard
Access the web dashboard at: `http://raspberry_pi_ip:8080`

#### Command Line Monitoring
```bash
# View access logs
python system_monitor.py --logs --filter today

# System performance
python system_monitor.py --performance

# Security alerts
python system_monitor.py --alerts
```

## 📊 API Documentation

### REST API Endpoints

#### Employee Management
```http
GET /api/employees
POST /api/employees
PUT /api/employees/{id}
DELETE /api/employees/{id}
```

#### Access Logs
```http
GET /api/access-logs
GET /api/access-logs/{employee_id}
POST /api/access-logs/export
```

#### System Control
```http
POST /api/system/lock
POST /api/system/unlock
GET /api/system/status
POST /api/system/reset
```

### WebSocket Events
```javascript
// Real-time access events
ws://raspberry_pi_ip:8081/access-events

// System status updates
ws://raspberry_pi_ip:8081/system-status
```

## 🔧 Troubleshooting

### Common Issues

#### ESP32 Connection Problems
```bash
# Problem: ESP32 not connecting to WiFi
# Solution: Check WiFi credentials and signal strength
# Test: Use WiFi scanner to verify network availability
```

#### Facial Recognition Accuracy
```bash
# Problem: Low recognition accuracy
# Solutions:
# 1. Improve lighting conditions
# 2. Capture more training images
# 3. Adjust confidence threshold
# 4. Clean camera lens
```

#### Firebase Connectivity
```bash
# Problem: Firebase authentication errors
# Solutions:
# 1. Verify service account key
# 2. Check internet connectivity
# 3. Validate Firebase project settings
# 4. Review security rules
```

#### Performance Issues
```bash
# Problem: Slow processing
# Solutions:
# 1. Reduce image resolution
# 2. Optimize recognition parameters
# 3. Check system resources
# 4. Consider hardware upgrade
```

### Diagnostic Commands
```bash
# System health check
python system_monitor.py --diagnostics

# Network connectivity test
python system_monitor.py --network-test

# Camera functionality test
python system_monitor.py --camera-test

# Firebase connection test
python database_manager.py --test-connection
```

## 🔄 System Maintenance

### Regular Maintenance Tasks

#### Weekly
- [ ] Check system logs for errors
- [ ] Verify backup integrity
- [ ] Update employee database
- [ ] Clean camera lens

#### Monthly
- [ ] Update system packages
- [ ] Review security settings
- [ ] Performance optimization
- [ ] Hardware inspection

#### Quarterly
- [ ] Retrain recognition model
- [ ] Security audit
- [ ] Hardware replacement planning
- [ ] System documentation update

### Backup and Recovery
```bash
# Create system backup
python scripts/backup_system.py --full-backup

# Restore from backup
python scripts/backup_system.py --restore --date 2025-01-15

# Schedule automatic backups
crontab -e
# Add: 0 2 * * * /path/to/backup_system.py --auto-backup
```

## 🤝 Contributing

We welcome contributions from the community! Here's how you can help:

### Types of Contributions
- 🐛 **Bug Reports**: Report issues with detailed reproduction steps
- 💡 **Feature Requests**: Suggest new functionality and improvements
- 📝 **Documentation**: Improve guides, API docs, and code comments
- 🔧 **Code Contributions**: Submit pull requests with enhancements
- 🧪 **Testing**: Help test new features and report feedback

### Development Workflow
1. **Fork** the repository
2. **Create** a feature branch (`git checkout -b feature/amazing-feature`)
3. **Implement** your changes with proper testing
4. **Document** your changes thoroughly
5. **Test** across different hardware configurations
6. **Commit** with descriptive messages (`git commit -m 'Add amazing feature'`)
7. **Push** to your branch (`git push origin feature/amazing-feature`)
8. **Create** a Pull Request with detailed description

### Coding Standards
- Follow PEP 8 for Python code
- Use meaningful variable and function names
- Include comprehensive docstrings
- Add unit tests for new functionality
- Maintain backward compatibility when possible

### Testing Guidelines
```bash
# Run unit tests
python -m pytest tests/

# Run integration tests
python -m pytest tests/integration/

# Performance testing
python -m pytest tests/performance/ --benchmark
```

## 📈 Roadmap

### Version 2.0 (Q2 2025)
- [ ] **Mobile App Integration**: iOS/Android companion app
- [ ] **Multi-location Support**: Manage multiple access points
- [ ] **Advanced Analytics**: ML-powered insights and predictions
- [ ] **Voice Commands**: Alexa/Google Assistant integration

### Version 2.1 (Q3 2025)
- [ ] **Biometric Enhancement**: Fingerprint integration
- [ ] **Edge AI Processing**: On-device ML inference
- [ ] **Advanced Security**: End-to-end encryption
- [ ] **API Gateway**: RESTful API management

### Version 3.0 (Q4 2025)
- [ ] **AI Behavior Analysis**: Anomaly detection
- [ ] **Scalability Improvements**: Enterprise-grade architecture
- [ ] **Integration Platform**: Third-party system connectors
- [ ] **Advanced Reporting**: Business intelligence dashboards

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for complete details.

### License Summary
```
MIT License - Permission is hereby granted, free of charge, to any person obtaining 
a copy of this software and associated documentation files (the "Software"), to 
deal in the Software without restriction, including without limitation the rights 
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies 
of the Software, and to permit persons to whom the Software is furnished to do so, 
subject to the following conditions:

✅ Commercial use allowed
✅ Modification allowed  
✅ Distribution allowed
✅ Private use allowed
❌ No warranty provided
❌ No liability assumed
```

## 🙏 Acknowledgments

### Open Source Libraries
- **OpenCV**: Computer vision and image processing
- **face_recognition**: Facial recognition algorithms
- **Firebase Admin SDK**: Cloud database integration
- **Flask**: Web framework for API endpoints

### Hardware Partners
- **Espressif Systems**: ESP32 development platform
- **Raspberry Pi Foundation**: Single-board computer ecosystem

### Community Contributors
Special thanks to all developers, testers, and documentation contributors who make this project possible.

 
 

### Professional Support
For enterprise implementations, custom development, or professional support, please contact us directly.

---

<div align="center">

**⭐ Star this project if you find it useful! ⭐**

[![GitHub stars](https://img.shields.io/github/stars/YourUsername/Employee-Presence-Detection-System.svg?style=social&label=Star)](https://github.com/YourUsername/Employee-Presence-Detection-System/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/YourUsername/Employee-Presence-Detection-System.svg?style=social&label=Fork)](https://github.com/YourUsername/Employee-Presence-Detection-System/network)

</div>
