# Android: Auidio and C++ wrapping

Those notes are mainly about getting something done with CLAM and Android.

## What can be done

### Capture audio from mic

- AudioRecord (Java/kotlin) <https://developer.android.com/reference/android/media/AudioRecord>
- Oboe (C++, lower latency) <https://github.com/google/oboe>

The only unrestricted input source in Android

### Capture audio from other app

`Audio Playback Capture` Android 10 / API 29+

- The other app must opt-in
- User must grant permission
- DRM audio is blocked


- `AudioPlaybackCaptureConfiguration`
- `AudioRecord` with an special mod

```kotlin
val config = AudioPlaybackCaptureConfiguration.Builder(mediaProjection)
    .addMatchingUsage(AudioAttributes.USAGE_MEDIA)
    .build()
```

With Oboe:

https://www.youtube.com/watch?v=csfHAbr5ilI&list=PLWz5rJ2EKKc_duWv9IPNvx9YBudNMmLSa






