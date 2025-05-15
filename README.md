# 📧 Python Auto Mailer using Gmail SMTP and CSV

This script automates the process of sending personalized emails from your Gmail account using Python. It reads recipient details from a CSV file, sends customized emails, and updates the CSV with the send status.

---

## 🚀 Features

- Sends emails via Gmail SMTP
- Reads email addresses and personalized greetings from a `.csv` file
- Automatically adds a `Status` column to track which emails were sent
- Skips emails already marked as `Sent`
- Logs failed sends with `"Failed"` status

---

## 🛠️ Requirements

- Python 3.x
- Gmail account with App Password (Generate this after enabling 2FA on your gmail account.)
- `pandas` library

Install the required dependency:

```bash
pip install pandas
