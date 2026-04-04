# 🖱️ Clicker2

A browser-based clicker game with upgrade system, data persistence, and mobile support. Built with Flask, this game works seamlessly on both desktop and mobile devices.

## ✨ Features

- **Click to earn** — Core clicking mechanic with satisfying feedback
- **Upgrade system** — Purchase upgrades to increase clicks per action
- **Auto-clickers** — Hire automated clickers that generate points while you're away
- **Data persistence** — Your progress is automatically saved and restored
- **Mobile responsive** — Fully playable on phones and tablets
- **Real-time updates** — No page refresh needed for game state updates

## 🛠️ Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: SQLite / (your choice)
- **Version Control**: Git & GitHub
- **Package Management**: uv (fast Python package installer)
- **Dependencies**: Flask, Flask-SQLAlchemy (optional)

## 📋 Prerequisites

- Python 3.8+
- uv package manager
- Git
- Modern web browser (Chrome, Firefox, Safari, Edge)

## 🚀 Installation

### 1. Clone the repository

```bash
git clone https://github.com/fyzov/clicker2.git
cd clicker2
```

### 2. Install dependencies with uv

```bash
uv pip install -r requirements.txt
```

Or if using pyproject.toml:

```bash
uv sync
```

### 3. Set up the database

```bash
python init_db.py
```

### 4. Run the application

```bash
python app.py
```

### 5. Open in browser

Navigate to: **http://localhost:5000**

## 📱 Mobile Access

### On the same network:

1. Find your computer's IP address:
   - **Windows**: `ipconfig` (look for IPv4 Address)
   - **Mac/Linux**: `ifconfig` or `ip addr`

2. Run Flask with host access:
```bash
flask run --host=0.0.0.0
```

3. On your phone, open: `http://YOUR_COMPUTER_IP:5000`

> ⚠️ Make sure both devices are on the same Wi-Fi network

## 🎮 How to Play

1. **Click** the main button to earn points
2. **Buy upgrades** to increase points per click
3. **Hire auto-clickers** to earn points automatically every second
4. **Progress saves automatically** — close the browser and come back later!

## 📁 Project Structure

```
clicker2/
├── app.py              # Main Flask application
├── requirements.txt    # Python dependencies
├── init_db.py         # Database initialization script
├── source/
│   └── app.py         # Additional routes/modules
├── static/
│   ├── css/
│   │   └── style.css  # Styling
│   └── js/
│       └── game.js    # Game logic
├── templates/
│   └── index.html     # Main game page
└── instance/
    └── clicker.db     # SQLite database (auto-created)
```

## 🔄 Git Workflow

### Check current status
```bash
git status
```

### Commit changes
```bash
git add .
git commit -m "fix: correct import in api.py"
git push origin main
```

### View branch structure
```bash
git log --oneline --graph --all --decorate
```

## 🐛 Common Issues & Solutions

### "Already up to date" when merging
This means the branch is already merged. Check with:
```bash
git log main..branch_name --oneline
```

### Port 5000 already in use
```bash
flask run --port=5001
```

### Mobile can't connect
- Check firewall settings
- Ensure Flask is running on `0.0.0.0`
- Try using `http://localhost:5000` from the computer first

## 🧪 Development

### Run in debug mode
```bash
flask run --debug
```

### Add new upgrade
1. Edit the upgrade data in `game.js`
2. Add corresponding backend logic in `app.py`
3. Update database schema if needed

## 📦 Deployment

### Deploy on Render/Railway
1. Push to GitHub
2. Connect repository to hosting service
3. Set environment variables:
   - `SECRET_KEY`
   - `DATABASE_URL`
4. Deploy!

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/amazing`
3. Commit changes: `git commit -m "feat: add amazing feature"`
4. Push: `git push origin feature/amazing`
5. Open a Pull Request

## 📄 License

MIT License — feel free to use and modify!

## 📞 Support

- Open an issue on GitHub
- Check existing issues for solutions

---

**Happy clicking! 🖱️💥**
