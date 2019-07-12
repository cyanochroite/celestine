"use strict";
exports.__esModule = true;
/* eslint-disable complexity */
/* eslint-disable func-names */
/* eslint-disable init-declarations */
/* eslint-disable max-len */
/* eslint-disable max-statements */
/* eslint-disable no-shadow */
/* eslint-disable no-unused-vars */
/* eslint-disable one-var */
var EventType;
(function (EventType) {
    var AnimationEvent;
    (function (AnimationEvent) {
        AnimationEvent["animationcancel"] = "animationcancel";
        AnimationEvent["animationend"] = "animationend";
        AnimationEvent["animationiteration"] = "animationiteration";
        AnimationEvent["animationstart"] = "animationstart";
    })(AnimationEvent = EventType.AnimationEvent || (EventType.AnimationEvent = {}));
    var BeforeUnloadEvent;
    (function (BeforeUnloadEvent) {
        BeforeUnloadEvent["beforeunload"] = "beforeunload";
    })(BeforeUnloadEvent = EventType.BeforeUnloadEvent || (EventType.BeforeUnloadEvent = {}));
    var ClipboardEvent;
    (function (ClipboardEvent) {
        ClipboardEvent["copy"] = "copy";
        ClipboardEvent["cut"] = "cut";
        ClipboardEvent["paste"] = "paste";
    })(ClipboardEvent = EventType.ClipboardEvent || (EventType.ClipboardEvent = {}));
    var CompositionEvent;
    (function (CompositionEvent) {
        CompositionEvent["compositionend"] = "compositionend";
        CompositionEvent["compositionstart"] = "compositionstart";
        CompositionEvent["compositionupdate"] = "compositionupdate";
    })(CompositionEvent = EventType.CompositionEvent || (EventType.CompositionEvent = {}));
    var DeviceMotionEvent;
    (function (DeviceMotionEvent) {
        DeviceMotionEvent["devicemotion"] = "devicemotion";
    })(DeviceMotionEvent = EventType.DeviceMotionEvent || (EventType.DeviceMotionEvent = {}));
    var DeviceOrientationEvent;
    (function (DeviceOrientationEvent) {
        DeviceOrientationEvent["deviceorientation"] = "deviceorientation";
    })(DeviceOrientationEvent = EventType.DeviceOrientationEvent || (EventType.DeviceOrientationEvent = {}));
    var DragEvent;
    (function (DragEvent) {
        DragEvent["drag"] = "drag";
        DragEvent["dragend"] = "dragend";
        DragEvent["dragenter"] = "dragenter";
        DragEvent["dragleave"] = "dragleave";
        DragEvent["dragover"] = "dragover";
        DragEvent["dragstart"] = "dragstart";
        DragEvent["drop"] = "drop";
    })(DragEvent = EventType.DragEvent || (EventType.DragEvent = {}));
    var Event;
    (function (Event) {
        Event["abort"] = "abort";
        Event["afterprint"] = "afterprint";
        Event["appinstalled"] = "appinstalled";
        Event["audioend"] = "audioend";
        Event["audiostart"] = "audiostart";
        Event["beforeprint"] = "beforeprint";
        Event["canplay"] = "canplay";
        Event["canplaythrough"] = "canplaythrough";
        Event["change"] = "change";
        Event["chargingchange"] = "chargingchange";
        Event["chargingtimechange"] = "chargingtimechange";
        Event["close"] = "close";
        Event["devicechange"] = "devicechange";
        Event["dischargingtimechange"] = "dischargingtimechange";
        Event["DOMContentLoaded"] = "DOMContentLoaded";
        Event["durationchange"] = "durationchange";
        Event["emptied"] = "emptied";
        Event["end"] = "end";
        Event["ended"] = "ended";
        Event["error"] = "error";
        Event["fullscreenchange"] = "fullscreenchange";
        Event["fullscreenerror"] = "fullscreenerror";
        Event["input"] = "input";
        Event["invalid"] = "invalid";
        Event["languagechange"] = "languagechange";
        Event["levelchange"] = "levelchange";
        Event["loadeddata"] = "loadeddata";
        Event["loadedmetadata"] = "loadedmetadata";
        Event["offline"] = "offline";
        Event["online"] = "online";
        Event["open"] = "open";
        Event["orientationchange"] = "orientationchange";
        Event["pause"] = "pause";
        Event["play"] = "play";
        Event["playing"] = "playing";
        Event["pointerlockchange"] = "pointerlockchange";
        Event["pointerlockerror"] = "pointerlockerror";
        Event["ratechange"] = "ratechange";
        Event["readystatechange"] = "readystatechange";
        Event["reset"] = "reset";
        Event["seeked"] = "seeked";
        Event["seeking"] = "seeking";
        Event["selectionchange"] = "selectionchange";
        Event["selectstart"] = "selectstart";
        Event["slotchange"] = "slotchange";
        Event["soundend"] = "soundend";
        Event["soundstart"] = "soundstart";
        Event["speechend"] = "speechend";
        Event["speechstart"] = "speechstart";
        Event["stalled"] = "stalled";
        Event["start"] = "start";
        Event["submit"] = "submit";
        Event["success"] = "success";
        Event["suspend"] = "suspend";
        Event["timeupdate"] = "timeupdate";
        Event["upgradeneeded"] = "upgradeneeded";
        Event["visibilitychange"] = "visibilitychange";
        Event["voiceschanged"] = "voiceschanged";
        Event["volumechange"] = "volumechange";
        Event["waiting"] = "waiting";
        Event["complete"] = "complete";
        Event["versionchange"] = "versionchange";
    })(Event = EventType.Event || (EventType.Event = {}));
    var ExtendableMessageEvent;
    (function (ExtendableMessageEvent) {
        ExtendableMessageEvent["message"] = "message";
    })(ExtendableMessageEvent = EventType.ExtendableMessageEvent || (EventType.ExtendableMessageEvent = {}));
    var FocusEvent;
    (function (FocusEvent) {
        FocusEvent["blur"] = "blur";
        FocusEvent["focus"] = "focus";
        FocusEvent["focusin"] = "focusin";
        FocusEvent["focusout"] = "focusout";
    })(FocusEvent = EventType.FocusEvent || (EventType.FocusEvent = {}));
    var GamepadEvent;
    (function (GamepadEvent) {
        GamepadEvent["gamepadconnected"] = "gamepadconnected";
        GamepadEvent["gamepaddisconnected"] = "gamepaddisconnected";
    })(GamepadEvent = EventType.GamepadEvent || (EventType.GamepadEvent = {}));
    var HashChangeEvent;
    (function (HashChangeEvent) {
        HashChangeEvent["hashchange"] = "hashchange";
    })(HashChangeEvent = EventType.HashChangeEvent || (EventType.HashChangeEvent = {}));
    var IDBVersionChangeEvent;
    (function (IDBVersionChangeEvent) {
        IDBVersionChangeEvent["blocked"] = "blocked";
    })(IDBVersionChangeEvent = EventType.IDBVersionChangeEvent || (EventType.IDBVersionChangeEvent = {}));
    var KeyboardEvent;
    (function (KeyboardEvent) {
        KeyboardEvent["keydown"] = "keydown";
        KeyboardEvent["keypress"] = "keypress";
        KeyboardEvent["keyup"] = "keyup";
    })(KeyboardEvent = EventType.KeyboardEvent || (EventType.KeyboardEvent = {}));
    var MessageEvent;
    (function (MessageEvent) {
        MessageEvent["message"] = "message";
        MessageEvent["messageerror"] = "messageerror";
    })(MessageEvent = EventType.MessageEvent || (EventType.MessageEvent = {}));
    var MouseEvent;
    (function (MouseEvent) {
        MouseEvent["click"] = "click";
        MouseEvent["contextmenu"] = "contextmenu";
        MouseEvent["dblclick"] = "dblclick";
        MouseEvent["mousedown"] = "mousedown";
        MouseEvent["mouseenter"] = "mouseenter";
        MouseEvent["mouseleave"] = "mouseleave";
        MouseEvent["mousemove"] = "mousemove";
        MouseEvent["mouseout"] = "mouseout";
        MouseEvent["mouseover"] = "mouseover";
        MouseEvent["mouseup"] = "mouseup";
        MouseEvent["show"] = "show";
    })(MouseEvent = EventType.MouseEvent || (EventType.MouseEvent = {}));
    var NotificationEvent;
    (function (NotificationEvent) {
        NotificationEvent["notificationclick"] = "notificationclick";
    })(NotificationEvent = EventType.NotificationEvent || (EventType.NotificationEvent = {}));
    var PageTransitionEvent;
    (function (PageTransitionEvent) {
        PageTransitionEvent["pagehide"] = "pagehide";
        PageTransitionEvent["pageshow"] = "pageshow";
    })(PageTransitionEvent = EventType.PageTransitionEvent || (EventType.PageTransitionEvent = {}));
    var Performance;
    (function (Performance) {
        Performance["resourcetimingbufferfull"] = "resourcetimingbufferfull";
    })(Performance = EventType.Performance || (EventType.Performance = {}));
    var PointerEvent;
    (function (PointerEvent) {
        PointerEvent["gotpointercapture"] = "gotpointercapture";
        PointerEvent["lostpointercapture"] = "lostpointercapture";
        PointerEvent["pointercancel"] = "pointercancel";
        PointerEvent["pointerdown"] = "pointerdown";
        PointerEvent["pointerenter"] = "pointerenter";
        PointerEvent["pointerleave"] = "pointerleave";
        PointerEvent["pointermove"] = "pointermove";
        PointerEvent["pointerout"] = "pointerout";
        PointerEvent["pointerover"] = "pointerover";
        PointerEvent["pointerup"] = "pointerup";
    })(PointerEvent = EventType.PointerEvent || (EventType.PointerEvent = {}));
    var PopStateEvent;
    (function (PopStateEvent) {
        PopStateEvent["popstate"] = "popstate";
    })(PopStateEvent = EventType.PopStateEvent || (EventType.PopStateEvent = {}));
    var ProgressEvent;
    (function (ProgressEvent) {
        ProgressEvent["abort"] = "abort";
        ProgressEvent["error"] = "error";
        ProgressEvent["load"] = "load";
        ProgressEvent["loadend"] = "loadend";
        ProgressEvent["loadstart"] = "loadstart";
        ProgressEvent["progress"] = "progress";
        ProgressEvent["timeout"] = "timeout";
    })(ProgressEvent = EventType.ProgressEvent || (EventType.ProgressEvent = {}));
    var PushEvent;
    (function (PushEvent) {
        PushEvent["push"] = "push";
        PushEvent["pushsubscriptionchange"] = "pushsubscriptionchange";
    })(PushEvent = EventType.PushEvent || (EventType.PushEvent = {}));
    var ServiceWorkerMessageEvent;
    (function (ServiceWorkerMessageEvent) {
        ServiceWorkerMessageEvent["message"] = "message";
    })(ServiceWorkerMessageEvent = EventType.ServiceWorkerMessageEvent || (EventType.ServiceWorkerMessageEvent = {}));
    var SpeechRecognitionEvent;
    (function (SpeechRecognitionEvent) {
        SpeechRecognitionEvent["nomatch"] = "nomatch";
        SpeechRecognitionEvent["result"] = "result";
    })(SpeechRecognitionEvent = EventType.SpeechRecognitionEvent || (EventType.SpeechRecognitionEvent = {}));
    var SpeechSynthesisErrorEvent;
    (function (SpeechSynthesisErrorEvent) {
        SpeechSynthesisErrorEvent["error"] = "error";
    })(SpeechSynthesisErrorEvent = EventType.SpeechSynthesisErrorEvent || (EventType.SpeechSynthesisErrorEvent = {}));
    var SpeechSynthesisEvent;
    (function (SpeechSynthesisEvent) {
        SpeechSynthesisEvent["boundary"] = "boundary";
        SpeechSynthesisEvent["end"] = "end";
        SpeechSynthesisEvent["mark"] = "mark";
        SpeechSynthesisEvent["pause"] = "pause";
        SpeechSynthesisEvent["resume"] = "resume";
        SpeechSynthesisEvent["start"] = "start";
    })(SpeechSynthesisEvent = EventType.SpeechSynthesisEvent || (EventType.SpeechSynthesisEvent = {}));
    var StorageEvent;
    (function (StorageEvent) {
        StorageEvent["storage"] = "storage";
    })(StorageEvent = EventType.StorageEvent || (EventType.StorageEvent = {}));
    var SVGEvent;
    (function (SVGEvent) {
        SVGEvent["SVGAbort"] = "SVGAbort";
        SVGEvent["SVGError"] = "SVGError";
        SVGEvent["SVGLoad"] = "SVGLoad";
        SVGEvent["SVGResize"] = "SVGResize";
        SVGEvent["SVGScroll"] = "SVGScroll";
        SVGEvent["SVGUnload"] = "SVGUnload";
    })(SVGEvent = EventType.SVGEvent || (EventType.SVGEvent = {}));
    var SVGZoomEvent;
    (function (SVGZoomEvent) {
        SVGZoomEvent["SVGZoom"] = "SVGZoom";
    })(SVGZoomEvent = EventType.SVGZoomEvent || (EventType.SVGZoomEvent = {}));
    var TimeEvent;
    (function (TimeEvent) {
        TimeEvent["beginEvent"] = "beginEvent";
        TimeEvent["endEvent"] = "endEvent";
        TimeEvent["repeatEvent"] = "repeatEvent";
    })(TimeEvent = EventType.TimeEvent || (EventType.TimeEvent = {}));
    var TouchEvent;
    (function (TouchEvent) {
        TouchEvent["touchcancel"] = "touchcancel";
        TouchEvent["touchend"] = "touchend";
        TouchEvent["touchmove"] = "touchmove";
        TouchEvent["touchstart"] = "touchstart";
    })(TouchEvent = EventType.TouchEvent || (EventType.TouchEvent = {}));
    var TransitionEvent;
    (function (TransitionEvent) {
        TransitionEvent["transitionend"] = "transitionend";
    })(TransitionEvent = EventType.TransitionEvent || (EventType.TransitionEvent = {}));
    var UIEvent;
    (function (UIEvent) {
        UIEvent["abort"] = "abort";
        UIEvent["error"] = "error";
        UIEvent["load"] = "load";
        UIEvent["resize"] = "resize";
        UIEvent["scroll"] = "scroll";
        UIEvent["select"] = "select";
        UIEvent["unload"] = "unload";
    })(UIEvent = EventType.UIEvent || (EventType.UIEvent = {}));
    var UserProximityEvent;
    (function (UserProximityEvent) {
        UserProximityEvent["userproximity"] = "userproximity";
    })(UserProximityEvent = EventType.UserProximityEvent || (EventType.UserProximityEvent = {}));
    var WheelEvent;
    (function (WheelEvent) {
        WheelEvent["wheel"] = "wheel";
    })(WheelEvent = EventType.WheelEvent || (EventType.WheelEvent = {}));
})(EventType = exports.EventType || (exports.EventType = {}));
