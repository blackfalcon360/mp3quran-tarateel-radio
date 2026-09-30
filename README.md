# Mp3Quran Tarateel — Android Python Radio v2

This project uses Kivy/Python for the UI and a native Android Foreground Service
with MediaSession for reliable background playback.

Stream:
https://qurango.net/radio/tarateel

Features:
- Play / Pause / Stop
- Foreground service
- Screen-off / lock-screen playback
- Android media notification
- Lock-screen/media-session controls
- Audio focus
- Android 13+ notification permission support

## Build

Recommended: Ubuntu 22.04/24.04 or WSL2.

```bash
sudo apt update
sudo apt install -y git zip unzip openjdk-17-jdk python3-pip
python3 -m pip install --upgrade pip
python3 -m pip install buildozer cython
buildozer android debug
```

APK will be under `bin/`.

## Important

The first build downloads Android SDK/NDK/Gradle components and can take
a significant amount of time.

On Android 13+, allow notifications when prompted. Android may also have
battery-optimization settings that can stop long-running apps on some phones;
if playback stops after a long idle period, set this app's battery usage to
"Unrestricted" in Android settings.

The stream URL is defined in `main.py` as `STREAM_URL`. Replace it if the
station changes its stream endpoint.

## If build fails

Use Java 17 and a clean build:

```bash
buildozer android clean
buildozer -v android debug
```
