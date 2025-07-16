[app]
# App-Grunddaten
title = FlohmarktMVP
package.name = flohmarktmvp
package.domain = org.example
version = 0.1

# Quellcode-Verzeichnis und Dateitypen
source.dir = .
source.include_exts = py,kv

# App-Anforderungen (Recipes & Libs)
requirements = kivy, requests, plyer, numpy

# Python-Files-Freigabe
android.permissions = CAMERA, INTERNET, WRITE_EXTERNAL_STORAGE, POST_NOTIFICATIONS

# Layout & Themes
orientation = portrait
fullscreen = 0

# Buildozer-Version und API Levels
[buildozer]
log_level = 2
warn_on_root = 1
# p4a.branch = stable
android.api = 33
android.ndk = 25b
android.arch = armeabi-v7a, arm64-v8a

