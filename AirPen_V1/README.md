# 🐺 Air-Pen V1 — Wireless Android Pen Tablet - Samsung

> Turn an Android tablet into a wireless pen-controlled mouse for Windows.

**Air-Pen V1** is the first working version of Air-Pen. It connects an Android tablet to a Windows PC over Wi-Fi and uses a compatible stylus to control the Windows mouse.

The goal of V1 is simple: **make the tablet work as a wireless pen input device.**

---

# 🟢 Air-Pen V1

Air-Pen V1 consists of two parts:

```text
Air-Pen/
│
├── app/
│   └── Android Tablet App
│
├── windows/
│   ├── receiver.py
│   └── requirements.txt
│
└── README.md
```

### Android App

The Android application captures stylus input and sends it to the Windows PC using a WebSocket connection.

### Windows Receiver

The Python receiver listens for the tablet connection and converts the received coordinates into Windows mouse movement.

---

# ✨ Features

* 🖊️ Stylus hover → mouse movement
* 🖱️ Stylus touch → left click
* 🖱️ Hold + move → drag
* ✋ Stylus release → release mouse button
* 📡 Wireless communication over local Wi-Fi
* 🖥️ Automatic Windows screen resolution detection
* 📐 Automatic tablet tracking-area calculation
* 🔄 Tablet coordinates mapped to PC screen coordinates
* 📱 Landscape tablet interface
* ▫️ Dedicated tracking boundary
* 🪶 Lightweight Python Windows receiver

---

# ⚙️ How It Works

```text
             ANDROID TABLET
          ┌───────────────────┐
          │                   │
          │    S Pen / Pen    │
          │         ↓         │
          │   Air-Pen App     │
          │                   │
          └─────────┬─────────┘
                    │
                  Wi-Fi
                    │
               WebSocket
                    │
                    ▼
          ┌───────────────────┐
          │  Windows Receiver │
          │     Python        │
          └─────────┬─────────┘
                    │
                    ▼
             Windows Mouse
```

The Android app converts the pen position into normalized coordinates between `0.0` and `1.0`.

The Windows receiver then converts those coordinates into the actual Windows display resolution.

---

# 📐 Tracking Area

The tablet uses a dedicated tracking area.

```text
┌──────────────────────────────────────────────┐
│                                              │
│    ┌────────────────────────────────────┐    │
│    │                                    │    │
│    │                                    │    │
│    │          TRACKING AREA             │    │
│    │                                    │    │
│    │                                    │    │
│    └────────────────────────────────────┘    │
│                                              │
└──────────────────────────────────────────────┘
```

The tracking area is mapped to the complete Windows display.

```text
Tablet                          Windows PC

Top-left     ───────────────►   Top-left

Top-right    ───────────────►   Top-right

Bottom-left  ───────────────►   Bottom-left

Bottom-right ───────────────►   Bottom-right
```

This means moving the stylus across the tablet tracking area moves the cursor across the corresponding area of the PC screen.

---

# 🎮 Controls

| Tablet Input | Windows Result |
| ------------ | -------------- |
| Pen hover    | Move cursor    |
| Pen touch    | Left click     |
| Hold + move  | Drag           |
| Pen release  | Release click  |

---

# 📡 Network Requirements

The Android tablet and Windows PC must be connected to the **same local Wi-Fi network**.

Find the Windows PC's IPv4 address:

```powershell
ipconfig
```

Example:

```text
IPv4 Address . . . . . . . . . : 192.168.1.13
```

The Android app uses the PC's local IP address to establish the WebSocket connection.

---

# 📦 Requirements

### Android

* Android tablet
* Compatible stylus
* Android stylus input support
* Wi-Fi

### Windows

* Windows 10 / 11
* Python 3
* Wi-Fi
* `websockets`
* `pynput`

---

# ⚠️ V1 Limitations

Air-Pen V1 is a functional first version, not a replacement for a dedicated graphics tablet yet.

Current limitations include:

* Wireless latency can still be noticeable.
* Cursor movement is not perfectly smooth.
* Stylus hover behavior depends on the Android device.
* V1 focuses on mouse-style control.
* No pressure-sensitive drawing support yet.
* No multi-monitor support yet.
* No advanced calibration system yet.

---

# 🧠 V1 Architecture

```text
Stylus
  │
  ▼
MotionEvent
  │
  ▼
Normalized Coordinates
  │
  ▼
WebSocket
  │
  ▼
Python Receiver
  │
  ▼
Windows Mouse API
  │
  ▼
Cursor
```

---

# 🚀 Future Versions

Air-Pen V1 establishes the basic wireless input system.

Future versions may explore:

* Lower latency
* Smoother cursor movement
* Higher update rates
* Pressure sensitivity
* Pen buttons
* Multi-monitor support
* Calibration
* Drawing-tablet mode
* Better stylus compatibility
* Connection recovery
* Custom controls

---

## Credits & Acknowledgements

This project was developed with assistance from several AI tools:

* **ChatGPT** — debugging, architecture discussions, documentation, and development assistance.
* **Claude** — code review, problem solving, and development assistance.
* **Gemini** — AI experimentation and development assistance.

The overall project design, implementation, testing, decisions, and direction are my own.

Thanks to these tools for helping me learn, experiment, and build Air-Pen. 🐺

---

# ❤️ Support the Project

**UPI ID:** `9988743742@fam`

