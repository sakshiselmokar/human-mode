# 🧠 human-mode

A smart CLI tool that reminds you to *actually be human*.

Most reminder apps just spam notifications.
This one adapts to your behavior.

---

## 🚀 Features

* ⏱️ Smart reminders (`10s`, `5m`, `1h`)
* 🧠 Activity-aware (won’t interrupt when idle)
* ⚡ Lightweight & fast (minimal dependencies)
* 📊 Usage analytics (`human report`)
* ⚠️ Burnout detection (long work session alerts)

---

## 📦 Installation

```bash
pip install human-mode
```

---

## 🛠️ Usage

### ➤ Add a reminder

```bash
human add "drink water" 30m
human add "stretch" 1h
human add "blink" 10s
```

---

### ➤ Run reminders

```bash
human run
```

---

### ➤ View report

```bash
human report
```

Example output:

```
📊 Human Mode Report
Total reminders: 5
Active time: 12.5 minutes
Burnout risk: Low 😊
```

---

## 🪟 Windows Note (Important)

If you see this error:

```
'human' is not recognized as a command
```

It means your system cannot find the installed CLI.

### ✅ Quick Fix (temporary)

```powershell
$env:Path += ";C:\Users\<your-username>\AppData\Roaming\Python\Python3xx\Scripts"
```

---

### ✅ Permanent Fix

1. Open **Environment Variables**
2. Edit **Path**
3. Add:

```
C:\Users\<your-username>\AppData\Roaming\Python\Python3xx\Scripts
```

4. Restart your terminal

---

## 💡 Why this exists

I tried multiple reminder apps.

Most of them:

* Required accounts
* Ran heavy background services
* Sent annoying notifications

So I built something simple:

* No cloud
* No accounts
* Just a CLI tool that adapts to how you work

---

## 🧠 How it works

* Tracks system activity (CPU usage as a proxy)
* Delays reminders when you're focused
* Skips reminders when you're idle
* Tracks usage to generate insights

---

## 📁 Project Structure

```
human-mode/
│
├── human_mode/
│   ├── cli.py
│   ├── reminder.py
│   └── utils.py
│
├── setup.py
├── README.md
└── requirements.txt
```

---

## ⚙️ Tech Stack

* Python (stdlib + minimal dependencies)
* `psutil` (for activity detection)

---

## 🚧 Future Improvements

* Desktop notifications
* Daily/weekly reports
* ML-based focus detection
* Plugin system (Slack, etc.)

---

## 🤝 Contributing

PRs and suggestions are welcome!

---

## ⭐ If you found this useful

Give it a star on GitHub — it helps a lot 🙌
