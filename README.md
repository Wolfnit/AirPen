# 🐺 Air-Pen — Wireless Android Pen Tablet

> An evolving Android-to-Windows input project that turns an Android tablet and compatible stylus into a wireless PC control surface.

Air-Pen is my experiment in turning an existing Android tablet into a **wireless pen tablet for Windows**.

The project uses the tablet's stylus input, sends the pen position over a local Wi-Fi connection, and converts it into Windows mouse input.

The goal is to create a lightweight alternative to a dedicated graphics tablet while keeping the system simple, responsive, and expandable.

---

# 📚 Versions & Guides

Each version of Air-Pen represents a different stage of development.

## 🟢 01 — Air-Pen: Wireless Pen Mouse

The first working version of Air-Pen.

An Android application captures stylus hover, touch, movement, and release events and sends them to a Python-based Windows receiver over WebSocket.

The Windows receiver converts the normalized tablet coordinates into actual Windows screen coordinates and controls the mouse.

### Current Features

* Stylus hover → cursor movement
* Stylus touch → left click
* Hold + move → drag
* Stylus release → mouse release
* Wireless communication over Wi-Fi
* Automatic Windows screen resolution detection
* Automatic tablet tracking-area calculation
* Landscape interface
* Visible tracking boundary
* Python Windows receiver

📁 `AirPen_V1/`

---

# 🚀 Project Vision

The long-term goal of Air-Pen is to turn an Android tablet into a **versatile wireless PC input device**.

The idea is:

```text
                 ┌─────────────────┐
                 │ ANDROID TABLET  │
                 │                 │
                 │  Stylus Input   │
                 └────────┬────────┘
                          │
                       Wi-Fi
                          │
                          ▼
                 ┌─────────────────┐
                 │    AIR-PEN      │
                 │                 │
                 │  Capture        │
                 │  Normalize      │
                 │  Transmit       │
                 └────────┬────────┘
                          │
                       WebSocket
                          │
                          ▼
                 ┌─────────────────┐
                 │ WINDOWS RECEIVER│
                 │                 │
                 │  Receive        │
                 │  Map            │
                 │  Execute        │
                 └────────┬────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │ WINDOWS PC      │
                 │                 │
                 │ Mouse / Input   │
                 └─────────────────┘
```

The eventual goal is to go beyond basic mouse control and make the tablet behave more like a dedicated graphics tablet.

---

# 🛠️ Planned Features

Future development may include:

* Improved cursor smoothness
* Lower input latency
* Higher event/update rate
* Better stylus compatibility
* Pressure sensitivity
* Pen button support
* Multi-monitor support
* Customizable controls
* Drawing-tablet mode
* Calibration tools
* Connection recovery
* Additional PC input controls

---

# 💻 Technology

### Android

* Kotlin
* Jetpack Compose
* Android Stylus / MotionEvent APIs
* OkHttp WebSocket

### Windows

* Python
* WebSockets
* pynput
* Windows mouse API

---

# 📡 How It Works

Air-Pen connects the Android tablet and Windows PC over the same local Wi-Fi network.

The Android application converts the stylus position into normalized coordinates:

```text
0.0 ─────────────────────── 1.0
 │                          │
 │       TRACKING AREA     │
 │                          │
0.0 ─────────────────────── 1.0
```

The Windows receiver then maps those coordinates to the actual PC display resolution.

This allows the tracking area to automatically correspond to the full Windows screen.

---

# ⚠️ Current Limitations

Air-Pen is currently an early-stage project.

* Wireless input can still have noticeable latency.
* Cursor movement is not yet as smooth as a dedicated graphics tablet.
* Stylus hover support depends on the Android device.
* The current Windows receiver primarily provides mouse-style input.
* Calibration and advanced tablet features are still being developed.

---

# 🤝 Development

Air-Pen is an ongoing personal project.

The focus is on experimenting with Android stylus APIs, wireless communication, low-latency input, and computer control while keeping the implementation lightweight.

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

If you find Air-Pen interesting or useful and would like to support its development, you can optionally support the project through UPI.

**UPI ID:** `9988743742@fam`

Any support helps me continue developing Air-Pen and experimenting with Android-to-PC tools.
