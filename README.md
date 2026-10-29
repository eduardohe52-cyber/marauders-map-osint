# marauders-map-osint
Real-time Wi-Fi tracking and power analysis using ESP32 and Python
# Marauder's Map OSINT Tool (Hardware & RF Hacking)

> *"I solemnly swear that I am up to no good."* - A real-life implementation of the Marauder's Map using ESP32 and Python.

## 📖 Overview
The **Marauder's Map OSINT Tool** is a physical and digital security assessment framework designed to track Wi-Fi devices (Probe Requests) in real-time and correlate their physical presence with electrical consumption anomalies. 

Inspired by the ethical hacking philosophy and classic literature, this project demonstrates how passive RF (Radio Frequency) triangulation and Side-Channel Analysis (Power Monitoring) can be used to map a physical environment without active intrusion.

## 🚀 Key Features
*   **Passive Wi-Fi Tracking:** 4 ESP32 nodes capture `Probe Requests` and RSSI (Signal Strength) in monitor mode.
*   **Trilateration & Kalman Filter:** Python server calculates (X, Y) coordinates and smooths the movement for a fluid, real-time visual map.
*   **Side-Channel Power Analysis:** Integration of non-invasive current sensors (SCT-013) to map electrical consumption and detect unauthorized devices (e.g., cryptojacking or physical bugs).
*   **Boolean Logic Filtering:** Uses `AND NOT` logic to filter out Randomized MACs (locally administered) and false positives.

## 🛠️ Hardware Requirements (BOM)
*   4x ESP32 Development Boards (WROOM / C3)
*   4x 2.4GHz Antennas
*   4x SCT-013 Non-invasive AC Current Sensors (Clamp meters)
*   1x Raspberry Pi 4 (or Kali Linux Laptop)
*   Power banks for wireless ESP32 nodes

## 💻 Software Stack
*   **ESP32 Nodes:** C++ (Arduino IDE / ESP-IDF) for packet sniffing and ADC reading.
*   **Server:** Python 3 (Scapy, PyKalman, Paho-MQTT).
*   **Visualization:** Python (Pygame / Tkinter) or HTML5 Canvas via WebSockets.

## ⚙️ Architecture
1.  **Capture:** ESP32s sniff Wi-Fi packets and electrical current data.
2.  **Transmit:** Data is sent to the central server via MQTT (lightweight IoT protocol).
3.  **Process:** The server applies the Kalman Filter and Trilateration algorithms.
4.  **Display:** The UI draws the "footprints" on a custom map overlay.

## 🛡️ Ethical Guidelines & Cleanup (Crucial)
As an ethical hacking project, privacy is paramount:
*   **No PII Storage:** Captured MAC addresses are hashed or discarded after the real-time rendering. We map *movement*, not *identities*.
*   **Authorization:** This tool is strictly for authorized physical penetration testing and laboratory environments.
*   **Cleanup:** No persistent backdoors or unauthorized data retention.

## 🧠 Lessons Learned & Philosophy
Building this project bridges the gap between **Software (Python/MQTT)**, **Hardware (Relays, ESP32)**, and **Physics (RF and Power Analysis)**. It honors the original MIT hacker ethic: building tools to understand the world, while maintaining strict personal and legal boundaries (The "Knife to the throat" principle).

## 📜 License
This project is licensed under the MIT License. You are free to use, modify, and distribute it, provided you give credit to the original author.

---
*Mischief Managed.*
