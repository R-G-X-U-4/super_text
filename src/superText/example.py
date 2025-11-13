import ctypes
from ctypes import wintypes

user32 = ctypes.WinDLL('user32', use_last_error=True)

# Define Windows types
LRESULT = wintypes.LPARAM
WNDPROC = ctypes.WINFUNCTYPE(LRESULT, wintypes.HWND, wintypes.UINT, wintypes.WPARAM, wintypes.LPARAM)

# Define the WNDCLASS structure
class WNDCLASS(ctypes.Structure):
    _fields_ = [
        ('style', wintypes.UINT),
        ('lpfnWndProc', WNDPROC),
        ('cbClsExtra', ctypes.c_int),
        ('cbWndExtra', ctypes.c_int),
        ('hInstance', wintypes.HINSTANCE),
        ('hIcon', wintypes.HICON),
        ('hCursor', wintypes.HCURSOR),
        ('hbrBackground', wintypes.HBRUSH),
        ('lpszMenuName', wintypes.LPCWSTR),
        ('lpszClassName', wintypes.LPCWSTR),
    ]

# Define the MSG structure
class MSG(ctypes.Structure):
    _fields_ = [
        ('hwnd', wintypes.HWND),
        ('message', wintypes.UINT),
        ('wParam', wintypes.WPARAM),
        ('lParam', wintypes.LPARAM),
        ('time', wintypes.DWORD),
        ('pt', wintypes.POINT),
    ]

# Window procedure
def wnd_proc(hwnd, msg, wparam, lparam):
    if msg == 2:  # WM_DESTROY
        user32.PostQuitMessage(0)
        return 0
    return user32.DefWindowProcW(hwnd, msg, wparam, lparam)

# Create a window
hInstance = wintypes.HINSTANCE(ctypes.windll.kernel32.GetModuleHandleW(None))
wc = WNDCLASS()
wc.lpfnWndProc = WNDPROC(wnd_proc)
wc.lpszClassName = "MyPythonWindow"
wc.hInstance = hInstance

user32.RegisterClassW(ctypes.byref(wc))

hwnd = user32.CreateWindowExW(
    0, wc.lpszClassName, "Hello from Python",
    0xcf0000, 100, 100, 500, 300,
    None, None, hInstance, None
)
user32.ShowWindow(hwnd, 1)

msg = MSG()
while user32.GetMessageW(ctypes.byref(msg), None, 0, 0) != 0:
    user32.TranslateMessage(ctypes.byref(msg))
    user32.DispatchMessageW(ctypes.byref(msg))
