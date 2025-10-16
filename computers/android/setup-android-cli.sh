#!/usr/bin/env bash
set -e

#sudo apt install \
#    openjdk-11-jdk \
#    gradle \
#    google-android-build-tools-34.0.0-installer \
#    google-android-platform-tools-installer \
#    google-android-cmdline-tools-17.0-installer \
#    google-android-platform-34-installer \
#    google-android-emulator-installer
#sudo sdkmanager "system-images;android-34;google_apis;x86_64"
#avdmanager create avd -n myimage -k "system-images;android-34;google_apis;x86_64"
#emulator -avd myimage

# === Utility: format steps and commands ===

step() {
  local BLUE="\033[1;34m"
  local RESET="\033[0m"
  echo -e "\n${BLUE}==> $1${RESET}"
}

run() {
  local CYAN="\033[1;36m"
  local RESET="\033[0m"
  echo -e "${CYAN}$ $*${RESET}"
  "$@"
}

# Leave these empty to auto-detect the latest available versions
BUILD_TOOLS_VERSION=""     # e.g. "34.0.0"
PLATFORM_API_VERSION=""    # e.g. "34"
SDK_ROOT_DIR="${XDG_DATA_HOME:-$HOME/.local/share}/android-sdk"
TOOLSDIR="$SDK_ROOT_DIR/cmdline-tools/latest"
BASHRC="$HOME/.bashrc"

step "Installing required system packages"
run sudo apt update
run sudo apt install -y openjdk-17-jdk unzip wget android-tools-adb android-tools-fastboot

step "Downloading Android command-line tools (latest)"
TOOLS_ZIP="commandlinetools-linux.zip"
run wget -q https://dl.google.com/android/repository/commandlinetools-linux-latest.zip -O "$TOOLS_ZIP"

run mkdir -p "$TOOLSDIR"
run unzip -q "$TOOLS_ZIP" -d "$SDK_ROOT_DIR/cmdline-tools"
run mv "$SDK_ROOT_DIR/cmdline-tools/cmdline-tools/"* "$TOOLSDIR/"
run rm "$TOOLS_ZIP"

step "Setting environment variables (current session)"
export ANDROID_SDK_ROOT="$SDK_ROOT_DIR"
export PATH="$TOOLSDIR/bin:$ANDROID_SDK_ROOT/platform-tools:$PATH"

step "Persisting environment variables to $BASHRC"
if ! grep -q 'ANDROID_SDK_ROOT' "$BASHRC"; then
  cat >> "$BASHRC" <<EOF

# >>> Android SDK environment variables >>>
export ANDROID_SDK_ROOT="$ANDROID_SDK_ROOT"
export PATH="\$ANDROID_SDK_ROOT/cmdline-tools/latest/bin:\$ANDROID_SDK_ROOT/platform-tools:\$PATH"
# <<< Android SDK environment variables <<<
EOF
  echo "✅ Environment variables added to $BASHRC"
else
  echo "ℹ️ Environment variables already present in $BASHRC"
fi

step "Resolving SDK versions"
PKG_LIST=$(sdkmanager --list --channel=0)

if [ -z "$BUILD_TOOLS_VERSION" ]; then
  BUILD_TOOLS_VERSION=$(echo "$PKG_LIST" | grep -oP 'build-tools;[0-9]+\.[0-9]+\.[0-9]+' | grep -v rc | sort -V | tail -1 | cut -d';' -f2)
  echo "✅ Using latest build-tools: $BUILD_TOOLS_VERSION"
else
  echo "✅ Using configured build-tools: $BUILD_TOOLS_VERSION"
fi

if [ -z "$PLATFORM_API_VERSION" ]; then
  PLATFORM_API_VERSION=$(echo "$PKG_LIST" | grep -oP 'platforms;android-[0-9]+' | grep -v rc | sort -t- -k2 -n | tail -1 | cut -d'-' -f2)
  echo "✅ Using latest platform API: android-$PLATFORM_API_VERSION"
else
  echo "✅ Using configured platform API: android-$PLATFORM_API_VERSION"
fi

step "Installing SDK components"
yes | run sdkmanager --sdk_root="$ANDROID_SDK_ROOT" --install \
  "platform-tools" \
  "build-tools;$BUILD_TOOLS_VERSION" \
  "platforms;android-$PLATFORM_API_VERSION"

step "Accepting licenses"
yes | run sdkmanager --sdk_root="$ANDROID_SDK_ROOT" --licenses

step "Android SDK CLI setup complete"

echo ""
echo "✅ SDK installed at: $ANDROID_SDK_ROOT"
echo ""
echo "🔧 To start using it now, run:"
echo "   source \"$BASHRC\""
echo ""
echo "🧹 To uninstall later, run:"
echo "   sudo apt remove --purge openjdk-17-jdk android-tools-adb android-tools-fastboot"
echo "   rm -rf \"$ANDROID_SDK_ROOT\""
echo "   sed -i '/ANDROID_SDK_ROOT/d' \"$BASHRC\""

