
exports.__esModule = true;
/* eslint-disable complexity */
/* eslint-disable func-names */
/* eslint-disable init-declarations */
/* eslint-disable max-len */
/* eslint-disable max-statements */
/* eslint-disable no-shadow */
/* eslint-disable no-unused-vars */
/* eslint-disable one-var */
let EventType;
(function (EventType) {

    let AnimationEvent;
    (function (AnimationEvent) {

        AnimationEvent.animationcancel = "animationcancel";
        AnimationEvent.animationend = "animationend";
        AnimationEvent.animationiteration = "animationiteration";
        AnimationEvent.animationstart = "animationstart";

    }(AnimationEvent = EventType.AnimationEvent || (EventType.AnimationEvent = {})));
    let BeforeUnloadEvent;
    (function (BeforeUnloadEvent) {

        BeforeUnloadEvent.beforeunload = "beforeunload";

    }(BeforeUnloadEvent = EventType.BeforeUnloadEvent || (EventType.BeforeUnloadEvent = {})));
    let ClipboardEvent;
    (function (ClipboardEvent) {

        ClipboardEvent.copy = "copy";
        ClipboardEvent.cut = "cut";
        ClipboardEvent.paste = "paste";

    }(ClipboardEvent = EventType.ClipboardEvent || (EventType.ClipboardEvent = {})));
    let CompositionEvent;
    (function (CompositionEvent) {

        CompositionEvent.compositionend = "compositionend";
        CompositionEvent.compositionstart = "compositionstart";
        CompositionEvent.compositionupdate = "compositionupdate";

    }(CompositionEvent = EventType.CompositionEvent || (EventType.CompositionEvent = {})));
    let DeviceMotionEvent;
    (function (DeviceMotionEvent) {

        DeviceMotionEvent.devicemotion = "devicemotion";

    }(DeviceMotionEvent = EventType.DeviceMotionEvent || (EventType.DeviceMotionEvent = {})));
    let DeviceOrientationEvent;
    (function (DeviceOrientationEvent) {

        DeviceOrientationEvent.deviceorientation = "deviceorientation";

    }(DeviceOrientationEvent = EventType.DeviceOrientationEvent || (EventType.DeviceOrientationEvent = {})));
    let DragEvent;
    (function (DragEvent) {

        DragEvent.drag = "drag";
        DragEvent.dragend = "dragend";
        DragEvent.dragenter = "dragenter";
        DragEvent.dragleave = "dragleave";
        DragEvent.dragover = "dragover";
        DragEvent.dragstart = "dragstart";
        DragEvent.drop = "drop";

    }(DragEvent = EventType.DragEvent || (EventType.DragEvent = {})));
    let Event;
    (function (Event) {

        Event.abort = "abort";
        Event.afterprint = "afterprint";
        Event.appinstalled = "appinstalled";
        Event.audioend = "audioend";
        Event.audiostart = "audiostart";
        Event.beforeprint = "beforeprint";
        Event.canplay = "canplay";
        Event.canplaythrough = "canplaythrough";
        Event.change = "change";
        Event.chargingchange = "chargingchange";
        Event.chargingtimechange = "chargingtimechange";
        Event.close = "close";
        Event.devicechange = "devicechange";
        Event.dischargingtimechange = "dischargingtimechange";
        Event.DOMContentLoaded = "DOMContentLoaded";
        Event.durationchange = "durationchange";
        Event.emptied = "emptied";
        Event.end = "end";
        Event.ended = "ended";
        Event.error = "error";
        Event.fullscreenchange = "fullscreenchange";
        Event.fullscreenerror = "fullscreenerror";
        Event.input = "input";
        Event.invalid = "invalid";
        Event.languagechange = "languagechange";
        Event.levelchange = "levelchange";
        Event.loadeddata = "loadeddata";
        Event.loadedmetadata = "loadedmetadata";
        Event.offline = "offline";
        Event.online = "online";
        Event.open = "open";
        Event.orientationchange = "orientationchange";
        Event.pause = "pause";
        Event.play = "play";
        Event.playing = "playing";
        Event.pointerlockchange = "pointerlockchange";
        Event.pointerlockerror = "pointerlockerror";
        Event.ratechange = "ratechange";
        Event.readystatechange = "readystatechange";
        Event.reset = "reset";
        Event.seeked = "seeked";
        Event.seeking = "seeking";
        Event.selectionchange = "selectionchange";
        Event.selectstart = "selectstart";
        Event.slotchange = "slotchange";
        Event.soundend = "soundend";
        Event.soundstart = "soundstart";
        Event.speechend = "speechend";
        Event.speechstart = "speechstart";
        Event.stalled = "stalled";
        Event.start = "start";
        Event.submit = "submit";
        Event.success = "success";
        Event.suspend = "suspend";
        Event.timeupdate = "timeupdate";
        Event.upgradeneeded = "upgradeneeded";
        Event.visibilitychange = "visibilitychange";
        Event.voiceschanged = "voiceschanged";
        Event.volumechange = "volumechange";
        Event.waiting = "waiting";
        Event.complete = "complete";
        Event.versionchange = "versionchange";

    }(Event = EventType.Event || (EventType.Event = {})));
    let ExtendableMessageEvent;
    (function (ExtendableMessageEvent) {

        ExtendableMessageEvent.message = "message";

    }(ExtendableMessageEvent = EventType.ExtendableMessageEvent || (EventType.ExtendableMessageEvent = {})));
    let FocusEvent;
    (function (FocusEvent) {

        FocusEvent.blur = "blur";
        FocusEvent.focus = "focus";
        FocusEvent.focusin = "focusin";
        FocusEvent.focusout = "focusout";

    }(FocusEvent = EventType.FocusEvent || (EventType.FocusEvent = {})));
    let GamepadEvent;
    (function (GamepadEvent) {

        GamepadEvent.gamepadconnected = "gamepadconnected";
        GamepadEvent.gamepaddisconnected = "gamepaddisconnected";

    }(GamepadEvent = EventType.GamepadEvent || (EventType.GamepadEvent = {})));
    let HashChangeEvent;
    (function (HashChangeEvent) {

        HashChangeEvent.hashchange = "hashchange";

    }(HashChangeEvent = EventType.HashChangeEvent || (EventType.HashChangeEvent = {})));
    let IDBVersionChangeEvent;
    (function (IDBVersionChangeEvent) {

        IDBVersionChangeEvent.blocked = "blocked";

    }(IDBVersionChangeEvent = EventType.IDBVersionChangeEvent || (EventType.IDBVersionChangeEvent = {})));
    let KeyboardEvent;
    (function (KeyboardEvent) {

        KeyboardEvent.keydown = "keydown";
        KeyboardEvent.keypress = "keypress";
        KeyboardEvent.keyup = "keyup";

    }(KeyboardEvent = EventType.KeyboardEvent || (EventType.KeyboardEvent = {})));
    let MessageEvent;
    (function (MessageEvent) {

        MessageEvent.message = "message";
        MessageEvent.messageerror = "messageerror";

    }(MessageEvent = EventType.MessageEvent || (EventType.MessageEvent = {})));
    let MouseEvent;
    (function (MouseEvent) {

        MouseEvent.click = "click";
        MouseEvent.contextmenu = "contextmenu";
        MouseEvent.dblclick = "dblclick";
        MouseEvent.mousedown = "mousedown";
        MouseEvent.mouseenter = "mouseenter";
        MouseEvent.mouseleave = "mouseleave";
        MouseEvent.mousemove = "mousemove";
        MouseEvent.mouseout = "mouseout";
        MouseEvent.mouseover = "mouseover";
        MouseEvent.mouseup = "mouseup";
        MouseEvent.show = "show";

    }(MouseEvent = EventType.MouseEvent || (EventType.MouseEvent = {})));
    let NotificationEvent;
    (function (NotificationEvent) {

        NotificationEvent.notificationclick = "notificationclick";

    }(NotificationEvent = EventType.NotificationEvent || (EventType.NotificationEvent = {})));
    let PageTransitionEvent;
    (function (PageTransitionEvent) {

        PageTransitionEvent.pagehide = "pagehide";
        PageTransitionEvent.pageshow = "pageshow";

    }(PageTransitionEvent = EventType.PageTransitionEvent || (EventType.PageTransitionEvent = {})));
    let Performance;
    (function (Performance) {

        Performance.resourcetimingbufferfull = "resourcetimingbufferfull";

    }(Performance = EventType.Performance || (EventType.Performance = {})));
    let PointerEvent;
    (function (PointerEvent) {

        PointerEvent.gotpointercapture = "gotpointercapture";
        PointerEvent.lostpointercapture = "lostpointercapture";
        PointerEvent.pointercancel = "pointercancel";
        PointerEvent.pointerdown = "pointerdown";
        PointerEvent.pointerenter = "pointerenter";
        PointerEvent.pointerleave = "pointerleave";
        PointerEvent.pointermove = "pointermove";
        PointerEvent.pointerout = "pointerout";
        PointerEvent.pointerover = "pointerover";
        PointerEvent.pointerup = "pointerup";

    }(PointerEvent = EventType.PointerEvent || (EventType.PointerEvent = {})));
    let PopStateEvent;
    (function (PopStateEvent) {

        PopStateEvent.popstate = "popstate";

    }(PopStateEvent = EventType.PopStateEvent || (EventType.PopStateEvent = {})));
    let ProgressEvent;
    (function (ProgressEvent) {

        ProgressEvent.abort = "abort";
        ProgressEvent.error = "error";
        ProgressEvent.load = "load";
        ProgressEvent.loadend = "loadend";
        ProgressEvent.loadstart = "loadstart";
        ProgressEvent.progress = "progress";
        ProgressEvent.timeout = "timeout";

    }(ProgressEvent = EventType.ProgressEvent || (EventType.ProgressEvent = {})));
    let PushEvent;
    (function (PushEvent) {

        PushEvent.push = "push";
        PushEvent.pushsubscriptionchange = "pushsubscriptionchange";

    }(PushEvent = EventType.PushEvent || (EventType.PushEvent = {})));
    let ServiceWorkerMessageEvent;
    (function (ServiceWorkerMessageEvent) {

        ServiceWorkerMessageEvent.message = "message";

    }(ServiceWorkerMessageEvent = EventType.ServiceWorkerMessageEvent || (EventType.ServiceWorkerMessageEvent = {})));
    let SpeechRecognitionEvent;
    (function (SpeechRecognitionEvent) {

        SpeechRecognitionEvent.nomatch = "nomatch";
        SpeechRecognitionEvent.result = "result";

    }(SpeechRecognitionEvent = EventType.SpeechRecognitionEvent || (EventType.SpeechRecognitionEvent = {})));
    let SpeechSynthesisErrorEvent;
    (function (SpeechSynthesisErrorEvent) {

        SpeechSynthesisErrorEvent.error = "error";

    }(SpeechSynthesisErrorEvent = EventType.SpeechSynthesisErrorEvent || (EventType.SpeechSynthesisErrorEvent = {})));
    let SpeechSynthesisEvent;
    (function (SpeechSynthesisEvent) {

        SpeechSynthesisEvent.boundary = "boundary";
        SpeechSynthesisEvent.end = "end";
        SpeechSynthesisEvent.mark = "mark";
        SpeechSynthesisEvent.pause = "pause";
        SpeechSynthesisEvent.resume = "resume";
        SpeechSynthesisEvent.start = "start";

    }(SpeechSynthesisEvent = EventType.SpeechSynthesisEvent || (EventType.SpeechSynthesisEvent = {})));
    let StorageEvent;
    (function (StorageEvent) {

        StorageEvent.storage = "storage";

    }(StorageEvent = EventType.StorageEvent || (EventType.StorageEvent = {})));
    let SVGEvent;
    (function (SVGEvent) {

        SVGEvent.SVGAbort = "SVGAbort";
        SVGEvent.SVGError = "SVGError";
        SVGEvent.SVGLoad = "SVGLoad";
        SVGEvent.SVGResize = "SVGResize";
        SVGEvent.SVGScroll = "SVGScroll";
        SVGEvent.SVGUnload = "SVGUnload";

    }(SVGEvent = EventType.SVGEvent || (EventType.SVGEvent = {})));
    let SVGZoomEvent;
    (function (SVGZoomEvent) {

        SVGZoomEvent.SVGZoom = "SVGZoom";

    }(SVGZoomEvent = EventType.SVGZoomEvent || (EventType.SVGZoomEvent = {})));
    let TimeEvent;
    (function (TimeEvent) {

        TimeEvent.beginEvent = "beginEvent";
        TimeEvent.endEvent = "endEvent";
        TimeEvent.repeatEvent = "repeatEvent";

    }(TimeEvent = EventType.TimeEvent || (EventType.TimeEvent = {})));
    let TouchEvent;
    (function (TouchEvent) {

        TouchEvent.touchcancel = "touchcancel";
        TouchEvent.touchend = "touchend";
        TouchEvent.touchmove = "touchmove";
        TouchEvent.touchstart = "touchstart";

    }(TouchEvent = EventType.TouchEvent || (EventType.TouchEvent = {})));
    let TransitionEvent;
    (function (TransitionEvent) {

        TransitionEvent.transitionend = "transitionend";

    }(TransitionEvent = EventType.TransitionEvent || (EventType.TransitionEvent = {})));
    let UIEvent;
    (function (UIEvent) {

        UIEvent.abort = "abort";
        UIEvent.error = "error";
        UIEvent.load = "load";
        UIEvent.resize = "resize";
        UIEvent.scroll = "scroll";
        UIEvent.select = "select";
        UIEvent.unload = "unload";

    }(UIEvent = EventType.UIEvent || (EventType.UIEvent = {})));
    let UserProximityEvent;
    (function (UserProximityEvent) {

        UserProximityEvent.userproximity = "userproximity";

    }(UserProximityEvent = EventType.UserProximityEvent || (EventType.UserProximityEvent = {})));
    let WheelEvent;
    (function (WheelEvent) {

        WheelEvent.wheel = "wheel";

    }(WheelEvent = EventType.WheelEvent || (EventType.WheelEvent = {})));

}(EventType = exports.EventType || (exports.EventType = {})));
