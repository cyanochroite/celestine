/* eslint-disable complexity */
/* eslint-disable func-names */
/* eslint-disable init-declarations */
/* eslint-disable max-len */
/* eslint-disable max-statements */
/* eslint-disable no-shadow */
/* eslint-disable no-unused-vars */
/* eslint-disable one-var */
export namespace EventType {
    export enum AnimationEvent {
        animationcancel = "animationcancel",
        animationend = "animationend",
        animationiteration = "animationiteration",
        animationstart = "animationstart",
    }
    export enum BeforeUnloadEvent {
        beforeunload = "beforeunload",
    }
    export enum ClipboardEvent {
        copy = "copy",
        cut = "cut",
        paste = "paste",
    }
    export enum CompositionEvent {
        compositionend = "compositionend",
        compositionstart = "compositionstart",
        compositionupdate = "compositionupdate",
    }
    export enum DeviceMotionEvent {
        devicemotion = "devicemotion",
    }
    export enum DeviceOrientationEvent {
        deviceorientation = "deviceorientation",
    }
    export enum DragEvent {
        drag = "drag",
        dragend = "dragend",
        dragenter = "dragenter",
        dragleave = "dragleave",
        dragover = "dragover",
        dragstart = "dragstart",
        drop = "drop",
    }
    export enum Event {
        abort = "abort",
        afterprint = "afterprint",
        appinstalled = "appinstalled",
        audioend = "audioend",
        audiostart = "audiostart",
        beforeprint = "beforeprint",
        canplay = "canplay",
        canplaythrough = "canplaythrough",
        change = "change",
        chargingchange = "chargingchange",
        chargingtimechange = "chargingtimechange",
        close = "close",
        devicechange = "devicechange",
        dischargingtimechange = "dischargingtimechange",
        DOMContentLoaded = "DOMContentLoaded",
        durationchange = "durationchange",
        emptied = "emptied",
        end = "end",
        ended = "ended",
        error = "error",
        fullscreenchange = "fullscreenchange",
        fullscreenerror = "fullscreenerror",
        input = "input",
        invalid = "invalid",
        languagechange = "languagechange",
        levelchange = "levelchange",
        loadeddata = "loadeddata",
        loadedmetadata = "loadedmetadata",
        offline = "offline",
        online = "online",
        open = "open",
        orientationchange = "orientationchange",
        pause = "pause",
        play = "play",
        playing = "playing",
        pointerlockchange = "pointerlockchange",
        pointerlockerror = "pointerlockerror",
        ratechange = "ratechange",
        readystatechange = "readystatechange",
        reset = "reset",
        seeked = "seeked",
        seeking = "seeking",
        selectionchange = "selectionchange",
        selectstart = "selectstart",
        slotchange = "slotchange",
        soundend = "soundend",
        soundstart = "soundstart",
        speechend = "speechend",
        speechstart = "speechstart",
        stalled = "stalled",
        start = "start",
        submit = "submit",
        success = "success",
        suspend = "suspend",
        timeupdate = "timeupdate",
        upgradeneeded = "upgradeneeded",
        visibilitychange = "visibilitychange",
        voiceschanged = "voiceschanged",
        volumechange = "volumechange",
        waiting = "waiting",
        complete = "complete",
        versionchange = "versionchange",
    }
    export enum ExtendableMessageEvent {
        message = "message",
    }
    export enum FocusEvent {
        blur = "blur",
        focus = "focus",
        focusin = "focusin",
        focusout = "focusout",
    }
    export enum GamepadEvent {
        gamepadconnected = "gamepadconnected",
        gamepaddisconnected = "gamepaddisconnected",
    }
    export enum HashChangeEvent {
        hashchange = "hashchange",
    }
    export enum IDBVersionChangeEvent {
        blocked = "blocked",
    }
    export enum KeyboardEvent {
        keydown = "keydown",
        keypress = "keypress",
        keyup = "keyup",
    }
    export enum MessageEvent {
        message = "message",
        messageerror = "messageerror",
    }
    export enum MouseEvent {
        click = "click",
        contextmenu = "contextmenu",
        dblclick = "dblclick",
        mousedown = "mousedown",
        mouseenter = "mouseenter",
        mouseleave = "mouseleave",
        mousemove = "mousemove",
        mouseout = "mouseout",
        mouseover = "mouseover",
        mouseup = "mouseup",
        show = "show",
    }
    export enum NotificationEvent {
        notificationclick = "notificationclick",
    }
    export enum PageTransitionEvent {
        pagehide = "pagehide",
        pageshow = "pageshow",
    }
    export enum Performance {
        resourcetimingbufferfull = "resourcetimingbufferfull",
    }
    export enum PointerEvent {
        gotpointercapture = "gotpointercapture",
        lostpointercapture = "lostpointercapture",
        pointercancel = "pointercancel",
        pointerdown = "pointerdown",
        pointerenter = "pointerenter",
        pointerleave = "pointerleave",
        pointermove = "pointermove",
        pointerout = "pointerout",
        pointerover = "pointerover",
        pointerup = "pointerup",
    }
    export enum PopStateEvent {
        popstate = "popstate",
    }
    export enum ProgressEvent {
        abort = "abort",
        error = "error",
        load = "load",
        loadend = "loadend",
        loadstart = "loadstart",
        progress = "progress",
        timeout = "timeout",
    }
    export enum PushEvent {
        push = "push",
        pushsubscriptionchange = "pushsubscriptionchange",
    }
    export enum ServiceWorkerMessageEvent {
        message = "message",
    }
    export enum SpeechRecognitionEvent {
        nomatch = "nomatch",
        result = "result",
    }
    export enum SpeechSynthesisErrorEvent {
        error = "error",
    }
    export enum SpeechSynthesisEvent {
        boundary = "boundary",
        end = "end",
        mark = "mark",
        pause = "pause",
        resume = "resume",
        start = "start",
    }
    export enum StorageEvent {
        storage = "storage",
    }
    export enum SVGEvent {
        SVGAbort = "SVGAbort",
        SVGError = "SVGError",
        SVGLoad = "SVGLoad",
        SVGResize = "SVGResize",
        SVGScroll = "SVGScroll",
        SVGUnload = "SVGUnload",
    }
    export enum SVGZoomEvent {
        SVGZoom = "SVGZoom",
    }
    export enum TimeEvent {
        beginEvent = "beginEvent",
        endEvent = "endEvent",
        repeatEvent = "repeatEvent",
    }
    export enum TouchEvent {
        touchcancel = "touchcancel",
        touchend = "touchend",
        touchmove = "touchmove",
        touchstart = "touchstart",
    }
    export enum TransitionEvent {
        transitionend = "transitionend",
    }
    export enum UIEvent {
        abort = "abort",
        error = "error",
        load = "load",
        resize = "resize",
        scroll = "scroll",
        select = "select",
        unload = "unload",
    }
    export enum UserProximityEvent {
        userproximity = "userproximity",
    }
    export enum WheelEvent {
        wheel = "wheel",
    }
}
