# Mp3Quran Tarateel — GitHub APK Builder

This repository is prepared so GitHub Actions builds the Android APK for you.

## For a non-technical user

1. Create/sign in to a GitHub account.
2. Create a new repository, for example `mp3quran-tarateel-radio`.
3. Upload all files and folders from this project to that repository.
4. Open the **Actions** tab.
5. Select **Build Android APK**.
6. Click **Run workflow**.
7. When the workflow finishes successfully, open the completed run.
8. Download the artifact named **Mp3Quran-Tarateel-APK**.
9. Extract the downloaded ZIP and install the `.apk` on Android.

No Ubuntu or local Android SDK is needed. GitHub Actions performs the Android build.

The workflow is also triggered automatically whenever code is pushed to the `main` branch.

## App

Name: Mp3Quran Tarateel

Stream:
https://qurango.net/radio/tarateel

Features:
- Foreground media service
- Background playback
- Lock-screen/media notification controls
- Play / Pause / Stop
- Audio focus
- Android 13+ notification permission
