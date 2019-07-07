"use strict";
exports.__esModule = true;
var EventListener;
(function (EventListener) {
    function eventTarget(method) {
        return function (event) { return method(event); };
    }
    function currentTarget(method) {
        return function (event) { return method(event.currentTarget); };
    }
    function invokeNow(selected, method) {
        selected.forEach(function (element) {
            method(element);
        });
    }
    function bubblePhase() {
        return false;
    }
    function capturePhase() {
        return true;
    }
    function selectAll(selector) {
        return [].slice.call(document.querySelectorAll(selector));
    }
    function selectFirst(selector) {
        return [document.querySelector(selector)];
    }
    function addEventListener(selected, type, callback, capture) {
        selected.forEach(function (element) {
            element.addEventListener(type, callback, capture);
        });
    }
    function SelectAllEventTargetBubblePhaseInvokeLater(selector, method) {
        var selected = selectAll(selector);
        var type = "blur";
        var callback = eventTarget(method);
        var capture = bubblePhase();
        addEventListener(selected, type, callback, capture);
    }
    EventListener.SelectAllEventTargetBubblePhaseInvokeLater = SelectAllEventTargetBubblePhaseInvokeLater;
    /*
    export function SelectAllEventTargetBubblePhaseInvokeNow(selector: string, method: (argument: Event | EventTarget) => void) {
        callback = eventTarget(method);
        capture = bubblePhase();
        const selected = selectAll(selector);
        invokeNow(selected, method);
        addEventListener(selected);
    }
    export function SelectAllEventTargetCapturePhaseInvokeLater(selector: string, method: (argument: Event | EventTarget) => void) {
        callback = eventTarget(method);
        capture = capturePhase();
        const selected = selectAll(selector);
        addEventListener(selected);
    }
    export function SelectAllEventTargetCapturePhaseInvokeNow(selector: string, method: (argument: Event | EventTarget) => void) {
        callback = eventTarget(method);
        capture = capturePhase();
        const selected = selectAll(selector);
        invokeNow(selected, method);
        addEventListener(selected);
    }
    export function SelectAllCurrentTargetBubblePhaseInvokeLater(selector: string, method: (argument: Event | EventTarget) => void) {
        callback = currentTarget(method);
        capture = bubblePhase();
        const selected = selectAll(selector);
        addEventListener(selected);
    }
    export function SelectAllCurrentTargetBubblePhaseInvokeNow(selector: string, method: (argument: Event | EventTarget) => void) {
        callback = currentTarget(method);
        capture = bubblePhase();
        const selected = selectAll(selector);
        invokeNow(selected, method);
        addEventListener(selected);
    }
    export function SelectAllCurrentTargetCapturePhaseInvokeLater(selector: string, method: (argument: Event | EventTarget) => void) {
        callback = currentTarget(method);
        capture = capturePhase();
        const selected = selectAll(selector);
        addEventListener(selected);
    }
    export function SelectAllCurrentTargetCapturePhaseInvokeNow(selector: string, method: (argument: Event | EventTarget) => void) {
        callback = currentTarget(method);
        capture = capturePhase();
        const selected = selectAll(selector);
        invokeNow(selected, method);
        addEventListener(selected);
    }
    export function SelectFirstEventTargetBubblePhaseInvokeLater(selector: string, method: (argument: Event | EventTarget) => void) {
        callback = eventTarget(method);
        capture = bubblePhase();
        const selected = selectFirst(selector);
        addEventListener(selected);
    }
    export function SelectFirstEventTargetBubblePhaseInvokeNow(selector: string, method: (argument: Event | EventTarget) => void) {
        callback = eventTarget(method);
        capture = bubblePhase();
        const selected = selectFirst(selector);
        invokeNow(selected, method);
        addEventListener(selected);
    }
    export function SelectFirstEventTargetCapturePhaseInvokeLater(selector: string, method: (argument: Event | EventTarget) => void) {
        callback = eventTarget(method);
        capture = capturePhase();
        const selected = selectFirst(selector);
        addEventListener(selected);
    }
    export function SelectFirstEventTargetCapturePhaseInvokeNow(selector: string, method: (argument: Event | EventTarget) => void) {
        callback = eventTarget(method);
        capture = capturePhase();
        const selected = selectFirst(selector);
        invokeNow(selected, method);
        addEventListener(selected);
    }
    export function SelectFirstCurrentTargetBubblePhaseInvokeLater(selector: string, method: (argument: Event | EventTarget) => void) {
        callback = currentTarget(method);
        capture = bubblePhase();
        const selected = selectFirst(selector);
        addEventListener(selected);
    }
    export function SelectFirstCurrentTargetBubblePhaseInvokeNow(selector: string, method: (argument: Event | EventTarget) => void) {
        callback = currentTarget(method);
        capture = bubblePhase();
        const selected = selectFirst(selector);
        invokeNow(selected, method);
        addEventListener(selected);
    }
    export function SelectFirstCurrentTargetCapturePhaseInvokeLater(selector: string, method: (argument: Event | EventTarget) => void) {
        callback = currentTarget(method);
        capture = capturePhase();
        const selected = selectFirst(selector);
        addEventListener(selected);
    }
    export function SelectFirstCurrentTargetCapturePhaseInvokeNow(selector: string, method: (argument: Event | EventTarget) => void) {
        const selected = selectFirst(selector);
        callback = currentTarget(method);
        capture = capturePhase();
        invokeNow(selected, method);
        addEventListener(selected);
    }
    */
})(EventListener = exports.EventListener || (exports.EventListener = {}));
