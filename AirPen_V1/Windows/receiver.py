import asyncio
import ctypes
import json

import websockets
# USE:- pip install websockets pynput

user32 = ctypes.windll.user32

PORT = 8765

mouse_down = False

SCREEN_WIDTH = user32.GetSystemMetrics(0)
SCREEN_HEIGHT = user32.GetSystemMetrics(1)

LEFT_DOWN = 0x0002
LEFT_UP = 0x0004




# 0.0 = left/top edge
# 1.0 = right/bottom edge

TABLET_LEFT = 0.0
TABLET_RIGHT = 1.0
TABLET_TOP = 0.0
TABLET_BOTTOM = 1.0


def clamp(value, minimum, maximum):
    return max(minimum, min(value, maximum))


def tablet_to_screen(x, y):
    # Map tablet coordinates to the calibrated area
    mapped_x = (x - TABLET_LEFT) / (TABLET_RIGHT - TABLET_LEFT)
    mapped_y = (y - TABLET_TOP) / (TABLET_BOTTOM - TABLET_TOP)

    # Keep cursor inside screen
    mapped_x = clamp(mapped_x, 0.0, 1.0)
    mapped_y = clamp(mapped_y, 0.0, 1.0)

    # Convert to Windows pixels
    screen_x = int(mapped_x * (SCREEN_WIDTH - 1))
    screen_y = int(mapped_y * (SCREEN_HEIGHT - 1))

    return screen_x, screen_y


# MOUSE FUNCTIONS

def move_mouse(x, y):
    user32.SetCursorPos(x, y)


def left_down():
    user32.mouse_event(LEFT_DOWN, 0, 0, 0, 0)


def left_up():
    user32.mouse_event(LEFT_UP, 0, 0, 0, 0)


# WEBSOCKET

async def handle_client(websocket):
    global mouse_down

    print("Tablet connected!")

    try:
        async for message in websocket:

            data = json.loads(message)

            event_type = data.get("type")

            x = float(data.get("x", 0.0))
            y = float(data.get("y", 0.0))

            # Convert tablet coordinates to Windows coordinates
            screen_x, screen_y = tablet_to_screen(x, y)

            # Move cursor
            if event_type in ("hover", "down", "move", "up"):
                move_mouse(screen_x, screen_y)

            # Pen touches tablet
            if event_type == "down":

                if not mouse_down:
                    left_down()
                    mouse_down = True

            # Pen lifted
            elif event_type == "up":

                if mouse_down:
                    left_up()
                    mouse_down = False

    except websockets.exceptions.ConnectionClosed:
        print("Tablet disconnected.")

    except Exception as e:
        print(f"Error: {e}")

    finally:

        # Safety release
        if mouse_down:
            left_up()
            mouse_down = False


# SERVER

async def main():

    print("TabletMouse Windows Receiver")
    print(f"Screen: {SCREEN_WIDTH} x {SCREEN_HEIGHT}")

    print(
        "Tablet mapping: "
        f"L={TABLET_LEFT} "
        f"R={TABLET_RIGHT} "
        f"T={TABLET_TOP} "
        f"B={TABLET_BOTTOM}"
    )

    print(f"Listening on port {PORT}...")
    print("Waiting for tablet...")

    async with websockets.serve(
        handle_client,
        "0.0.0.0",
        PORT
    ):
        await asyncio.Future()


if __name__ == "__main__":
    asyncio.run(main())