"use strict";
exports.__esModule = true;
/* eslint-disable func-names */
/* eslint-disable func-style */
/* eslint-disable init-declarations */
/* eslint-disable max-len */
/* eslint-disable max-params */
/* eslint-disable max-statements */
/* eslint-disable no-shadow */
/* eslint-disable no-unused-vars */
var EventListener;
(function (EventListener) {
    function eventTarget(method) {
        return function (event) { return method(event); };
    }
    function currentTarget(method) {
        return function (event) { return method(event.currentTarget); };
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
    function invokeNow(selected, method) {
        selected.forEach(function (element) {
            method(element);
        });
    }
    function addEventListener(selected, type, callback, capture) {
        selected.forEach(function (element) {
            element.addEventListener(type, callback, capture);
        });
    }
    function SelectAllEventTargetBubblePhaseInvokeLater(selector, type, method) {
        var callback = eventTarget(method);
        var capture = bubblePhase();
        var selected = selectAll(selector);
        addEventListener(selected, type, callback, capture);
    }
    EventListener.SelectAllEventTargetBubblePhaseInvokeLater = SelectAllEventTargetBubblePhaseInvokeLater;
    function SelectAllEventTargetBubblePhaseInvokeNow(selector, type, method) {
        var callback = eventTarget(method);
        var capture = bubblePhase();
        var selected = selectAll(selector);
        invokeNow(selected, method);
        addEventListener(selected, type, callback, capture);
    }
    EventListener.SelectAllEventTargetBubblePhaseInvokeNow = SelectAllEventTargetBubblePhaseInvokeNow;
    function SelectAllEventTargetCapturePhaseInvokeLater(selector, type, method) {
        var callback = eventTarget(method);
        var capture = capturePhase();
        var selected = selectAll(selector);
        addEventListener(selected, type, callback, capture);
    }
    EventListener.SelectAllEventTargetCapturePhaseInvokeLater = SelectAllEventTargetCapturePhaseInvokeLater;
    function SelectAllEventTargetCapturePhaseInvokeNow(selector, type, method) {
        var callback = eventTarget(method);
        var capture = capturePhase();
        var selected = selectAll(selector);
        invokeNow(selected, method);
        addEventListener(selected, type, callback, capture);
    }
    EventListener.SelectAllEventTargetCapturePhaseInvokeNow = SelectAllEventTargetCapturePhaseInvokeNow;
    function SelectAllCurrentTargetBubblePhaseInvokeLater(selector, type, method) {
        var callback = currentTarget(method);
        var capture = bubblePhase();
        var selected = selectAll(selector);
        addEventListener(selected, type, callback, capture);
    }
    EventListener.SelectAllCurrentTargetBubblePhaseInvokeLater = SelectAllCurrentTargetBubblePhaseInvokeLater;
    function SelectAllCurrentTargetBubblePhaseInvokeNow(selector, type, method) {
        var callback = currentTarget(method);
        var capture = bubblePhase();
        var selected = selectAll(selector);
        invokeNow(selected, method);
        addEventListener(selected, type, callback, capture);
    }
    EventListener.SelectAllCurrentTargetBubblePhaseInvokeNow = SelectAllCurrentTargetBubblePhaseInvokeNow;
    function SelectAllCurrentTargetCapturePhaseInvokeLater(selector, type, method) {
        var callback = currentTarget(method);
        var capture = capturePhase();
        var selected = selectAll(selector);
        addEventListener(selected, type, callback, capture);
    }
    EventListener.SelectAllCurrentTargetCapturePhaseInvokeLater = SelectAllCurrentTargetCapturePhaseInvokeLater;
    function SelectAllCurrentTargetCapturePhaseInvokeNow(selector, type, method) {
        var callback = currentTarget(method);
        var capture = capturePhase();
        var selected = selectAll(selector);
        invokeNow(selected, method);
        addEventListener(selected, type, callback, capture);
    }
    EventListener.SelectAllCurrentTargetCapturePhaseInvokeNow = SelectAllCurrentTargetCapturePhaseInvokeNow;
    function SelectFirstEventTargetBubblePhaseInvokeLater(selector, type, method) {
        var callback = eventTarget(method);
        var capture = bubblePhase();
        var selected = selectFirst(selector);
        addEventListener(selected, type, callback, capture);
    }
    EventListener.SelectFirstEventTargetBubblePhaseInvokeLater = SelectFirstEventTargetBubblePhaseInvokeLater;
    function SelectFirstEventTargetBubblePhaseInvokeNow(selector, type, method) {
        var callback = eventTarget(method);
        var capture = bubblePhase();
        var selected = selectFirst(selector);
        invokeNow(selected, method);
        addEventListener(selected, type, callback, capture);
    }
    EventListener.SelectFirstEventTargetBubblePhaseInvokeNow = SelectFirstEventTargetBubblePhaseInvokeNow;
    function SelectFirstEventTargetCapturePhaseInvokeLater(selector, type, method) {
        var callback = eventTarget(method);
        var capture = capturePhase();
        var selected = selectFirst(selector);
        addEventListener(selected, type, callback, capture);
    }
    EventListener.SelectFirstEventTargetCapturePhaseInvokeLater = SelectFirstEventTargetCapturePhaseInvokeLater;
    function SelectFirstEventTargetCapturePhaseInvokeNow(selector, type, method) {
        var callback = eventTarget(method);
        var capture = capturePhase();
        var selected = selectFirst(selector);
        invokeNow(selected, method);
        addEventListener(selected, type, callback, capture);
    }
    EventListener.SelectFirstEventTargetCapturePhaseInvokeNow = SelectFirstEventTargetCapturePhaseInvokeNow;
    function SelectFirstCurrentTargetBubblePhaseInvokeLater(selector, type, method) {
        var callback = currentTarget(method);
        var capture = bubblePhase();
        var selected = selectFirst(selector);
        addEventListener(selected, type, callback, capture);
    }
    EventListener.SelectFirstCurrentTargetBubblePhaseInvokeLater = SelectFirstCurrentTargetBubblePhaseInvokeLater;
    function SelectFirstCurrentTargetBubblePhaseInvokeNow(selector, type, method) {
        var callback = currentTarget(method);
        var capture = bubblePhase();
        var selected = selectFirst(selector);
        invokeNow(selected, method);
        addEventListener(selected, type, callback, capture);
    }
    EventListener.SelectFirstCurrentTargetBubblePhaseInvokeNow = SelectFirstCurrentTargetBubblePhaseInvokeNow;
    function SelectFirstCurrentTargetCapturePhaseInvokeLater(selector, type, method) {
        var callback = currentTarget(method);
        var capture = capturePhase();
        var selected = selectFirst(selector);
        addEventListener(selected, type, callback, capture);
    }
    EventListener.SelectFirstCurrentTargetCapturePhaseInvokeLater = SelectFirstCurrentTargetCapturePhaseInvokeLater;
    function SelectFirstCurrentTargetCapturePhaseInvokeNow(selector, type, method) {
        var callback = currentTarget(method);
        var capture = capturePhase();
        var selected = selectFirst(selector);
        invokeNow(selected, method);
        addEventListener(selected, type, callback, capture);
    }
    EventListener.SelectFirstCurrentTargetCapturePhaseInvokeNow = SelectFirstCurrentTargetCapturePhaseInvokeNow;
})(EventListener = exports.EventListener || (exports.EventListener = {}));
