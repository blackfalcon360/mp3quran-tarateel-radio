[app]
title = Mp3Quran Tarateel
package.name = mp3quranradio
package.domain = org.mp3quran
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,java,xml
version = 2.0
requirements = python3,kivy,pyjnius
orientation = portrait
fullscreen = 0

# Android
android.api = 35
android.minapi = 23
android.ndk = 27c
android.archs = arm64-v8a, armeabi-v7a
android.permissions = INTERNET,FOREGROUND_SERVICE,FOREGROUND_SERVICE_MEDIA_PLAYBACK,WAKE_LOCK,POST_NOTIFICATIONS
android.add_src = src/main/java
android.add_manifest = AndroidManifest.xml

# MediaSession dependencies
android.gradle_dependencies = androidx.media:media:1.7.0,androidx.core:core:1.13.1
android.enable_androidx = True
android.accept_sdk_license = True

[buildozer]
log_level = 2
warn_on_root = 1
