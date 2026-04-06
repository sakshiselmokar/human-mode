# 🧠 human-mode

A **smart CLI tool** that reminds you to *actually be human*.

Most reminder apps just spam notifications. This one adapts to your **behavior and focus**.

---

## 🎬 Demo Video

[Watch the demo](https://youtu.be/zNaKq_OiQ2g?feature=shared)

Click to watch **human-mode in action**!

---

## 🚀 Features

* ⏱️ **Smart reminders**: 10s, 5m, 1h
* 🧠 **Activity-aware**: delays alerts when idle, fires when you’re focused
* ⚡ **Lightweight & fast**: minimal dependencies
* 📊 **Usage analytics**: get a human report
* ⚠️ **Burnout detection**: warns during long work sessions
* 🔔 **Now alerts**: instant notifications for critical tasks
* 🖥️ **Desktop notifications**: alerts show up right on your screen

---

## 📦 Installation

```bash
pip install human-mode
```

---

## 🛠️ Usage

### Add a reminder

```bash
human add "drink water" 30m
human add "stretch" 1h
human add "blink" 10s
```

### Run reminders

```bash
human run
```

### View report

```bash
human report
```

Example output:

```text
📊 Human Mode Report
Total reminders: 5
Active time: 12.5 minutes
Burnout risk: Low 😊
```

---

## 🪟 Windows Note

If you see `'human' is not recognized as a command`, add the CLI to your PATH:

**Temporary:**

```powershell
$env:Path += ";C:\Users\<your-username>\AppData\Roaming\Python\Python3xx\Scripts"
```

**Permanent:**

1. Open **Environment Variables**
2. Edit **Path**
3. Add: `C:\Users\<your-username>\AppData\Roaming\Python\Python3xx\Scripts`
4. Restart your terminal

---

## 💡 Why this exists

I tried multiple reminder apps — all of them:

* Required accounts
* Ran heavy background services
* Sent annoying notifications

So I built something **simple and effective**:

* No cloud
* No accounts
* Just a CLI tool that adapts to your work

---

## 🧠 How it works

* Tracks **system activity** (CPU usage as a proxy)
* Delays reminders when you’re focused
* Skips reminders when idle
* Fires **critical “Now” alerts** immediately
* Shows **desktop notifications**
* Tracks usage for **insights**

---

## 📁 Project Structure

```text
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
* `psutil` for activity detection

---

## 🚧 Future Improvements

* Daily/weekly reports
* ML-based focus detection
* Plugin system (Slack, etc.)

---

## 🤝 Contributing

PRs and suggestions are welcome!

---

## ⭐ Found this useful?

Give it a star on GitHub 🙌
