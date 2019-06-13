export const EventType = Object.freeze({
    "AnimationEvent": {
        "animationcancel": 0x00,
        "animationend": 0x01,
        "animationiteration": 0x02,
        "animationstart": 0x03
    },
    "AudioProcessingEvent": {
        "audioprocess": 0x00
    },
    "BeforeUnloadEvent": {
        "beforeunload": 0x00
    },
    "ClipboardEvent": {
        "copy": 0x00,
        "cut": 0x01,
        "paste": 0x02
    },
    "CompositionEvent": {
        "compositionend": 0x00,
        "compositionstart": 0x01,
        "compositionupdate": 0x02
    },
    "DeviceMotionEvent": {
        "devicemotion": 0x00
    },
    "DeviceOrientationEvent": {
        "deviceorientation": 0x00
    },
    "DragEvent": {
        "drag": 0x00,
        "dragend": 0x01,
        "dragenter": 0x02,
        "dragleave": 0x03,
        "dragover": 0x04,
        "dragstart": 0x05,
        "drop": 0x06
    },
    "Event": {
        "DOMContentLoaded": 0x00,
        "abort": 0x01,
        "afterprint": 0x02,
        "appinstalled": 0x03,
        "audioend": 0x04,
        "audiostart": 0x05,
        "beforeprint": 0x06,
        "blocked": 0x07,
        "canplay": 0x08,
        "canplaythrough": 0x09,
        "change": 0x0A,
        "chargingchange": 0x0B,
        "chargingtimechange": 0x0C,
        "close": 0x0D,
        "complete": 0x0E,
        "devicechange": 0x0F,
        "dischargingtimechange": 0x10,
        "durationchange": 0x11,
        "emptied": 0x12,
        "end": 0x13,
        "ended": 0x14,
        "error": 0x15,
        "fullscreenchange": 0x16,
        "fullscreenerror": 0x17,
        "input": 0x18,
        "invalid": 0x19,
        "languagechange": 0x1A,
        "levelchange": 0x1B,
        "loadeddata": 0x1C,
        "loadedmetadata": 0x1D,
        "offline": 0x1E,
        "online": 0x1F,
        "open": 0x20,
        "orientationchange": 0x21,
        "pause": 0x22,
        "play": 0x23,
        "playing": 0x24,
        "pointerlockchange": 0x25,
        "pointerlockerror": 0x26,
        "ratechange": 0x27,
        "readystatechange": 0x28,
        "reset": 0x29,
        "seeked": 0x2A,
        "seeking": 0x2B,
        "selectionchange": 0x2C,
        "selectstart": 0x2D,
        "slotchange": 0x2E,
        "soundend": 0x2F,
        "soundstart": 0x30,
        "speechend": 0x31,
        "speechstart": 0x32,
        "stalled": 0x33,
        "start": 0x34,
        "submit": 0x35,
        "success": 0x36,
        "suspend": 0x37,
        "timeupdate": 0x38,
        "upgradeneeded": 0x39,
        "versionchange": 0x3A,
        "visibilitychange": 0x3B,
        "voiceschanged": 0x3C,
        "volumechange": 0x3D,
        "waiting": 0x3E
    },
    "ExtendableMessageEvent": {
        "message": 0x00
    },
    "FocusEvent": {
        "blur": 0x00,
        "focus": 0x01,
        "focusin": 0x02,
        "focusout": 0x03
    },
    "GamepadEvent": {
        "gamepadconnected": 0x00,
        "gamepaddisconnected": 0x01
    },
    "HashChangeEvent": {
        "hashchange": 0x00
    },
    "KeyboardEvent": {
        "keydown": 0x00,
        "keypress": 0x01,
        "keyup": 0x02,
        "message": 0x03
    },
    "MessageEvent": {
        "messageerror": 0x00
    },
    "MouseEvent": {
        "click": 0x00,
        "contextmenu": 0x01,
        "dblclick": 0x02,
        "mousedown": 0x03,
        "mouseenter": 0x04,
        "mouseleave": 0x05,
        "mousemove": 0x06,
        "mouseout": 0x07,
        "mouseover": 0x08,
        "mouseup": 0x09,
        "show": 0x0A
    },
    "NotificationEvent": {
        "notificationclick": 0x00
    },
    "OfflineAudioCompletionEvent": {
        "complete": 0x00
    },
    "PageTransitionEvent": {
        "pagehide": 0x00,
        "pageshow": 0x01
    },
    "Performance": {
        "resourcetimingbufferfull": 0x00
    },
    "PointerEvent": {
        "gotpointercapture": 0x00,
        "lostpointercapture": 0x01,
        "pointercancel": 0x02,
        "pointerdown": 0x03,
        "pointerenter": 0x04,
        "pointerleave": 0x05,
        "pointermove": 0x06,
        "pointerout": 0x07,
        "pointerover": 0x08,
        "pointerup": 0x09
    },
    "PopStateEvent": {
        "popstate": 0x00
    },
    "ProgressEvent": {
        "abort": 0x00,
        "error": 0x01,
        "load": 0x02,
        "loadend": 0x03,
        "loadstart": 0x04,
        "progress": 0x05,
        "timeout": 0x06
    },
    "PushEvent": {
        "push": 0x00,
        "pushsubscriptionchange": 0x01
    },
    "SVGEvent": {
        "SVGAbort": 0x00,
        "SVGError": 0x01,
        "SVGLoad": 0x02,
        "SVGResize": 0x03,
        "SVGScroll": 0x04,
        "SVGUnload": 0x05
    },
    "SVGZoomEvent": {
        "SVGZoom": 0x00
    },
    "ServiceWorkerMessageEvent": {
        "message": 0x00
    },
    "SpeechRecognitionEvent": {
        "nomatch": 0x00,
        "result": 0x01
    },
    "SpeechSynthesisErrorEvent": {
        "boundary": 0x00,
        "end": 0x01,
        "error": 0x02,
        "mark": 0x03,
        "pause": 0x04,
        "resume": 0x05,
        "start": 0x06
    },
    "StorageEvent": {
        "storage": 0x00
    },
    "TimeEvent": {
        "beginEvent": 0x00,
        "endEvent": 0x01,
        "repeatEvent": 0x02
    },
    "TouchEvent": {
        "touchcancel": 0x00,
        "touchend": 0x01,
        "touchmove": 0x02,
        "touchstart": 0x03
    },
    "TransitionEvent": {
        "transitionend": 0x00
    },
    "UIEvent": {
        "abort": 0x00,
        "error": 0x01,
        "load": 0x02,
        "resize": 0x03,
        "scroll": 0x04,
        "select": 0x05,
        "unload": 0x06
    },
    "UserProximityEvent": {
        "userproximity": 0x00
    },
    "WheelEvent": {
        "wheel": 0x00
    }
});
